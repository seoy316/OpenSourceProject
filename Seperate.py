import csv
import pandas as pd
import kss
from eunjeon import Mecab

read_list = []

df = pd.read_csv('./report/금오공과2020.01.01~2020.10.19.csv', encoding='utf-8') # 파일 바꾸면 됨
contents = df['contents']
cat_val = contents.values

for sent in kss.split_sentences(str(cat_val)):
    read_list.append(sent)

mecab = Mecab()
for line in read_list:
    print(mecab.pos(line))

