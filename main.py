import ast
import csv
import re

import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException

Input_Name = '경북대학교 "경북대"'  # str(input("대학 이름: "))
Input_Start = str(input("시작 날짜:"))
Input_End = str(input("종료 날짜:"))
Print_File = Input_Name[:4] + Input_Start + "~" + Input_End

RESULT_PATH = './report/'

title_text = []  # 뉴스 제목
date_text = []  # 날짜
contents_text = []  # 뉴스 내용
resulted = {}
result_test = []

driver = webdriver.Chrome('chromedriver')

import urllib.request
from bs4 import BeautifulSoup


def getFirstChild(parent, tagName):
    for child in parent.children:
        if child.name == tagName:
            return child
    return None


def getSearchResult(url):
    try:
        driver.get(url)
        response = driver.page_source
    except:
        print("driver.get Error! : " + url)
        return False, None, None, None

    soup = BeautifulSoup(response, "html.parser")

    search_count = 0

    title_desc_all_my = soup.find('div',
                                  class_="title_desc all_my")  # <div class="title_desc all_my"><span>1-10 / 682,261건</span></div>
    if title_desc_all_my is None:
        print("No <div class=title_desc all_my>")
        re = "try"  # 오류수정하려고 붙임
        return False, re, None, None  # 오류수정하려고 re 로 바꿈

    search_count_text = title_desc_all_my.find('span').get_text()  # 1-10 / 682,261건
    if search_count_text is None:
        print("No <span class=search_count_text>")
        return False, None, None, None

    search_count_text = search_count_text.replace(",", "")
    sep_pos = search_count_text.find("-")
    if sep_pos < 0:
        return False, None, None, None

    start_idx = int(search_count_text[:sep_pos])

    sep_pos = search_count_text.find("/")
    if sep_pos < 0:
        return False, None, None, None

    search_total_count = int(search_count_text[sep_pos + 1:len(search_count_text) - 1])

    return True, start_idx, search_total_count, soup


def clean_text(text):
    cleaned_text = re.sub('[a-zA-Z]', '', text)
    cleaned_text = re.sub('[\{\}\[\]\/?;|\)*~`!^\-_+<>@\#$%&\\\=◈\(\'\"◆★▷▶▲■◇△Δ○]', '', cleaned_text)
    cleaned_text = cleaned_text.replace("오류를 우회하기 위한 함수 추가", "")
    cleaned_text = cleaned_text.replace("동영상 뉴스 오류를 위한 함수 추가", "")
    cleaned_text = cleaned_text.replace("무단전재 및 재배포 금지", "")
    cleaned_text = cleaned_text.replace("본문 내용", "")
    cleaned_text = cleaned_text.replace("플레이어", "")
    cleaned_text = cleaned_text.replace("무단 전재 및 재배포 금지", "")
    return cleaned_text


# 날짜 정제화 함수
def date_cleansing(test):
    pattern = '\d+.(\d+).(\d+).'  # 정규표현식
    r = re.compile(pattern)
    match = r.search(test).group(0)  # 2018.11.05.
    return match


import sys
import datetime
from tqdm import tqdm

SEARCH_WORD = Input_Name
BASE_URL = "https://search.naver.com/search.naver?&where=news&pd=3&query="
DAYS_SEARCH = 1

news_link = []

req_start = 1
err_count = 0
total_result_count = 0

start_dt = datetime.datetime.strptime(Input_Start, '%Y.%m.%d')
last_dt = datetime.datetime.strptime(Input_End, '%Y.%m.%d')

ds = start_dt.strftime('%Y.%m.%d')
de = last_dt.strftime('%Y.%m.%d')

url = BASE_URL + urllib.parse.quote(SEARCH_WORD) + "&start=1&ds=" + ds + "&de=" + de
result = getSearchResult(url)
if not result[0]:
    print("Error getting url : " + url)
    sys.exit()

search_total_count = result[2]
print("search_total_count=" + str(search_total_count))
pbar = tqdm(total=search_total_count)

