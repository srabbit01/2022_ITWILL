# -*- coding: utf-8 -*-
"""
step03_word_embedding_LSTM.py

 - word Embedding + LSTM 
 
 - chap09: Embedding + DNN -> chap10: Embedding + LSTM + DNN
"""

# texts 처리 
import pandas as pd # csv file
import numpy as np # list -> numpy 
import string # texts 전처리  
from sklearn.model_selection import train_test_split # split
from tensorflow.keras.preprocessing.text import Tokenizer # 토큰 생성기 
from tensorflow.keras.preprocessing.sequence import pad_sequences # [추가] 패딩 

# DNN model 
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, Flatten # [추가] 

# 1. csv file laod 
path = r'C:/work/Crystal/DataAnalysis/[ITWILL]BigDataAnalysis_ExpertTraining/06_Python_DL/data'
spam_data = pd.read_csv(path + '/temp_spam_data2.csv', header = None)


label = spam_data[0] 
texts = spam_data[1]


# 2. texts와 label 전처리

# 1) label 전처리 
label = [1 if lab=='spam' else 0  for lab in label]

# list -> numpy 형변환 
label = np.array(label)

# 2) texts 전처리 
def text_prepro(texts): # [text_sample.txt] 참고 
    # Lower case
    texts = [x.lower() for x in texts]
    # Remove punctuation
    texts = [''.join(c for c in x if c not in string.punctuation) for x in texts]
    # Remove numbers
    texts = [''.join(c for c in x if c not in string.digits) for x in texts]
    # Trim extra whitespace
    texts = [' '.join(x.split()) for x in texts]
    return texts


# 함수 호출 
texts = text_prepro(texts)
print(texts)


# 3. num_words = 4000 제한
tokenizer = Tokenizer(num_words = 4000) #  4000 단어 제한 
# num_words: 단어 사전에서 앞부터 4000개의 단어만 추출 (이외 사용 X)
# 전체 단어 제한은 아니고, 희소행렬에서 열의 개수만 지정하는 것
# Word Embedding에서는 의미 X -> 이는 희소행렬 차원에서만 의미 있음

tokenizer.fit_on_texts(texts = texts) # 텍스트 반영 -> token 생성  

words = tokenizer.index_word # 단어 반환 
print(words)

print('전체 단어 수 =', len(words)) # 전체 단어 수 = 8629

# input_dimension
voc_size = len(words) + 1 # 전체 단어수 + 1(padding) = 8630 



# 4. sequence(정수 색인)
seq_result = tokenizer.texts_to_sequences(texts)
print(seq_result)

lens = [len(sent) for sent in seq_result]
print(lens)

maxlen = max(lens)
maxlen # 158


# 5. padding : maxlen 기준으로 단어 길이 맞춤 
x_data = pad_sequences(seq_result, maxlen = maxlen)
x_data.shape # (5574, 158) -(문장, 단어길이)


# 6. train/test split : 80% vs 20%
x_train, x_val, y_train, y_val = train_test_split(
    x_data, label, test_size=20)

type(x_train) # numpy.ndarray
type(y_train) # list


# 7. DNN model
model = Sequential() # keras model 

# 8. Embedding layer : 1층 
model.add(Embedding(input_dim=voc_size, output_dim=32, input_length=maxlen))
'''
input_dim : 전체단어수 + 1
output_dim : 임베딩 벡터 차원(32~128) 
input_length : 1문장을 구성하는 단어길이 
'''

# 전결합층: 2d -> 1d
# model.add(Flatten())

# [추가] RNN Layer: 순환 신경망
model.add(LSTM(units=32, activation='tanh')) # 2층
# 자체 2차원의 데이터를 1차원으로 평평하게 해주는 기능이 있어, 전결합층 필요 X
          
# hidden layer1 : w[32, 32] 
model.add(Dense(units=32,  activation='relu')) # 3층 

# output layer : [32, 1]
model.add(Dense(units = 1, activation='sigmoid')) # 4층 


# 9. model compile : 학습과정 설정(이항분류기)
model.compile(optimizer='rmsprop', # 'adam' or 'rmsprop' 
              loss = 'binary_crossentropy', #
              metrics=['accuracy'])
# 자연어 분류 시, 대부분 rmsprop 최적화 알고리즘 사용

# 10. model training : train(80) vs val(20) 
model.fit(x=x_train, y=y_train, # 훈련셋 
          epochs=10, # [수정]반복학습 
          batch_size = 512,
          verbose=1, # 출력여부 
          validation_data=(x_val, y_val)) # 검증셋 


# 11. model evaluation : val dataset 
print('='*30)
print('model evaluation')
model.evaluate(x=x_val, y=y_val)
