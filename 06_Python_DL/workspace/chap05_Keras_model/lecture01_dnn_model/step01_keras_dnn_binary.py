# -*- coding: utf-8 -*-
"""
step01_keras_dnn_binary.py

Keras : DNN model 생성을 위한 고수준 API
 
Keras 이항분류기 
 - X변수 : 스케일링(0~1)
 - y변수 : one hot encoding(binary)
"""

from sklearn.datasets import load_iris # dataset 
from sklearn.model_selection import train_test_split # split 
from sklearn.preprocessing import minmax_scale # x변수 : 스케일링(0~1)

from tensorflow.keras.utils import to_categorical # Y변수 : encoding
from tensorflow.keras import Sequential # model 생성
from tensorflow.keras.layers import Dense # DNN layer 구축 

import tensorflow as tf
import numpy as np 
import random as rd 

################################
### keras 내부 seed 적용 
################################
tf.random.set_seed(123)
np.random.seed(123)
rd.seed(123)


# 1. dataset load & 전처리 
X, y = load_iris(return_X_y=True)

# X변수 : 정규화(0~1)
# 독립변수(X) 값이 너무 큰 경우 문제가 발생할 수 있기 때문에 정규화 필수
X = minmax_scale(X[:100]) 
X.shape # (100, 4)

# y변수 : one hot encoding
y = to_categorical(y[:100]) 
y.shape # (100, 2)
'''
[1., 0.] - class0
[0., 1.] - class1
'''


# 2. 공급 data 생성 : 훈련용, 검증용 
x_train, x_val, y_train, y_val = train_test_split(
    X, y, test_size=0.3, random_state=123)


# 3. keras model & layer 구축 
model = Sequential()


# hidden layer1 : w[4, 8] -> [input, output]
model.add(Dense(units=8, input_shape =(4, ), activation = 'relu')) # 1층 

# hidden layer2 : w[8, 4] -> [input, output]
model.add(Dense(units=4, activation = 'relu')) # 2층 

# output layer : w[4, 2] -> [input, output]
model.add(Dense(units=2, activation = 'sigmoid')) # 3층 

# model layer 확인
model.summary()
'''
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
dense (Dense)                (None, 8)                 40=(4*8)+8
_________________________________________________________________
dense_1 (Dense)              (None, 4)                 36=(8*4)+4        
_________________________________________________________________
dense_2 (Dense)              (None, 2)                 10=(4*2)+2         
=================================================================
Total params: 86
Trainable params: 86
Non-trainable params: 0
_________________________________________________________________
# Param = (input+output)+b
# b = 뉴런의 수
'''


# 4. model compile : 학습과정 설정(이항분류기)
model.compile(optimizer='adam', 
              loss = 'binary_crossentropy',  
              metrics=['accuracy'])
'''
- optimizer: 최적화 알고리즘 (adam, sgd 등)
- loss: 손실함수 (분류: crossentropy, 회귀: mse)
- metrics: 평가방법 (분류: accuracy, 회귀: mae)
'''


# 5. model training : train(70) vs val(30) 
model.fit(x=x_train, y=y_train, # 훈련셋
          epochs=30, # 반복학습
          verbose=1, # 학습과정 출력 유무
          validation_data=(x_val, y_val)) # 검정 데이터
'''
Epoch 29/30
3/3 [==============================] - 0s 15ms/step - loss: 0.6167 - accuracy: 1.0000 - val_loss: 0.6135 - val_accuracy: 1.0000
Epoch 30/30
3/3 [==============================] - 0s 15ms/step - loss: 0.6134 - accuracy: 1.0000 - val_loss: 0.6105 - val_accuracy: 1.0000
'''


# 6. model evaluation : val dataset 
print('='*30)
print('model evaluation')
model.evaluate(x=x_val, y=y_val)
'''
1/1 [==============================] - 0s 2ms/step - loss: 0.6105 - accuracy: 1.0000
'''
# 손실: 0.6, 정확도: 100% 







 