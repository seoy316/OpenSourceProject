import pandas as pd
import csv
import os

from tqdm import tqdm

df1 = pd.read_csv("./report/금오공과2015.01.01~2015.12.31.csv")
df2 = pd.read_csv("./report/금오공과2016.01.01~2016.12.31.csv")
df3 = pd.read_csv("./report/금오공과2017.01.01~2017.12.31.csv")
df4 = pd.read_csv("./report/금오공과2018.01.01~2018.12.31.csv")
df5 = pd.read_csv("./report/금오공과2019.01.01~2019.12.31.csv")
df6 = pd.read_csv("./report/금오공과2020.01.01~2020.10.19.csv")

# print(df)

# selectdata = pd.DataFrame(df, columns=["contents"])

# print(selectdata)

my_edudic = ["BK21", "EU ICI-ECP", "LINC+", "LINC+", "NCS학습모듈 개발 및 보완", "WCI", "WCU", "WIE", "WISE", "고등교육평가인증",
                      "공공부문 인적자원개발 우수기관 인증제", "광역경제권인재양성", "교육부 소관 이공분야 연구개발", "교육역량강화", "교육협력", "국가장학",
                      "학술지 지원", "국립대학 육성", "글로벌 교육 지원", "글로벌박사", "글로벌 연구 네트워크", "글로벌 연구실", "녹색성장분야 전문대학원 육성",
                      "대학 취업 창업 지원", "대학교육역량강화", "대학자율역량강화지원", "대학재정지원", "대학혁신지원", "미래기초과학 핵심리더양성", "법학전문대학원 실무교육역량강화",
                      "법학전문대학원 취약계층 장학금 지원", "사회과학연구지원", "산업단지캠퍼스 및 산학융합지구 조성", "산업단지캠퍼스 제도 운영", "산학협력 선도대학 육성",
                      "산학협력 중심대학", "산학협력형 시범", "선취업 후진학 관련 평생교육", "성인문해교육 지원", "세계수준의 연구중심대학 육성", "신성장 전문대학원 육성",
                      "실험실 특화형 창업선도대학", "여대생 커리어 개발 지원", "연구윤리활동지원", "우수저서 사후 지원", "의과학자 육성 지원", "이공분야 ", "인문사회분야",
                      "인문 사회 연구", "인문학", "인문한국지원", "장애대학생 지원", "정부 해외인턴", "지방대학 특성화", "지역인재육성", "지역혁신", "커넥트 코리아",
                      "특성화 전문대학 육성", "평생학습 중심대학 육성", "학교 기업 지원", "학부교육선도대학", "학술지원", "학술자원공동관리 체계 구축", "학자금 이중지원 방지",
                      "학제간 융합 연구", "한국학 대중화 시범", "한국학 진흥", "최우수학과", "우수학과", "등록금", "성장", "발전", "교육", "신뢰", "운영", "교육부", "평가",
                      "양성", "추진", "과학", "위원회", "후원", "학습", "멘토링", "수업", "학회", "학술", "도서관", "교육과정"]


my_research= ["협약", "체결", "연구", "사업", "지원", "선정", "개최", "스마트 공장", "R&D", "업무", "기업", "평가", "MOU", "도약", "타결", "추진", "계약", "로봇 산업", "사회",
              "성과", "교류", "컨설팅", "산업", "기업", "협력", "산학", "개발", "융합", "선정", "중소기업", "혁신", "업체", "평가", "후원", "특허", "개발", "기술", "혁신", "업체",
              "스타트업", "반도체", "설립", "태양광"]

my_student =["총동창회", "출신", "선출", "입학생", "졸업", "등록금", "진로", "연합", "창업", "분야", "취업", "인재", "청년", "발명", "전공", "유학생", "인턴", "대학원", "실습",
             "스타트업", "출석"]

my_professor=["출신 교수", "교수", "교직원", "선출" , "총장", "연구", "연구자", "강사"]

my_prestudent =["수시 모집", "정시 모집", "모집", "경쟁률", "전형", "수시", "정시"]

