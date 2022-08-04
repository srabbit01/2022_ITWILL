# -*- coding: utf-8 -*-
"""
step02_Tfidf_sparse_matrix.py

<작업 순서>
 1. csv file 가져오기 : temp_spam_data.csv
 2. texts, target 전처리 
 3. max features -> 최대 단어의 개수
 4. sparse matrix : TFiDF 가중치 
"""

import pandas as pd # csv file 
from sklearn.feature_extraction.text import TfidfVectorizer # sparse matrix 

## 1. csv file 가져오기 
path = r"C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML\data"
spam_data = pd.read_csv(path + '/temp_spam_data.csv',header=None, encoding='utf-8')

print(spam_data.info())
print(spam_data)
'''
      0                        1
0   ham    우리나라    대한민국, 우리나라 만세
1  spam      비아그라 500GRAM 정력 최고!
2   ham               나는 대한민국 사람
3  spam  보험료 15000원에 평생 보장 마감 임박
4   ham                   나는 홍길동
# 0: 정답, 1: 문장(문제)
'''

## 2. texts, target 전처리

# 1) target 전처리 : dummy변수 
target = spam_data[0]
target 
# list 내포
target = [1 if t == 'spam' else 0 for t in target ]
print(target) 

# 2) texts 전처리 : 공백, 특수문자, 숫자  
texts = spam_data[1]

print('전처리 전')
print(texts)

# << texts 전처리 함수 >> 
import string 
def text_prepro(texts): 
    # Lower case: 소문자
    texts = [x.lower() for x in texts]
    # Remove punctuation: 문장부호 제거  
    texts = [''.join(ch for ch in st if ch not in string.punctuation) for st in texts]
    # Remove numbers: 숫자 제거
    texts = [''.join(ch for ch in st if ch not in string.digits) for st in texts]
    # Trim extra whitespace: 2칸 이상 공백 -> 1칸 변경
    texts = [' '.join(x.split()) for x in texts]
    return texts

# 함수 호출
texts = text_prepro(texts)
print('전처리 후 ')
print(texts)


## 3. 단어 사전 
obj = TfidfVectorizer() # 단어 생성기 
fit = obj.fit(texts)
voca = fit.vocabulary_
print(voca)

# max_features: 최대 단어 개수
max_features=len(voca) # 16


## 4. 희소행렬(sparse matrix) 
sparse_mat = obj.fit_transform(texts)
print(sparse_mat)
'''
  (Doc, Term) 가중치(TFiDF방식)
  (0, 4)	0.4206690600631704
  (0, 2)	0.3393931489111758
  (0, 9)	0.8413381201263408
  (1, 13)	0.5
  (1, 12)	0.5
  (1, 0)	0.5
  (1, 7)	0.5
  (2, 8)	0.6591180018251055
  (2, 1)	0.5317722537280788
  (2, 2)	0.5317722537280788
  (3, 11)	0.40824829046386296
  (3, 3)	0.40824829046386296
  (3, 5)	0.40824829046386296
  (3, 14)	0.40824829046386296
  (3, 10)	0.40824829046386296
  (3, 6)	0.40824829046386296
  (4, 15)	0.7782829228046183
  (4, 1)	0.6279137616509933
  '''

# 만일 최대 단어 개수 10개로 지정하면
max_features10=10

obj10=TfidfVectorizer(max_features=max_features10)
sparse_mat10=obj10.fit_transform(texts)
print(sparse_mat10)
'''
  (0, 4)	0.4206690600631704
  (0, 2)	0.3393931489111758
  (0, 9)	0.8413381201263408
  (1, 0)	0.7071067811865475
  (1, 7)	0.7071067811865475
  (2, 8)	0.6591180018251055
  (2, 1)	0.5317722537280788
  (2, 2)	0.5317722537280788
  (3, 3)	0.5773502691896258
  (3, 5)	0.5773502691896258
  (3, 6)	0.5773502691896258
  (4, 1)	1.0
  '''
# 단어 0~9까지만 결정
sparse_mat10_arr=sparse_mat10.toarray()
print(sparse_mat10_arr)
'''
[[0.         0.         0.33939315 0.         0.42066906 0.
  0.         0.         0.         0.84133812]
 [0.70710678 0.         0.         0.         0.         0.
  0.         0.70710678 0.         0.        ]
 [0.         0.53177225 0.53177225 0.         0.         0.
  0.         0.         0.659118   0.        ]
 [0.         0.         0.         0.57735027 0.         0.57735027
  0.57735027 0.         0.         0.        ]
 [0.         1.         0.         0.         0.         0.
  0.         0.         0.         0.        ]]
'''
sparse_mat10_arr.shape # (5,10) = 5행 10열
