# -*- coding: utf-8 -*-
"""
step06.word_count.py

뉴스 기사 -> word count -> 시각화
"""

# 1. file load
import pickle
path = 'C:\\work\\Crystal\\DataAnalysis\\[ITWILL]BigDataAnalysis_ExpertTraining\\04. Python Basic\\workspace\\chap10_Crawling\\data'

file=open(path+'/news_data.pkl',mode='rb')
news_data_load=pickle.load(file)

# 2. 전처리
# 전처리 함수
def clean_text(texts) :    
    from re import sub # re 모듈 가져오기 
    # 단계1 : 소문자 변경   
    texts_re = [ st.lower() for st in texts]
    # 단계2 : 숫자 제거 
    texts_re2 = [sub('[0-9]', '', st) for st in texts_re]    
    # 단계3 : 문장부호 제거 
    punc_str = '[,.?!:;]'
    texts_re3 = [sub(punc_str, '', st) for st in texts_re2]    
    # 단계4 : 특수문자 제거 
    spec_str = '[@#$%^&*()↑↓(\')"]'
    texts_re4 = [sub(spec_str, '', st) for st in texts_re3]    
    # 단계5 : 2칸 이상 공백(white space) 제거 
    texts_re5 = [' '.join(st.split()) for st in texts_re4 ]
    return texts_re5
news_data_clean=clean_text(news_data_load)
print(news_data_clean)

# 3. word count: 공백 기준 단어 생성
wc={}
for texts in news_data_clean:
    for word in texts.split():
        wc[word]=wc.get(word,0)+1
print(wc)
len(wc) # 231

# 2음절 이상 단어만 선정
# 객체 복제
wc2=wc.copy() # 내용만 복제
for k in wc.keys():
    if len(k)<2: # 1음절 단어 제거
        del wc2[k] # wc2 2음절 이하 단어 제거
len(wc2) # 212

# 4. top 10 단어 선정
from collections import Counter # class

count=Counter(wc2) # count 객체 생성
type(count) # collections.Counter
count # 튜플 내 딕셔너리 형색
top10=count.most_common(10)
top10 # 출현 빈도수 top10 출력

words=[] # 단어
counts=[] # 빈도수
for word, count in top10: #('검수완박', 5)
    words.append(word)
    counts.append(count)
print(words) # x축
print(counts) # y축

# 5. top 10 단어 시각화
import matplotlib.pyplot as plt # 별칭
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

# 1) 선 그래프 그리기b
plt.plot(words,counts) # (x축,y축)
plt.show()

# 2) 막대 그래프 그리기
plt.bar(words,counts) # (x축,y축)
plt.show()