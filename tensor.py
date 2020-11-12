from konlpy.tag import Twitter, Okt
from gensim.models import Word2Vec
import csv

from tqdm import tqdm

twitter = Okt()

file = open("./Filtered_Data/금오공과research.txt", 'r', encoding='utf-8-sig')
line = file.readline()
token = []
embeddingmodel = []

category = ['교육', '연구/사업', '재학생/졸업생', '신입생', '교수진', '문화/기타']

for i in tqdm(line):
    sentence = twitter.pos(i[0], norm=True, stem=True)
    temp = []
    temp_embedding = []
    all_temp = []
    for k in range(len(sentence)):
        temp_embedding.append(sentence[k][0])
        temp.append(sentence[k][0] + '/' + sentence[k][1])
    all_temp.append(temp)
    embeddingmodel.append(temp_embedding)
    category_number_dic = {'교육': 0, '연구/사업': 1, '재학생/졸업생': 2, '신입생': 3, '교수진': 4, '문화/기타': 5}
    all_temp.append(category_number_dic.get(str(category)))
    token.append(all_temp)
print("토큰 처리 완료")

embeddingmodel = []
for i in tqdm(range(len(token))):
    temp_embeddingmodel = []
    for k in range(len(token[i][0])):
        temp_embeddingmodel.append(token[i][0][k])
    embeddingmodel.append(temp_embeddingmodel)

embedding = Word2Vec(embeddingmodel, size=300, window=5, min_count=10, iter=5, sg=1, max_vocab_size=360000000)
embedding.save('post.embedding')
