import pandas as pd

from eunjeon import Mecab
from tqdm import tqdm

input_file = './Filtered_Data/'
output_file = './Filtered_Data/금오공과Research_result.csv'

df1 = pd.read_csv(input_file+'금오공과Research_result.csv', engine="python", encoding="utf-8-sig")
# df2 = pd.read_csv(input_file+'금오공과Education_result.csv', engine="python", encoding="utf-8-sig")
# df3 = pd.read_csv(input_file+'금오공과Student_result.csv', engine="python", encoding="utf-8-sig")

mecab = Mecab(dicpath='C:/mecab/mecab-ko-dic')

# print(mecab.pos('빅데이터'))

contents1 = df1.values
# contents2 = df2.values
# contents3 = df3.values

result1 =[]
result2 =[]
result3 =[]

for i in tqdm(contents1):
    tmp = mecab.nouns(str(i))
    result1.extend(tmp)

# for i in tqdm(contents2):
#     tmp = mecab.nouns(str(i))
#     result2.extend(tmp)
#
# for i in tqdm(contents3):
#     tmp = mecab.nouns(str(i))
#     result3.extend(tmp)

sum1 = str(result1)
# sum2 = str(result2)
# sum3 = str(result3)

finish1 = sum1.replace("'","")
# finish2 = sum2.replace("'","")
# finish3 = sum3.replace("'","")


Category1 = open(input_file + '금오공과research.txt', mode='wt', encoding='utf-8')
# Category2 = open(input_file + '금오공과education.txt', mode='wt', encoding='utf-8')
# Category3 = open(input_file + '금오공과student.txt', mode='wt', encoding='utf-8')

Category1.write(finish1)
# Category2.write(finish2)
# Category3.write(finish3)

Category1.close()
# Category2.close()
# Category3.close()

#29810631
#29800914
#29793824
#29776044
#29766918
#29766667
#29737451
#29720599
#29664295