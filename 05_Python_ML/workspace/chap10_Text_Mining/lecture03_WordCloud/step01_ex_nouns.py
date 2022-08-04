# -*- coding: utf-8 -*-
"""
step01_ex_nouns.py

1. text file 읽기 
2. 명사 추출 : kkma
3. 전처리 : 단어 길이 제한, 숫자 제외 
4. 단어 구름 시각화 : install 필요 - ppt 참고
"""

from konlpy.tag import Kkma # class - 형태소 
from wordcloud import WordCloud # class - 단어 구름 시각화 

# 1. text file 읽기 
path=r"C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05_Python_ML"
path = path + r'\workspace\chap10_Text_Mining\data'
file = open(path + '/text_data.txt', mode='r', encoding='utf-8')
data = file.read()
print(data)
'''
# 문단 단위: 문장 포함
형태소 분석을 시작합니다. 나는 데이터 분석을 좋아합니다. 
직업은 데이터 분석 전문가 입니다. Text mining 기법은 2000대 초반에 개발된 기술이다.
'''
file.close()

# 2. 문장 추출 
kkma = Kkma() # 형태소 분석기 생성

# 문단(str) -> 문장(list) 
ex_sent = kkma.sentences(data)
print(ex_sent) # list 
'''
['형태소 분석을 시작합니다.', '나는 데이터 분석을 좋아합니다.',
 '직업은 데이터 분석 전문가 입니다.',
 'Text mining 기법은 2000대 초반에 개발된 기술이다.']
'''

# 문단 -> 명사(단어)
ex_nouns=kkma.nouns(data) # 이렇게 하지 X
print(ex_nouns)
'''
['형태소', '분석', '나', '데이터', '직업', '전문가', '기법',
 '2000', '2000대', '대', '초반', '개발', '기술']
# 유일한 명사 하나만 추출 (중복 X)
'''

# 3. 명사 추출 : 문장 -> 명사 
nouns = [] # 중복 명사 저장

for sent in ex_sent : # '형태소 분석을 시작합니다.'    
    for noun in kkma.nouns(sent) : # 문장 -> 명사 추출 
        nouns.append(noun)
print(nouns)
'''
['형태소', '분석', '데이터', '분석', '직업', '데이터', '분석', 
 '전문가', '기법', '2000', '2000대', '대', '초반', '개발', '기술']
# 중복 명사도 추출 -> word count하기 위해
'''


# 4. 전처리 
from re import match # 숫자 제외 

nouns_count = {} # 단어 카운터 

for noun in nouns : 
    # 접두어가 숫자로 시작하지 않는 단어 추출 X
    if len(noun) > 1 and not(match('^[0-9]', noun)) :
        nouns_count[noun] = nouns_count.get(noun, 0) + 1
        
print(nouns_count)        
'''
word count
{'형태소': 1, '분석': 3, '데이터': 2, '직업': 1, '전문가': 1,
 '기법': 1, '초반': 1, '개발': 1, '기술': 1}
'''
nouns2=[]
for noun in nouns:
    if len(noun)>1 and not(match('^[0-9]', noun)):
        nouns2.append(noun)

# 5. 단어 구름 시각화

# 1) Top5 word  
from collections import Counter # class 

word_count = Counter(nouns_count)
'''
Counter({'형태소': 1,
         '분석': 3,
         '데이터': 2,
         '직업': 1,
         '전문가': 1,
         '기법': 1,
         '초반': 1,
         '개발': 1,
         '기술': 1})
'''
word_count2 = Counter(nouns2)
'''
Counter({'형태소': 1,
         '분석': 3,
         '데이터': 2,
         '직업': 1,
         '전문가': 1,
         '기법': 1,
         '초반': 1,
         '개발': 1,
         '기술': 1})
'''
# 출현 빈도수 상위 5개만 추출
top5_word = word_count.most_common(5) # top5
print(top5_word)
# [('분석', 3), ('데이터', 2), ('형태소', 1),
# ('직업', 1), ('전문가', 1)]

# 2) word cloud 
wc = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf',
          width=500, height=400,
          max_words=100,max_font_size=150,
          background_color='white')
'''
- font_path: 글꼴 경로 지정
- height: 세로, height: 가로
- max_words: 최대 단어 개수
- max_font_size: 최대 단어 크기
- background_color: 배경 색상
'''

wc_result = wc.generate_from_frequencies(dict(top5_word))

import matplotlib.pyplot as plt 

plt.imshow(wc_result)
plt.axis('off') # 축 눈금 감추기 
plt.show()







