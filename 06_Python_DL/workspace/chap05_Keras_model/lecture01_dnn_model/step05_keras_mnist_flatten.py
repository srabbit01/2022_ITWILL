# -*- coding: utf-8 -*-
"""
step05_keras_mnist_flatten.py

1. Mnist dataset 다항분류기 
2. Full batch vs Mini batch 
3. Flatten layer: 차원을 일치시켜주는 Layer
   = 2d 이미지의 경우, model 내 1d로 만들어야 제대로 학습 가능
   - 즉, input(2d) -> Flatten Layer -> model(1d)
"""

from tensorflow.keras.datasets import mnist # mnist load 
from tensorflow.keras.utils import to_categorical # Y변수 : encoding 
from tensorflow.keras import Sequential # keras model 생성 
from tensorflow.keras.layers import Dense # DNN layer 구축 
from tensorflow.keras.layers import Flatten

################################
## keras 내부 w,b변수 seed 적용 
################################
import tensorflow as tf
import numpy as np 
import random as rd

tf.random.set_seed(123)
np.random.seed(123)
rd.seed(123)


# 1. mnist dataset load 
(x_train, y_train), (x_val, y_val) = mnist.load_data() # (images, labels)

# images : X변수 
x_train.shape # (60000, 28, 28) - (size, h, w) : 2d 제공 
x_val.shape # (10000, 28, 28)

x_train[0] # 0~255
x_train.max() # 255

# labels : y변수 
y_train.shape # (60000,)
y_train[0] # 5


# 2. X,y변수 전처리 

# 1) X변수 : 정규화 & reshape(2d -> 1d)
x_train = x_train / 255. # 정규화 
x_val = x_val / 255.


# 2d 이미지의 경우, 반드시 1차원으로 변형해야 정상적인 학습이 가능
'''
# reshape(2d -> 1d)
x_train = x_train.reshape(-1, 784) # (60000, 28*28)
x_val = x_val.reshape(-1, 784) # (10000, 28*28)
'''


# 2) y변수 : one-hot encoding
y_train = to_categorical(y_train)
y_val = to_categorical(y_val)



# 3. keras model & layer 구축
model = Sequential()

# Flatten Layer: 2d(28,28)를 1d(784)로 평탄화 -> 층수로 포함되지 않음
model.add(Flatten(input_shape=(28,28))) # 보통 2d 또는 3d image 사용
# 2d: input_shape=(28,28)=(가로픽셀,세로픽셀)

# hidden layer1 : w[784, 128]
model.add(Dense(units=128, input_shape=(784), activation='relu'))# 1층 

# hidden layer2 : w[128, 64]
model.add(Dense(units=64, activation='relu'))# 2층 

# hidden layer3 : w[64, 32]
model.add(Dense(units=32, activation='relu'))# 3층

# output layer : w[32, 10]
model.add(Dense(units=10, activation='softmax'))# 4층

#  model layer 확인 
model.summary()
'''
Model: "sequential_10"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
flatten (Flatten)            (None, 784)               0         
_________________________________________________________________
dense_31 (Dense)             (None, 128)               100480    
_________________________________________________________________
dense_32 (Dense)             (None, 64)                8256      
_________________________________________________________________
dense_33 (Dense)             (None, 32)                2080      
_________________________________________________________________
dense_34 (Dense)             (None, 10)                330       
=================================================================
Total params: 111,146
Trainable params: 111,146
Non-trainable params: 0
_________________________________________________________________
'''

# 4. model compile : 학습과정 설정(다항분류기) 
model.compile(optimizer='adam', 
              loss='categorical_crossentropy', 
              metrics=['accuracy'])


# 5. model training : train(70) vs val(30)
model.fit(x=x_train, y=y_train, # 훈련셋 
          epochs=10, # 반복학습 횟수 
          batch_size=100, # 1회 공급data 크기  
          verbose=1, # 출력여부 
          validation_data= (x_val, y_val)) # 검증셋
'''
Epoch 10/10
600/600 [==============================] - 2s 3ms/step
 - loss: 0.0227 - accuracy: 0.9927 - val_loss: 0.0924 - val_accuracy: 0.9752
'''


# 6. model evaluation : val dataset 
print('model evaluation')
model.evaluate(x=x_val, y=y_val)
'''
model evaluation
313/313 [==============================] - 0s 2ms/step
 - loss: 0.0924 - accuracy: 0.9752
'''




