# -*- coding: utf-8 -*-
"""
step01_TfidfVectorizer.py

TFiDF 단어 생성기 : TfidfVectorizer  
  1. 단어 생성기(word tokenizer): 문장 -> 단어
  2. 단어 사전(word dictionary): (단어: 단어 식별 고유 수치)
  3. 희소행렬(sparse matrix) : 단어 출현 비율에 의해서 가중치 적용 행렬 
    1) TF 가중치 : 단어출현빈도수  
    2) TFiDF 가중치 : 단어출현빈도수(TF) x 문서출현빈도수의 역수(iDF) 
"""

from sklearn.feature_extraction.text import TfidfVectorizer # 단어 생성기

# 테스트 문장 
sentences = [
    "Mr. Green killed Colonel Mustard in the study with the candlestick. Mr. Green is not a very nice fellow.",
    "Professor Plum has a green plant in his study.",
    "Miss Scarlett watered Professor Plum's green plant while he was away from his office last week."
]

print(sentences)


# 1. 단어 생성기
obj = TfidfVectorizer() # 생성자 


# 2. 단어 사전 
fit = obj.fit(sentences) # 문장 적용 
voca = fit.vocabulary_ 
print(voca)
'''
{'mr': 14, 'green': 5, 'killed': 11, 'colonel': 2, 'mustard': 15, 'in': 9, 'the': 24, 'study': 23, 'with': 30, 'candlestick': 1, 'is': 10, 'not': 17, 'very': 25, 'nice': 16, 'fellow': 3, 'professor': 21, 'plum': 20, 'has': 6, 'plant': 19, 'his': 8, 'miss': 13, 'scarlett': 22, 'watered': 27, 'while': 29, 'he': 7, 'was': 26, 'away': 0, 'from': 4, 'office': 18, 'last': 12, 'week': 28}
# 단어 사전: {'단어': 고유숫자}
# 고유 숫자: 중복되지 않는 유일한 숫자(컴퓨터 인식) -> 부호화된 문자(나중에 해당 숫자로 분석 실행)
# 영문의 경우, 알파벳 우선순위대로 적용
'''
print(len(voca)) # 31

# 3. 희소행렬(sparse matrix): 문장 -> 희소행렬
sparse_mat = obj.fit_transform(sentences)
print(sparse_mat)
'''
  (doc,term)=(문서위치,고유숫자)
            가중치(Weight)=TFiDF
  (0, 3)	0.2205828828763741
  (0, 16)	0.2205828828763741 - fellow
  (0, 25)	0.2205828828763741
  (0, 17)	0.2205828828763741
  (0, 10)	0.2205828828763741
  ...
  (0, 24)	0.4411657657527482 - 'the'(정관사): 의미는 없으나 가중치 높음
  ...
  '''
type(sparse_mat) # scipy.sparse.csr.csr_matrix

# 4. scipy -> numpy
sparse_arr=sparse_mat.toarray()
print(sparse_arr)
'''
[[0.         0.22058288 0.22058288 0.22058288 0.         0.26055961
  0.         0.         0.         0.16775897 0.22058288 0.22058288
  0.         0.         0.44116577 0.22058288 0.22058288 0.22058288
  0.         0.         0.         0.         0.         0.16775897
  0.44116577 0.22058288 0.         0.         0.         0.
  0.22058288]
 [0.         0.         0.         0.         0.         0.26903992
  0.45552418 0.         0.34643788 0.34643788 0.         0.
  0.         0.         0.         0.         0.         0.
  0.         0.34643788 0.34643788 0.34643788 0.         0.34643788
  0.         0.         0.         0.         0.         0.
  0.        ]
 [0.27054288 0.         0.         0.         0.27054288 0.15978698
  0.         0.27054288 0.20575483 0.         0.         0.
  0.27054288 0.27054288 0.         0.         0.         0.
  0.27054288 0.20575483 0.20575483 0.20575483 0.27054288 0.
  0.         0.         0.27054288 0.27054288 0.27054288 0.27054288
  0.        ]]
'''
sparse_arr.shape # (3, 31)

# 5. scipy -> pandas
import pandas as pd
sparse_DF=pd.DataFrame(sparse_arr)
print(sparse_DF)








