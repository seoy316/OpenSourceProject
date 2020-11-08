import pandas as pd
import csv
import os
import numpy as np

from tqdm import tqdm

from Cleaning import *

toPath = './report/'
fromPath = './CleanFile/'

df1 = pd.read_csv(toPath + "금오공과2015.01.01~2015.12.31.csv")
df2 = pd.read_csv(toPath + "금오공과2016.01.01~2016.12.31.csv")
df3 = pd.read_csv(toPath + "금오공과2017.01.01~2017.12.31.csv")
df4 = pd.read_csv(toPath + "금오공과2018.01.01~2018.12.31.csv")
df5 = pd.read_csv(toPath + "금오공과2019.01.01~2019.12.31.csv")
df6 = pd.read_csv(toPath + "금오공과2020.01.01~2020.10.19.csv")

data1 = df1['contents']
data2 = df2['contents']
data3 = df3['contents']
data4 = df4['contents']
data5 = df5['contents']
data6 = df6['contents']

contents = []
for i in data1.values:
    contents.append(clean_text(i))

df1.loc[:, ['contents']] = contents
df1 = df1.reindex(columns=["date", "title", "contents"])
df1.to_csv(fromPath + "금오공과2015.01.01~2015.12.31.csv", index=False, mode='wt', encoding='utf-8-sig', header=False)


contents=[]
for i in data2.values:
    contents.append(clean_text(i))

df2.loc[:, ['contents']] = contents
df2 = df2.reindex(columns=["date", "title", "contents"])
df2.to_csv(fromPath + "금오공과2016.01.01~2016.12.31.csv", index=False, mode='wt', encoding='utf-8-sig', header=False)


contents=[]
for i in data3.values:
    contents.append(clean_text(i))

df3.loc[:, ['contents']] = contents
df3 = df3.reindex(columns=["date", "title", "contents"])
df3.to_csv(fromPath + "금오공과2017.01.01~2017.12.31.csv", index=False, mode='wt', encoding='utf-8-sig', header=False)


contents=[]
for i in data4.values:
    contents.append(clean_text(i))

df4.loc[:, ['contents']] = contents
df4 = df4.reindex(columns=["date", "title", "contents"])
df4.to_csv(fromPath + "금오공과2018.01.01~2018.12.31.csv", index=False, mode='wt', encoding='utf-8-sig', header=False)


contents=[]
for i in data5.values:
    contents.append(clean_text(i))

df5.loc[:, ['contents']] = contents
df5 = df5.reindex(columns=["date", "title", "contents"])
df5.to_csv(fromPath + "금오공과2019.01.01~2019.12.31.csv", index=False, mode='wt', encoding='utf-8-sig', header=False)


contents=[]
for i in data6.values:
    contents.append(clean_text(i))

df6.loc[:, ['contents']] = contents
df6 = df6.reindex(columns=["date", "title", "contents"])
df6.to_csv(fromPath + "금오공과2020.01.01~2020.10.19.csv", index=False, mode='wt', encoding='utf-8-sig', header=False)

