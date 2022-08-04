# -*- coding: utf-8 -*-
"""
step03_TF_sparse_matrix.py

sparse_matrix 순서
1. csv file 가져오기 
2. texts, target 전처리 
3. max features
4. sparse matrix : TF 가중치 
"""

import string # texts 전처리 
import pandas as pd # csv file 
from sklearn.feature_extraction.text import CountVectorizer # sparse matrix 
'''
CountVectorizer: TF 가중치 (단어의 출현 빈도수)
TfidfVectorizer: Tfidf 가중치 (단어의 출현 빈도수 * 문서의 출현 빈도수 역수)
'''

# 1. csv file 가져오기 
path = r"C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML\data"
spam_data = pd.read_csv(path + '/temp_spam_data.csv',header=None, encoding='utf-8')

print(spam_data.info())
print(spam_data)


# 2. texts, target 전처리

# 1) target 전처리 : dummy변수 
target = spam_data[0]
target # ham=0, spam=1
target = [1 if t == 'spam' else 0 for t in target ]
print(target) # [0, 1, 0, 1, 0]

# 2) texts 전처리 : 공백, 특수문자, 숫자  
texts = spam_data[1]

print('전처리 전')
print(texts)

# texts 전처리 함수 
def text_prepro(texts):
    # Lower case 
    texts = [x.lower() for x in texts]
    # Remove punctuation
    texts = [''.join(c for c in x if c not in string.punctuation) for x in texts]
    # Remove numbers 
    texts = [''.join(c for c in x if c not in string.digits) for x in texts]
    # Trim extra whitespace
    texts = [' '.join(x.split()) for x in texts]
    return texts


texts = text_prepro(texts)
print('전처리 후 ')
print(texts)


# 3. max features : 희소행렬의 열 수(word size)
obj = CountVectorizer() # 단어 생성기 
fit = obj.fit(texts)
voca = fit.vocabulary_ # 단어 사전 
print(voca)

len(voca) # 16
max_features = len(voca) # 전체 단어수 


# 4. sparse matrix : max features 지정 
obj2 = CountVectorizer(max_features = max_features)

# 희소행렬 
sparse_mat = obj2.fit_transform(texts)
print(sparse_mat)
'''
  (0, 9)	2 -> '우리나라'
  (0, 2)	1
  (0, 4)	1
  (1, 7)	1
  (1, 0)	1
  (1, 12)	1
  (1, 13)	1
'''

# numpy array 변환 
sparse_mat_arr = sparse_mat.toarray()

print(sparse_mat_arr)
sparse_mat_arr.shape # TF 방식의 희소행렬 : (5, 16)
''' 
[[0 0 1 0 1 0 0 0 0 2 0 0 0 0 0 0]
 [1 0 0 0 0 0 0 1 0 0 0 0 1 1 0 0]
 [0 1 1 0 0 0 0 0 1 0 0 0 0 0 0 0]
 [0 0 0 1 0 1 1 0 0 0 1 1 0 0 1 0]
 [0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 1]]
'''






