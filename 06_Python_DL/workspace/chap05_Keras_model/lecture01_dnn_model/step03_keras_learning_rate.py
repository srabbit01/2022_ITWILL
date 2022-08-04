# -*- coding: utf-8 -*-
"""
step03_keras_learning_rate.py

keras 모델에서 학습률 적용   
 optimizer=Adam(learning_rate = 0.01)
"""

from sklearn.datasets import load_iris # dataset 
from sklearn.model_selection import train_test_split # split 
from sklearn.preprocessing import minmax_scale # x변수 : 스케일링(0~1)
from sklearn.metrics import accuracy_score  # model 평가 

from tensorflow.keras.utils import to_categorical # Y변수 : encoding
from tensorflow.keras import Sequential # model 생성
from tensorflow.keras.layers import Dense # DNN layer 구축 
from tensorflow.keras.models import load_model # model load 

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

X.shape # (150, 4)
y.shape # (150,)


# X변수 : 정규화(0~1)
X = minmax_scale(X) # 

# y변수 : one hot encoding(binary)
y_one = to_categorical(y) # 
print(y_one)
y_one.shape #  (150, 3)
'''
[1, 0, 0] <- 0
[0, 1, 0] <- 1
[0, 0, 1] <- 2
'''

# 2. 공급 data 생성 : 훈련용, 검증용 
x_train, x_val, y_train, y_val = train_test_split(
    X, y_one, test_size=0.3, random_state=123)


# 3. keras model & layer 구축 
model = Sequential()


# hidden layer1 : [4, 12] -> [input, output]
model.add(Dense(units=12, input_shape =(4, ), activation = 'relu')) # 1층 

# hidden layer2 : [12, 6] -> [input, output]
model.add(Dense(units=6, activation = 'relu')) # 2층 

# output layer : [6, 3] -> [input, output]
model.add(Dense(units=3, activation = 'softmax')) # 3층 


# 4. model compile : 학습과정 설정(다항분류기) - [수정]
from tensorflow.keras import optimizers

# optimizers.Adam(learning_rate=0.001)

model.compile(optimizer=optimizers.Adam(learning_rate=0.001), # default=0.001
              loss = 'categorical_crossentropy',  
              metrics=['accuracy'])


# 5. model training : train(70) vs val(30) 
model.fit(x=x_train, y=y_train, # 훈련셋
          epochs=100, # 반복학습
          verbose=1, # 학습과정 출력 유무
          validation_data=(x_val, y_val)) # 검정 데이터
'''
1. learning_rate=0.001
Epoch 100/100
4/4 [==============================] - 0s 10ms/step
 - loss: 0.3877 - accuracy: 0.9619 - val_loss: 0.3624 - val_accuracy: 0.8667
2. learning_rate=0.01
Epoch 100/100
4/4 [==============================] - 0s 7ms/step
 - loss: 0.0427 - accuracy: 0.9905 - val_loss: 0.0711 - val_accuracy: 0.9778 
'''


# 6. model evaluation : val dataset 
print('='*30)
print('model evaluation')
model.evaluate(x=x_val, y=y_val)
'''
2/2 [==============================] - 0s 1ms/step
 - loss: 0.0711 - accuracy: 0.9778
'''