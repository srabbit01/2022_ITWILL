# -*- coding: utf-8 -*-
"""
step03_word2vec.py

유사 단어 검색 

1. pip install gensim
2. word2vec 개요 
  - 중심단어와 주변단어 벡터 간의 연산으로 유사단어 예측
3. word2vec 유형 
  1) CBOW : 주변단어 학습 -> 중심단어 예측 
  2) SKIP-Gram : 중심단어 -> 주변단어 예측 
"""

from gensim.models import Word2Vec # model 
import nltk
nltk.download('punkt') # nltk data download
from nltk.tokenize import word_tokenize # 문장 -> 단어 token
from nltk.tokenize import sent_tokenize # 문단 -> 문장 token
import pandas as pd # csv file


'''
https://www.kaggle.com/rounakbanik/the-movies-dataset
movies_metadata.csv : 파일 다운로드 
'''

# 1. dataset load 
path=r"C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML"
data = pd.read_csv(path+'/data/movies_metadata.csv')
print(data.info())


# 2. 변수 선택 & 전처리 
df = data[['title', 'overview']]
df = df.dropna(axis = 0) # 결측치 제거 
df.info()
'''
Int64Index: 44506 entries, 0 to 45465
Data columns (total 2 columns):
 #   Column    Non-Null Count  Dtype 
---  ------    --------------  ----- 
 0   title     44506 non-null  object
 1   overview  44506 non-null  object
 '''


# 3. token 생성 

# overview 단어 벡터 생성 
overview = df['overview'].tolist() # column -> list변환 
overview # list
len(overview) # 44506 : [0, 1, ~ ,44505]
overview[0] # 첫번째 문장 

# 문장 -> 단어
result = [word_tokenize(row) for row in overview ] 
len(result) # 44506
result[0] # 첫번째 문장 -> 단어 벡터
type(result)

# 4. word2vec 
help(Word2Vec)
# Skip-Gram
model = Word2Vec(sentences=result, window=5, min_count=1, sg=1) 
'''
- sentences: 분석하고자 할 단어 벡터 
- window: 1회 학습할 단어 개수 (n개의 단어를 묶어 학습)
         ex) window=2: my name is hong -> (my, name), (my, is), (my, hong)
             -> my: 중심단어, 이외 단어: 주변단어
- min_count: 단어 최소 출현 빈도수 (기본: 5)
- sg: 1인 경우 Skip-Gram 알고리즘 사용, 0인 경우 CBOW 알고리즘 사용 (기본: 0)
'''
# CBOW
model2 = Word2Vec(sentences=result, window=5, min_count=1, sg=0) 

# 5. 유사 단어 검색 
# Skip-Gram
word_search = model.wv.most_similar(['husband']) 
print('top5 :',  word_search[:5])
'''
Skip-Gram(sg=1)
top5 : [('boyfriend', 0.8680989146232605),
        ('lover', 0.8660980463027954),
        ('fiancé', 0.8102416396141052), 
        ('ex-husband', 0.7922183871269226), 
        ('ex-boyfriend', 0.7776419520378113)]
'''

# CBOW
word_search2 = model2.wv.most_similar(['husband']) 
print('top5 :',  word_search2[:5])
'''
top5 : [('mother', 0.8963012099266052), 
        ('boyfriend', 0.8945639133453369), 
        ('lover', 0.8905669450759888), 
        ('sister', 0.8736879825592041), 
        ('grandmother', 0.8479388952255249)]
'''
# 결과적으로 Skip-Gram 알고리즘이 더 성능이 좋음을 알 수 있음

# 다른 단어 검색하기
word_search = model.wv.most_similar(['woman']) 
print('top5 :',  word_search[:5])
'''
top5 : [('man', 0.8135198354721069), 
        ('girl', 0.7917199730873108), 
        ('lady', 0.7912495136260986), 
        ('heiress', 0.7848188877105713), 
        ('schoolgirl', 0.7839974761009216)]
'''
word_search = model.wv.most_similar(['success']) 
print('top5 :',  word_search[:5])
'''
top5 : [('fame', 0.8241891264915466),  -> 명성
        ('sensation', 0.7832537889480591), -> 새로운 혁명
        ('commercial', 0.7824046015739441), -> 상업
        ('stardom', 0.7800833582878113),
        ('popularity', 0.7753292322158813)] -> 인기
'''