my_culture =["초대전", "특강", "기념", "특강", "세미나", "동아리", "한국문화재단",  "문화", "장학금", "행사", "지원", "프로그램", "문화센터", "기부", "연극제", "보건", "시설", "예술", "미디어",
     "세미나", "토론회"]

for i in tqdm(my_edudic):
    # print(i)
    dfFiltered1 = df1[df1["contents"].str.contains(i + "사업")]
    dfFiltered2 = df2[df2["contents"].str.contains(i + "사업")]
    dfFiltered3 = df3[df3["contents"].str.contains(i + "사업")]
    dfFiltered4 = df4[df4["contents"].str.contains(i + "사업")]
    dfFiltered5 = df5[df5["contents"].str.contains(i + "사업")]
    dfFiltered6 = df6[df6["contents"].str.contains(i + "사업")]

    dfFiltered1 = dfFiltered1.assign(edudic=i)
    dfFiltered2 = dfFiltered2.assign(edudic=i)
    dfFiltered3 = dfFiltered3.assign(edudic=i)
    dfFiltered4 = dfFiltered4.assign(edudic=i)
    dfFiltered5 = dfFiltered5.assign(edudic=i)
    dfFiltered6 = dfFiltered6.assign(edudic=i)

    dfFiltered1 = dfFiltered1.reindex(columns=["edudic", "date", "title", "contents"])
    dfFiltered2 = dfFiltered2.reindex(columns=["edudic", "date", "title", "contents"])
    dfFiltered3 = dfFiltered3.reindex(columns=["edudic", "date", "title", "contents"])
    dfFiltered4 = dfFiltered4.reindex(columns=["edudic", "date", "title", "contents"])
    dfFiltered5 = dfFiltered5.reindex(columns=["edudic", "date", "title", "contents"])
    dfFiltered6 = dfFiltered6.reindex(columns=["edudic", "date", "title", "contents"])

    dfFiltered1.to_csv("./report/금오공과2015.01.01~2015.12.31_Filtered.csv", index=False, mode='a', encoding='utf-8-sig', header=False)
    dfFiltered2.to_csv("./report/금오공과2016.01.01~2016.12.31_Filtered.csv", index=False, mode='a', encoding='utf-8-sig', header=False)
    dfFiltered3.to_csv("./report/금오공과2017.01.01~2017.12.31_Filtered.csv", index=False, mode='a', encoding='utf-8-sig', header=False)
    dfFiltered4.to_csv("./report/금오공과2018.01.01~2018.12.31_Filtered.csv", index=False, mode='a', encoding='utf-8-sig', header=False)
    dfFiltered5.to_csv("./report/금오공과2019.01.01~2019.12.31_Filtered.csv", index=False, mode='a', encoding='utf-8-sig', header=False)
    dfFiltered6.to_csv("./report/금오공과2020.01.01~2020.10.19_Filtered.csv", index=False, mode='a', encoding='utf-8-sig', header=False)

