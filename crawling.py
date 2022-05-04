import ast
import csv
import re

from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException

import datetime
from tqdm import tqdm
import sys

from bs4 import BeautifulSoup
import urllib.request
from urllib.parse import quote

from Cleaning import *

if __name__ == "__main__":
    print("실행")


# 기사 크롤링
def crawling(uName, startDate, endDate):  # uName=대학명, sd=시작날짜, ed=종료날짜

    title_text = []  # 뉴스 제목
    date_text = []  # 날짜
    contents_text = []  # 뉴스 내용

    RESULT_PATH = './Data/'
    driver = webdriver.Chrome('chromedriver')
    BASE_URL = "https://search.naver.com/search.naver?&where=news&pd=3&query="
    DAYS_SEARCH = 1

    news_link = []

    req_start = 1
    err_count = 0

    SEARCH_WORD = uName
    start_dt = datetime.datetime.strptime(startDate, '%Y-%m-%d')
    last_dt = datetime.datetime.strptime(endDate, '%Y-%m-%d')

    fileName = uName[:4] + startDate + "~" + endDate

    while True:

        ds = start_dt.strftime('%Y.%m.%d')
        end_dt = min(start_dt + datetime.timedelta(days=DAYS_SEARCH), last_dt)
        de = end_dt.strftime('%Y.%m.%d')

        target_URL = BASE_URL + urllib.parse.quote(SEARCH_WORD) + "&start=" + str(req_start) + "&ds=" + ds + "&de=" + de

        try:
            driver.get(target_URL)
            response = driver.page_source

        except:
            print("driver.get Error! : " + target_URL)
            break

        soup = BeautifulSoup(response, "html.parser")

        req_start = req_start + 10
        title_info = soup.find_all('div', 'info_group')  # 개별 기사 정보 (링크 등)

        # 찾는게 없을 경우
        if not title_info:
            if end_dt < last_dt:
                print("No <div class=info_group>")
                start_dt = end_dt + datetime.timedelta(days=1)
                end_dt = start_dt + datetime.timedelta(days=DAYS_SEARCH)
                req_start = 1
                continue
            else:
                break

        for title in title_info:
            title_link = title.select('a')
            if (len(title_link) != 1):
                news_title_link = title_link[1]['href']
                if news_title_link in news_link:
                    continue
                else:
                    # 뉴스 링크 저장(중복제외)
                    news_link.append(news_title_link)
                    # 날짜 저장
                    news_date = title.select('span')
                    if (len(news_date)) == 2:
                        date_text.append(news_date[1].get_text())
                    else:
                        date_text.append(news_date[2].get_text())

        total_count = []

        for count in soup.find_all('div', 'sc_page_inner'):
            end_count = count.select('a')

        if (end_count[len(end_count) - 1]['aria-pressed'] == 'true'):
            if end_dt < last_dt:
                start_dt = end_dt + datetime.timedelta(days=1)
                end_dt = start_dt + datetime.timedelta(days=DAYS_SEARCH)
                req_start = 1
                continue
            else:
                break

    num = 0

    for n in tqdm(range(len(news_link))):

        # 긁어온 URL로 접속하기
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

        # 뉴스 제목 크롤링

        try:
            item = soup.find('div', class_="media_end_head_title")
            title = item.find('h2', class_="media_end_head_headline").get_text()
            title_text.append(title)

        except:
            title = "OUTLINK"
            title_text.append(title)

        # 뉴스 본문 크롤링

        try:
            content_of_article = soup.select('#dic_area')
            for item in content_of_article:
                text = re.sub('&nbsp; | &nbsp;| \n|\t|\r', '', item.get_text())
                text = re.sub('\n\n', '', text)

                contents_text.append(text.strip())

        except:
            doc = "OUTLINK"
            contents_text.append(doc)


    print(len(news_link), "건")

    driver.close()

    resulted = {'date': date_text, 'title': title_text, 'contents': contents_text}
    outputFileName = fileName + '.csv'
    df = pd.DataFrame(resulted)
    df.to_csv(RESULT_PATH + outputFileName, encoding='utf-8-sig', index=False)
    print("Completed!!!")


def test(): # 크롤링 테스트
    sd = datetime.date(2022,4,6)
    ed = datetime.date(2022,4,7)

    crawling("금오공과대학교", str(datetime.datetime.strptime(str(sd), '%Y-%m-%d').date()),
             str(datetime.datetime.strptime(str(ed), '%Y-%m-%d').date()))