while True:

    ds = start_dt.strftime('%Y.%m.%d')
    end_dt = min(start_dt + datetime.timedelta(days=DAYS_SEARCH), last_dt)
    de = end_dt.strftime('%Y.%m.%d')

    url = BASE_URL + urllib.parse.quote(SEARCH_WORD) + "&start=" + str(req_start) + "&ds=" + ds + "&de=" + de

    result = getSearchResult(url)

    if result[1] == "try":  # 해당날짜에 기사가 없을 경우 오류나는거 해결하려고 붙임
        start_dt = end_dt + datetime.timedelta(days=1)
        end_dt = start_dt + datetime.timedelta(days=DAYS_SEARCH)
        err_count -= 1

    if not result[0]:
        err_count = err_count + 1
        continue

    if err_count >= 3:  # 3회 이상 오류나면 빠져나간다
        break

    start_idx = result[1]
    if start_idx < req_start:
        if end_dt < last_dt:
            start_dt = end_dt + datetime.timedelta(days=1)
            end_dt = start_dt + datetime.timedelta(days=DAYS_SEARCH)
            req_start = 1
            continue
        else:
            break

    soup = result[3]

    news_lists = []

    page_item_count = 0
    for child in soup.find('ul', class_="type01").children:
        if child.name == "li":
            news_lists.append(child)
            page_item_count = page_item_count + 1

    req_start = req_start + page_item_count
    for news in news_lists:
        news_target1 = getFirstChild(news,
                                     "dl")  # 바로 밑의 <dl> <dt><a>...</a></dt> <dd><span>디지털타임스</span>5일 전<a>네이버뉴스</a></dd> </dl>
        news_target2 = getFirstChild(news_target1, "dd")  # 바로 밑의 <dd>
        news_target3 = getFirstChild(news_target2, "a")  # 바로 밑의 <a> => Naver뉴스 인 경우만 있다
        num = 0

        if news_target3 is not None:
            if "naver" in news_target3.attrs['href']:
                news_item_link = news_target3.attrs['href']
                if news_item_link in news_link :    # 중복된 기사는 넘김
                    continue
                else:
                    news_link.append(news_item_link)
                    date_list = news_target1.select('.txt_inline')
                    date_text.append(date_cleansing(str(date_list)))
                    title_list = news_target1.find('dt', '').find('a').text.strip("\n\t\r")
                    title_text.append(title_list)

    if pbar is not None:
        pbar.update(page_item_count)

if pbar is not None:
    pbar.close()


print(len(news_link))

naver_news_title = []
naver_news_content = []
num = 0

for n in tqdm(range(len(news_link))):

    ########### 긁어온 URL로 접속하기 ############
    try:
        driver.get(news_link[n])

    except:
        print("Error! getting url=" + news_link[n])
        continue

    try:
        response = driver.page_source

    except UnexpectedAlertPresentException:
        driver.Alert.accept()
        print("게시글이 삭제된 경우입니다.")
        continue

    soup = BeautifulSoup(response, "html.parser")

    ###### 뉴스 타이틀 긁어오기 ######

    title = None

    try:
        item = soup.find('div', class_="article_info")
        title = item.find('h3', class_="tts_head").get_text()

    except:
        title = "OUTLINK"

    naver_news_title.append(title)

    ###### 뉴스 본문 긁어오기 ######

    doc = None
    text = ""

    data = soup.find_all("div", {"class": "_article_body_contents"})

    if data:
        for item in data:
            text = text + str(item.find_all(text=True)).strip()
            text = ast.literal_eval(text)
            doc = ' '.join(text)
            cleand = clean_text(doc)
    else:
        doc = "OUTLINK"

    contents_text.append(cleand.strip())

resulted = {'date': date_text, 'title': title_text, 'contents': contents_text }
outputFileName = Print_File + '.csv'
df = pd.DataFrame(resulted)
df.to_csv(RESULT_PATH + outputFileName, encoding='utf-8')
print("Completed!!!")