for i in tqdm(my_research):
    # print(i)
    dfFiltered1 = df1[df1["contents"].str.contains(i)]
    dfFiltered2 = df2[df2["contents"].str.contains(i)]
    dfFiltered3 = df3[df3["contents"].str.contains(i)]
    dfFiltered4 = df4[df4["contents"].str.contains(i)]
    dfFiltered5 = df5[df5["contents"].str.contains(i)]
    dfFiltered6 = df6[df6["contents"].str.contains(i)]

    dfFiltered1 = dfFiltered1.assign(research=i)
    dfFiltered2 = dfFiltered2.assign(research=i)
    dfFiltered3 = dfFiltered3.assign(research=i)
    dfFiltered4 = dfFiltered4.assign(research=i)
    dfFiltered5 = dfFiltered5.assign(research=i)
    dfFiltered6 = dfFiltered6.assign(research=i)

    dfFiltered1 = dfFiltered1.reindex(columns=["research", "date", "title", "contents"])
    dfFiltered2 = dfFiltered2.reindex(columns=["research", "date", "title", "contents"])
    dfFiltered3 = dfFiltered3.reindex(columns=["research", "date", "title", "contents"])
    dfFiltered4 = dfFiltered4.reindex(columns=["research", "date", "title", "contents"])
    dfFiltered5 = dfFiltered5.reindex(columns=["research", "date", "title", "contents"])
    dfFiltered6 = dfFiltered6.reindex(columns=["research", "date", "title", "contents"])

    dfFiltered1.to_csv("./report/금오공과2015.01.01~2015.12.31_Filtered_research.csv", index=False, mode='a', encoding='utf-8-sig', header=False)
    dfFiltered2.to_csv("./report/금오공과2016.01.01~2016.12.31_Filtered_research.csv", index=False, mode='a', encoding='utf-8-sig', header=False)
    dfFiltered3.to_csv("./report/금오공과2017.01.01~2017.12.31_Filtered_research.csv", index=False, mode='a', encoding='utf-8-sig', header=False)
    dfFiltered4.to_csv("./report/금오공과2018.01.01~2018.12.31_Filtered_research.csv", index=False, mode='a', encoding='utf-8-sig', header=False)
    dfFiltered5.to_csv("./report/금오공과2019.01.01~2019.12.31_Filtered_research.csv", index=False, mode='a', encoding='utf-8-sig', header=False)
    dfFiltered6.to_csv("./report/금오공과2020.01.01~2020.10.19_Filtered_research.csv", index=False, mode='a', encoding='utf-8-sig', header=False)

for i in tqdm(my_student):
    # print(i)
    dfFiltered1 = df1[df1["contents"].str.contains(i)]
    dfFiltered2 = df2[df2["contents"].str.contains(i)]
    dfFiltered3 = df3[df3["contents"].str.contains(i)]
    dfFiltered4 = df4[df4["contents"].str.contains(i)]
    dfFiltered5 = df5[df5["contents"].str.contains(i)]
    dfFiltered6 = df6[df6["contents"].str.contains(i)]

    dfFiltered1 = dfFiltered1.assign(student=i)
    dfFiltered2 = dfFiltered2.assign(student=i)
    dfFiltered3 = dfFiltered3.assign(student=i)
    dfFiltered4 = dfFiltered4.assign(student=i)
    dfFiltered5 = dfFiltered5.assign(student=i)
    dfFiltered6 = dfFiltered6.assign(student=i)

    dfFiltered1 = dfFiltered1.reindex(columns=["student", "date", "title", "contents"])
    dfFiltered2 = dfFiltered2.reindex(columns=["student", "date", "title", "contents"])
    dfFiltered3 = dfFiltered3.reindex(columns=["student", "date", "title", "contents"])
    dfFiltered4 = dfFiltered4.reindex(columns=["student", "date", "title", "contents"])
    dfFiltered5 = dfFiltered5.reindex(columns=["student", "date", "title", "contents"])
    dfFiltered6 = dfFiltered6.reindex(columns=["student", "date", "title", "contents"])

    dfFiltered1.to_csv("./report/금오공과2015.01.01~2015.12.31_Filtered_student.csv", index=False, mode='a', encoding='utf-8-sig', header=False)
    dfFiltered2.to_csv("./report/금오공과2016.01.01~2016.12.31_Filtered_student.csv", index=False, mode='a', encoding='utf-8-sig', header=False)
    dfFiltered3.to_csv("./report/금오공과2017.01.01~2017.12.31_Filtered_student.csv", index=False, mode='a', encoding='utf-8-sig', header=False)
    dfFiltered4.to_csv("./report/금오공과2018.01.01~2018.12.31_Filtered_student.csv", index=False, mode='a', encoding='utf-8-sig', header=False)
    dfFiltered5.to_csv("./report/금오공과2019.01.01~2019.12.31_Filtered_student.csv", index=False, mode='a', encoding='utf-8-sig', header=False)
    dfFiltered6.to_csv("./report/금오공과2020.01.01~2020.10.19_Filtered_student.csv", index=False, mode='a', encoding='utf-8-sig', header=False)
