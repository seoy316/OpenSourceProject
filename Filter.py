import pandas as pd

df = pd.read_csv(r"C:\\Users\\USER.LAPTOP-1GI8MJIL\\Desktop\\Team\\OpenSourceProject\\report\\금오공과2015.01.01~2015.12.31.csv")

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
                      "학제간 융합 연구", "한국학 대중화 시범", "한국학 진흥"]

for i in my_edudic:
    print(i)
    dfFiltered = df[df["contents"].str.contains(i)]
    print(dfFiltered["contents"].count())
    # print(dfFiltered)

    print(dfFiltered)

    dfFiltered.to_csv(r"C:\\Users\\USER.LAPTOP-1GI8MJIL\\Desktop\\Team\\OpenSourceProject\\report\\test.csv")

# with open("C:\\Users\\USER.LAPTOP-1GI8MJIL\\Desktop\\Team\\OpenSourceProject\\report\\test.txt", "w", encoding="utf-8") as f:
#     f.write(str(dfFiltered))
#     f.write("\n")


