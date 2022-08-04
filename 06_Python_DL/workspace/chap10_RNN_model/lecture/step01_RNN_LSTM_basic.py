# -*- coding: utf-8 -*-
"""
step01_RNN_LSTM_basic.py

RNN model 
 - 순환신경망 모델 

NotImplementedError 오류해결법 : array_ops.py 파일 교체(data 폴더) -> restart 
C:\\Users\컴퓨터이름\anaconda3envs\tensorflow\Lib\site-packages\tensorflow\python\ops
array_ops.py 파일 교체 
"""

import tensorflow as tf # seed value 
import numpy as np # ndarray
from tensorflow.keras import Sequential # model
from tensorflow.keras.layers import SimpleRNN, LSTM, Dense # RNN layer 
# LSTM: 이전 정보에 대한 기억력이 SimpleRNN보다 더 높음

tf.random.set_seed(123) # seed값 지정 

# many-to-one : word(4개) -> 출력(1개)
X = [[[0.0], [0.1], [0.2], [0.3]], 
     [[0.1], [0.2], [0.3], [0.4]],
     [[0.2], [0.3], [0.4], [0.5]],
     [[0.3], [0.4], [0.5], [0.6]],
     [[0.4], [0.5], [0.6], [0.7]],
     [[0.5], [0.6], [0.7], [0.8]]] 

Y = [0.4, 0.5, 0.6, 0.7, 0.8, 0.9] 

X = np.array(X, dtype=np.float32)
X_data=tf.constant(X, dtype=tf.int32)

Y = np.array(Y, dtype=np.float32)
Y_data = tf.constant(Y, dtype=tf.int32)

X.shape # (6, 4, 1) - (batch_size, time_steps, features)
'''
- batch_size: 1회 공급되는 데이터 개수 (6개 문장)
- time_steps: 문장에 포함된 단어의 개수 (4개 단어)
- features: 단어 내 음절의 개수 (1개 음절)
            = 한 time_step (시간 단계)에서 사용되는 차원 개수 (1개 차원)
            = 1개 단어의 길이
'''
Y.shape

input_shape = (4, 1) # (time_steps, features)
# 공급 데이터: 4개 단어, 1음절

model = Sequential() 

# RNN layer 추가 
'''
model.add(SimpleRNN(units=30, input_shape=input_shape, activation='tanh'))
# activation(활성함수): tanh(-1 ~ +1 값으로 정규화)
'''
model.add(LSTM(units=30, input_shape=input_shape, activation='tanh'))

# DNN layer 추가 
model.add(Dense(units=1)) # 출력 : 회귀모델 
# 출력층 활성함수 X -> 회귀모델 의미

# model 학습환경 
model.compile(optimizer='adam', 
              loss='mse', metrics=['mae'])

# model training 
model.fit(X, Y, epochs=100, verbose=1)
'''
1) RNN
Epoch 100/100
1/1 [==============================] - 0s 0s/step
 - loss: 2.0145e-04 - mae: 0.0121
2) LSTM
Epoch 100/100
1/1 [==============================] - 0s 4ms/step
 - loss: 5.1977e-04 - mae: 0.0196
'''

# model prediction
y_pred = model.predict(X)
print(y_pred)
'''
# Y = [0.4, 0.5, 0.6, 0.7, 0.8, 0.9] 
# 1) RNN: Y_pred
[[0.37206325]
 [0.49444115]
 [0.60844016]
 [0.7126006 ]
 [0.8061328 ]
 [0.8888123 ]]
# 2) LSTM: Y_pred
[[0.43407246]
 [0.51645815]
 [0.6017104 ]
 [0.68928045]
 [0.77856946]
 [0.8689499 ]]
'''

