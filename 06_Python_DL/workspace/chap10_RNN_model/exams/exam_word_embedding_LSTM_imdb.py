# -*- coding: utf-8 -*-
"""
IMDB 데이터셋 : 25,000개의 영화 리뷰를 대상으로 x변수는 단어 단위 정수 인덱스를 제공하고,
y변수는 1과 0으로 영화 리뷰에 대한 긍정과 부정을 label로 제공하는 감성분석용 데이터셋 


문) 다음과 같은 IMDB 데이터셋을 이용하여 단어 임베딩과 순환신경망으로 분류모형을 만드시오.  
    x_data : 25,000개 영화 review 텍스트에 대한 정수 인덱스
    y_data : 영화review 긍정(1) 또는 부정(0)
    
    
    <조건1> Embedding layer 구성 : 
            input_dim = vocab_size, output_dim = 16차원, input_length = maxlen 
    <조건2> RNN layer : 32개 뉴런을 갖는 순환신경망(LSTM 클래스 이용) 
    <조건3> DNN layer 구성 : 
            hidden layer : 32개 뉴런을 갖는 히든 계층(Dense 클래스 이용) 
            output layer : 1개 뉴런을 갖는 출력 계층(Dense 클래스 이용)  
    <조건4> model compile : 최적화 알고리즘(optimizer = 'rmsprop')
    <조건5> model training : epochs=10, batch_size = 512
    <조건6> model evaluation : 검증용 데이터셋으로 분류모형 검증 
"""

from tensorflow.keras.datasets.imdb import load_data # IMDB dataset 
from tensorflow.keras.preprocessing.sequence import pad_sequences # 패딩
# DNN model 
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, LSTM  

# 가중치의 초기값 고정 
import tensorflow as tf
import numpy as np # list -> numpy 
tf.random.set_seed(123)
np.random.seed(123)

vocab_size = 10000 # 단어집합 10,000개 사용
maxlen = 200 # 1개 문장을 구성하는 단어 길이 

# 1. dataset load : 주요단어 10,000개 사용 
(x_train, y_train), (x_val, y_val) = load_data(num_words = vocab_size)
x_train.shape # (25000,)
y_train.shape # (25000,)

# 첫번째 훈련용 영화 review와 긍정/부정 
print('첫번째 훈련용 리뷰 :', x_train[0]) # 정수인덱스 
print('첫번째 훈련용 리뷰 레이블', y_train[0]) # 1 - 긍정 
'''
첫번째 훈련용 리뷰 : [1, 14, 22, 16, 43, 530, 973, 1622, 1385, 65, 458, 4468, 66, 3941, 4, 173, 36, 256, 5, 25, 100, 43, 838, 112, 50, 670, 22665, 9, 35, 480, 284, 
5, 150, 4, 172, 112, 167, 21631, 336, 385, 39, 4, 172, 4536, 1111, 17, 546, 38, 13, 447, 4, 192, 50, 16, 6, 147, 2025, 19, 14, 22, 4, 1920, 4613, 469, 4, 22, 71, 
87, 12, 16, 43, 530, 38, 76, 15, 13, 1247, 4, 22, 17, 515, 17, 12, 16, 626, 18,19193, 5, 62, 386, 12, 8, 316, 8, 106, 5, 4, 2223, 5244, 16, 480, 66, 3785, 33, 4, 
130, 12, 16, 38, 619, 5, 25, 124, 51, 36, 135, 48, 25, 1415, 33, 6, 22, 12, 215,28, 77, 52, 5, 14, 407, 16, 82, 10311, 8, 4, 107, 117, 5952, 15, 256, 4, 31050, 
7, 3766, 5, 723, 36, 71, 43, 530, 476, 26, 400, 317, 46, 7, 4, 12118, 1029, 13, 104, 88, 4, 381, 15, 297, 98, 32, 2071, 56, 26, 141, 6, 194, 7486, 18, 4, 226, 22, 21, 134, 476, 26, 480, 5, 144, 30, 5535, 18, 51, 36, 28, 224, 92, 25, 104, 4, 226, 65, 16, 38, 1334, 88, 12, 16, 283, 5, 16, 4472, 113, 103, 32, 15, 16, 5345, 19, 178, 32]
첫번째 훈련용 리뷰 레이블 : 1
'''

# 검증용 영화 review와 긍정/부정 
x_val.shape # (25000,)
y_val.shape # (25000,)



# 2. padding : 리뷰 최대 단어 길이 200개로 제한하여 패딩 진행 
x_train = pad_sequences(x_train, maxlen=maxlen) # 단어길이 = 200
x_val = pad_sequences(x_val, maxlen=maxlen) # 단어길이 = 200


model = Sequential() # keras 모델 생성 


# 3. Embedding layer : 1층 - 인코딩 수행 


# 4.순환신경망(RNN layer) 추가


# 5. DNN layer 
    

# 6. model compile : 학습과정 설정(이항분류기)
model.compile()



# 7. model training  
model.fit() 



# 8. model evaluation : val dataset 
print('='*30)
print('model evaluation')




