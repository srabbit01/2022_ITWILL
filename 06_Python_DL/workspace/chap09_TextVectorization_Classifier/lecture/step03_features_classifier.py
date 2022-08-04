# -*- coding: utf-8 -*-
"""
step03_features_classifier.py

 - 텍스트 전처리 -> 희소행렬(인코딩) + DNN model 
"""

# texts 처리 
import pandas as pd # csv file
import numpy as np # list -> numpy 
import string # texts 전처리  
from sklearn.model_selection import train_test_split # split
from tensorflow.keras.preprocessing.text import Tokenizer # 토큰 생성기 
import time # time check 

# DNN model 
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense 

# seed값 적용
import tensorflow as tf
import numpy as np
import random as rd
tf.random.set_seed(123)
np.random.seed(123)
rd.seed(123)

# 1. csv file laod 
path = r'C:/work/Crystal/DataAnalysis/[ITWILL]BigDataAnalysis_ExpertTraining/06_Python_DL/workspace/chap09_TextVectorization_Classifier/data'
spam_data = pd.read_csv(path + '/temp_spam_data2.csv', header = None)
spam_data.info()
'''
RangeIndex: 5574 entries, 0 to 5573
Data columns (total 2 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   0       5574 non-null   object
 1   1       5574 non-null   object
dtypes: object(2)
'''

label = spam_data[0] # ham or spam -> 0 or 1 encoding
texts = spam_data[1] # english text -> 희소행렬 encoding


# 2. texts와 label 전처리

# 1) label 전처리 : 0 혹은 1로 변환
label = [1 if lab=='spam' else 0  for lab in label]

# list -> numpy 형변환 
label = np.array(label)
type(label)

# 2) texts 전처리 
def text_prepro(texts): 
    # Lower case: 소문자화
    texts = [x.lower() for x in texts]
    # Remove punctuation: 특수문자 제거
    texts = [''.join(c for c in x if c not in string.punctuation) for x in texts]
    # Remove numbers: 숫자 제거
    texts = [''.join(c for c in x if c not in string.digits) for x in texts]
    # Trim extra whitespace: 공백 제거
    texts = [' '.join(x.split()) for x in texts]
    return texts

# 함수 호출 
texts = text_prepro(texts)
print(texts)


# 3. 토큰 생성기: 4,000개 제한
tokenizer = Tokenizer(num_words=4001) # 전체 단어 이용
# 1차: 전체 단어 이용, 2차: 4000개 제한

tokenizer.fit_on_texts(texts = texts) 

words = tokenizer.index_word 
print(words)

print('전체 단어 수 =', len(words)) 
# 전체 단어 수 = 8629


# 4. Sparse matrix 
x_data = tokenizer.texts_to_matrix(texts=texts, mode='tfidf')
x_data.shape # 1차: (5574, 8630) = (전체문서개수, 전체단어개수+1)
# 2차: (5574, 4001) 전체 단어수 + 1 (Padding)


# 5. train/test split : 80% vs 20%
x_train, x_val, y_train, y_val = train_test_split(
    x_data, label, test_size=20)


# 6. DNN model
model = Sequential() 

# input_shape = (8630, ) # 1차
input_shape = (4001, ) # 2차

# hidden layer1 : w[8630x64]
model.add(Dense(units=64, input_shape=input_shape, activation='relu')) # 1층 

# hidden layer2 : w[63x32]
model.add(Dense(units=32, activation='relu')) # 2층 

# output layer : w[32x1]
model.add(Dense(units = 1, activation='sigmoid')) # 3층 


# 7. model compile : 학습과정 설정(이항분류기)
model.compile(optimizer='adam', 
              loss = 'binary_crossentropy', 
              metrics=['accuracy'])

start = time.time()


# 8. model training : train(80) vs val(20) 
model.fit(x=x_train, y=y_train, # 훈련셋 
          epochs=5, # 반복학습 
          batch_size = 512,
          verbose=1, # 출력여부 
          validation_data=(x_val, y_val)) # 검증셋 
'''
Epoch 5/5
11/11 [==============================] - 0s 27ms/step
 - loss: 0.0234 - accuracy: 0.9977 - val_loss: 0.4014 - val_accuracy: 0.9500
'''
end = time.time()

# 총 모델 생성 시간 확인
tot_time = end - start
print('학습 소요 시간 :', tot_time)
'''
1) num_words=None=8629
  - loss: 0.0234 - accuracy: 0.9977
  - 학습 소요 시간 : 4.1560540199279785 초 
2) num_words=4000
  - loss: 0.0284 - accuracy: 0.9955
  - 학습 소요 시간 : 2.121903657913208 초
=> 두 모델 성능에 큰 차이 X -> 시간 차이 많이 남 (메모리 문제, 비용 문제 등 해결)
'''


# 9. model evaluation : val dataset 
print('='*30)
print('model evaluation')
model.evaluate(x=x_val, y=y_val)
'''
model evaluation
1/1 [==============================] - 0s 3ms/step
 - loss: 0.4014 - accuracy: 0.9500
'''
