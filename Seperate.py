import pandas as pd
import glob
import os

root_dir = './Filtered_Data/'

# contents = []
#
# f = open(root_dir + '금오공과_research.txt', mode='a', encoding='utf-8')
#
#
# df1 = pd.read_csv(root_dir+'금오공과2020_F_research.csv', encoding='utf-8-sig')
# df2 = pd.read_csv(root_dir+'금오공과2019_F_research.csv', encoding='utf-8-sig')
# df3 = pd.read_csv(root_dir+'금오공과2018_F_research.csv', encoding='utf-8-sig')
# df4 = pd.read_csv(root_dir+'금오공과2017_F_research.csv', encoding='utf-8-sig')
# df5 = pd.read_csv(root_dir+'금오공과2016_F_research.csv', encoding='utf-8-sig')
# df6 = pd.read_csv(root_dir+'금오공과2015_F_research.csv', encoding='utf-8-sig')
#
#
# contents2 = df2['contents']
# contents3 = df3['contents']
#
# read_list.append(contents1.values)
# read_list.append(contents2.values)
# read_list.append(contents3.values)


input_file = './Filtered_Data/'
output_file = './Filtered_Data/금오공과Education_result.csv'

allFile_list = glob.glob(os.path.join(input_file, "*edu.csv"))
print(allFile_list)

allData = []
for file in allFile_list:
    df = pd.read_csv(file, engine="python", encoding="utf-8-sig")
    data = df['contents']
    allData.append(data)

dataCombine = pd.concat(allData, axis=0,ignore_index=True)
dataCombine.to_csv(output_file, index=False, encoding='utf-8-sig')

result_line = pd.read_csv( "./Filtered_Data/금오공과Education_result.csv", engine='python',encoding='utf-8-sig')
result_line.head(30)


