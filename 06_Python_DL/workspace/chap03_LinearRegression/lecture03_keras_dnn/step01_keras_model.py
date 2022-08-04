# -*- coding: utf-8 -*-
"""
step01_keras_model.py

High Level API - Keras

# High Level API: 사용자 중심 API 
  -> 사용자가 비교적 쉽게 개발(작성) 가능
# Low Level API: 기계 중심 API (기계어 중심) 
  -> 해석에 어려움이 있으나, 실행 속도 매우 빠름
"""

# dataset 
from sklearn.datasets import load_iris # dataset
from sklearn.model_selection import train_test_split # split 
from sklearn.metrics import mean_squared_error, r2_score # 평가 

# keras model 
import tensorflow as tf
from tensorflow.keras import Sequential # kearas model (객체 생성)
from tensorflow.keras.layers import Dense # DNN Hidden layer 
import numpy as np 
import random 


## karas 내부 weight seed 적용 
tf.random.set_seed(123) # global seed 
np.random.seed(123) # numpy seed
random.seed(123) # random seed 


# 1. dataset laod 
X, y = load_iris(return_X_y=True)


# 2. 공급 data 생성 : 훈련셋, 검증셋 
x_train, x_val, y_train, y_val = train_test_split(
    X, y, test_size=0.3, random_state=123)


# 3. DNN model 생성 
model = Sequential() # kearas model


# 4. DNN model layer 구축 
help(Dense)
########################################
## hidden layer: 2개, unit=12 > unit=6
########################################
# w, b 변수: keras에서 자동 생성
# model.add(Dense(units=뉴런수, [input_shape=(입력수,)], [activation='활성함수']))

# hidden layer1: w[4, 12] = input(4), output(12)
'''
units = 뉴런 수 (12), input_shape = 입력 수, activation = 활성함수
'''
model.add(Dense(units=12, input_shape=(4,), activation='relu'))# 1층 

# hidden layer2: w[12, 6] = input(12), output(6)
'''
units = 뉴런 수 (6), activation = 활성함수
'''
model.add(Dense(units=6, activation='relu'))# 2층

# output layer = 출력층 : w[6, 1] = input(6), output(1) 
'''
units = 뉴런 수 (1)
'''
model.add(Dense(units=1))# 3층 

# model layer 확인
dir(model)
'''
predict: 예측치 출력
add: layer 생성
compile: 학습환경 생성
fit: 모델 생성
history: epoch에 따른 손실
summary(): 모델 생성 요약본
'''
model.history
model.summary()
'''
Model: "sequential_2"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
dense_1 (Dense)              (None, 12)                60         -> 1번째 은닉층
_________________________________________________________________
dense_2 (Dense)              (None, 6)                 78         -> 2번째 은닉층
_________________________________________________________________
dense_3 (Dense)              (None, 1)                 7          -> 출력층
=================================================================
Total params: 145
Trainable params: 145
Non-trainable params: 0
_________________________________________________________________
# Param: 네트워크 개수 = (입력 수 * 출력 수) + bias(편향)=뉴런의수
  - 60 = 4 * 12 + 12
  - 78 = 12 * 6 + 6
  - 7 = 6 * 1 + 1
'''

# 5. model compile : 학습과정 설정 
'''
- optimizer: 최적화 알고리즘 (adam, agd)
- loss: 손실 함수 (mse)
- metrics: 모델 평가 방법 (mae, mse, rmse)
'''
model.compile(optimizer='adam', loss='mse', metrics=['mae'])


# 6. model training 
help(model.compile)
model.fit(x=x_train, y=y_train, # 훈련 데이터
          epochs=100, # 반복 학습 횟수
          verbose=1,  # 콘솔 출력 여부
          validation_data=(x_val, y_val)) # 평가 데이터   
'''
Epoch 99/100
4/4 [==============================] - 0s 14ms/step 
 - loss: 0.0406 - mae: 0.1501 - val_loss: 0.0431 - val_mae: 0.1495
Epoch 100/100
4/4 [==============================] - 0s 15ms/step
 - loss: 0.0409 - mae: 0.1513 - val_loss: 0.0395 - val_mae: 0.1436
-> 훈련 데이터 손실 및 평가 결과 - 평가 데이터 손실 및 평가 결과
=> 100 번 완료
'''

# 7. model evaluation(검증)
# 모델 검증 도구: model.evaluate()
print('\nmodel evaluation')
model.evaluate(x_val, y_val, verbose=1)
'''
model evaluation
1/2 [==============>...............] 
 - ETA: 0s - loss: 0.0489 - mae: 0.1582
2/2 [==============================] 
 - 0s 997us/step - loss: 0.0395 - mae: 0.1436
=> 손실 및 평가 결과 확인하기
'''

# 8. model 예측
y_pred = model.predict(x_val)

# 9. model 평가: mean_squared_error, r2_score 

# 1) mean_squared_error
mse = mean_squared_error(y_val,y_pred)
print('MSE =', mse)
# MSE = 0.03947469712946161

# 2) r2_score
r2 = r2_score(y_val,y_pred)
print('r2_score =', r2)
# r2_score = 0.9492145732610167

# 3) 훈련 결과 및 평가 결과 비교
import matplotlib.pyplot as plt
plt.plot(x_val,y_val,'y--')
plt.plot(x_val,y_pred,'g-')
plt.show()