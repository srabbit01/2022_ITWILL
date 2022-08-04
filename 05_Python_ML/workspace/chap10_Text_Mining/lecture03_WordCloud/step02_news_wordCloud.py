# -*- coding: utf-8 -*-
"""
step02_news_wordCloud.py

1. pickle file 읽기 : news(5개월)
2. 문장 추출 : Okt
3. 명사 추출 : Okt
4. 전처리 : 단어 길이 제한, 숫자 제외 
5. Word Cloud
"""

from konlpy.tag import Okt # class - 형태소 
from wordcloud import WordCloud # class - 단어 구름 시각화 
import pickle # pickle file 읽기 

# 1. pickle file 읽기
path=r"C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML"
path = path + r'\workspace\chap10_Text_Mining\data'

# file load 
file = open(path + '/news_data.pkl', mode='rb')
news_data = pickle.load(file)
file.close()

news_data[0] # 2021-11-01
news_data[-1] # 2022-03-31

okt = Okt() # object

# 2. 문단(str) -> 문장(list) 
ex_sents = []
for sent in news_data : # news_data[:1]
    para = sent[0] # 문단 추출 (색인 필요)
    # 문단 -> 문장
    sents = okt.normalize(para) # 문장(문자열) 반환 
    print(sents)
    ex_sents.append(sents) # 단일list 저장 
print(ex_sents)
len(ex_sents) # 151 = 5개월 * 하루 

# 3. 명사 추출 : Kkma
nouns_word = [] # 명사 저장 

for sent in ex_sents :
    for noun in okt.nouns(sent): # 서수 제외 
        nouns_word.append(noun)

len(nouns_word) # 1189


# 4. 단어 전처리 & 카운터 : 단어 길이 제한, 숫자 제외
nouns_count = {} # 단어 카운터 

for noun in nouns_word : 
    if len(noun) > 1 : # 2음절 이상 단어 선정
        nouns_count[noun] = nouns_count.get(noun, 0) + 1
        
print(nouns_count) # dict
# ('종합', 12) 단어 제거
del nouns_count['종합']


# 5. 단어 구름 시각화

# 1) TopN word  
from collections import Counter # class 

word_count = Counter(nouns_count)
type(top100_word)
top100_word = word_count.most_common(100) # top 100
print(top100_word)
'''
[('코로나', 16), ('종합', 12), ('이재명', 9), ('감염', 8),
 ('정부', 8), ('윤석열', 7), ('신규', 7), ('추가', 7), ('검토', 6),
 ('오미크론', 6), ('방역', 5), ('바이든', 5), ('일본', 5),
 ('밀리터리', 4), ('동서남북', 4), ('사망', 4), ('위해', 4),
 ('대책', 4), ('검찰', 4), ('사흘', 4), ('홍콩', 4), ('전차', 4),
 ('외무', 3), ('추진', 3), ('인상', 3), ('금리', 3), ('전략', 3),
 ('울산', 3), ('부족', 3), ('미래', 3), ('거리', 3), ('의회', 3),
 ('확산', 3), ('이준석', 3), ('중환자', 3), ('속보', 3), ('사회', 3),
 ('국민', 3), ('협상', 3), ('서울', 3), ('강화', 3), ('미접', 3),
 ('종자', 3), ('접종', 3), ('완화', 3), ('개발', 3), ('행위', 3),
 ('명대', 3), ('발사', 3), ('나토', 3), ('러시아', 3), ('제한', 3),
 ('의무', 3), ('물가', 3), ('미사일', 3), ('배치', 3), ('지원', 3),
 ('침공', 3), ('내정', 2), ('미정', 2), ('인플레', 2), ('파업', 2),
 ('지속', 2), ('세계', 2), ('민심', 2), ('강원도', 2), ('총리', 2),
 ('식사', 2), ('위반', 2), ('외교', 2), ('실종', 2), ('대선', 2),
 ('병상', 2), ('가동', 2), ('주장', 2), ('조치', 2), ('대화', 2),
 ('정직', 2), ('조문', 2), ('독일', 2), ('공급', 2), ('공략', 2),
 ('후보', 2), ('의혹', 2), ('소환', 2), ('이란', 2), ('총력', 2),
 ('회장', 2), ('승인', 2), ('패스', 2), ('강진', 2), ('기준', 2),
 ('가치', 2), ('심층', 2), ('인터뷰', 2), ('수능', 2), ('시행', 2),
 ('타격', 2), ('유럽', 2), ('국내', 2)]
# 일부 의미 없으나 출현 빈도수 높은 단어는 삭제하기
# 예시: '종합' 등
'''

# 2) word cloud 
wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf',
          width=500, height=400,
          max_words=100,max_font_size=150,
          background_color='white')


wc_result = wc.generate_from_frequencies(dict(top100_word))

import matplotlib.pyplot as plt 

plt.imshow(wc_result)
plt.axis('off') # 축 눈금 감추기 
plt.show()






