# -*- coding: utf-8 -*-
"""
step02_keras_dnn_category.py

keras 다항분류기 
 - X변수 : 스케일링(0~1)
 - y변수 : one hot encoding(binary)
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
X = minmax_scale(X) 

# y변수 : one hot encoding
y = to_categorical(y) 


# 2. 공급 data 생성 : 훈련용, 검증용 
x_train, x_val, y_train, y_val = train_test_split(
    X, y, test_size=0.3, random_state=123)


# 3. keras model & layer 구축
model = Sequential()

# hidden layer1 : [4, 12] -> [input, output]
model.add(Dense(units=12, input_shape =(4, ), activation = 'relu')) # 1층 

# hidden layer2 : [12, 6] -> [input, output]
model.add(Dense(units=6, activation = 'relu')) # 2층 

# output layer : [6, 3] -> [input, output]
model.add(Dense(units=3, activation = 'softmax')) # 3층 : [수정]

# model layer 확인
model.summary()
'''
Model: "sequential_3"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
dense_9 (Dense)              (None, 12)                60        
_________________________________________________________________
dense_10 (Dense)             (None, 6)                 78        
_________________________________________________________________
dense_11 (Dense)             (None, 3)                 21        
=================================================================
Total params: 159
Trainable params: 159
Non-trainable params: 0
_________________________________________________________________
'''


# 4. model compile : 학습과정 설정(다항분류기)
model.compile(optimizer='adam', 
              loss = 'categorical_crossentropy',  # [수정]
              metrics=['accuracy'])


# 5. model training : train(70) vs val(30) 
model.fit(x=x_train, y=y_train, # 훈련셋
          epochs=100, # 반복학습
          verbose=1, # 학습과정 출력 유무
          validation_data=(x_val, y_val)) # 검정 데이터
'''
Epoch 100/100
4/4 [==============================] - 0s 8ms/step
 - loss: 0.3877 - accuracy: 0.9619 - val_loss: 0.3624 - val_accuracy: 0.8667
'''


# 6. model evaluation : val dataset 
print('='*30)
print('model evaluation')
model.evaluate(x=x_val, y=y_val)
'''
model evaluation
2/2 [==============================] - 0s 2ms/step
 - loss: 0.3624 - accuracy: 0.8667
'''


# 7. save model & load model: hdrf 파일 형식으로 저장

# 1) save
path=r'C:/work/Crystal/DataAnalysis/[ITWILL]BigDataAnalysis_ExpertTraining/06_Python_DL/workspace/chap05_Keras_model/model'
model.save(path+'/keras_model_iris.h5')

# 2) load
my_model = load_model(path+'/keras_model_iris.h5')


# 8. new data & predict
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.5, random_state=123)

# predict
y_pred = my_model.predict(x_test) # new dataset
print(y_pred) # 확률 예측치

y_test # one-hot encoding

# 관측치 및 예측치 -> 10진수 변환
y_pred = tf.argmax(y_pred, axis=1) # 행 단위 색인(위치) 반환
y_test = tf.argmax(y_test, axis=1)

# 분류 정확도 확인
acc = accuracy_score(y_test, y_pred)
print('accuracy =', acc)
# accuracy = 0.8933333333333333