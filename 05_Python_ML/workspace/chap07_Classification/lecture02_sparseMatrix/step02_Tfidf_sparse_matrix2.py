# -*- coding: utf-8 -*-
"""
step02_Tfidf_sparse_matrix.py

<작업 순서>
 1. csv file 가져오기 : temp_spam_data2.csv
 2. texts, target 전처리 
 3. max features -> 최대 단어의 개수
 4. sparse matrix : TFiDF 가중치 
 5. train/test split [추가]
 6. np.save/np.load : 데이터 파일에 저장
"""

import pandas as pd # csv file 
from sklearn.feature_extraction.text import TfidfVectorizer # sparse matrix 

## 1. csv file 가져오기 
path = r"C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML\data"
spam_data = pd.read_csv(path + '/temp_spam_data2.csv',header=None, encoding='utf-8')

print(spam_data.info())
print(spam_data)
'''
         0                                                  1
0      ham  Go until jurong point, crazy.. Available only ...
1      ham                      Ok lar... Joking wif u oni...
2     spam  Free entry in 2 a wkly comp to win FA Cup fina...
3      ham  U dun say so early hor... U c already then say...
4      ham  Nah I don't think he goes to usf, he lives aro...
   ...                                                ...
5569  spam  This is the 2nd time we have tried 2 contact u...
5570   ham                Will  b going to esplanade fr home?
5571   ham  Pity, * was in mood for that. So...any other s...
5572   ham  The guy did some bitching but I acted like i'd...
5573   ham                         Rofl. Its true to its name
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
max_features=len(voca) # 8603


## 4. 희소행렬(sparse matrix) 
sparse_mat = obj.fit_transform(texts)
print(sparse_mat)
'''
  (0, 8091)	0.18581153399604194
  (0, 249)	0.32587667443850526
  (0, 2930)	0.15277917749361952
  (0, 7403)	0.16172136734642226
  :	:
  (5573, 7682)	0.44042919432448746
  (5573, 4790)	0.40096836775091094
  (5573, 3651)	0.5453490184435557
  (5573, 7533)	0.15187824069920672
  '''
  
  
# 만일 최대 단어 개수 5000개로 지정하면
max_features2=5000
obj2=TfidfVectorizer(max_features=max_features2,stop_words='english')
'''
max_features: 최대 단어 길이
stop_words: 불용어 단어 제거
'''
sparse_mat2=obj2.fit_transform(texts)
print(sparse_mat2)
# 단어 0~9까지만 결정
sparse_mat2_arr=sparse_mat2.toarray()
print(sparse_mat2_arr)
sparse_mat2_arr.shape # (5574, 5000)

# target 변수 numpy array 변환
import numpy as np
y=np.array(target)
y # array([0, 0, 1, ..., 0, 0, 0])

# 5. train/test split [추가]
from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(sparse_mat2_arr,y,test_size=0.3,random_state=123)
X_train.shape # (3901, 5000)
X_test.shape # (1673, 5000)

# 6. npy file save [추가]
spam_train_test=(X_train,X_test,y_train,y_test)

# file save
np.save(path+'/spam_train_test.npy',spam_train_test)

# file load
X_train, X_test, y_train, y_test=np.load(path+'\spam_train_test.npy',allow_pickle=True)
# Object arrays cannot be loaded when allow_pickle=False
# -> 피클 형식으로 저장했기 때문에 
# allow_pickle: 피클(이진) 형태로 저장 여부 (기본: False)


