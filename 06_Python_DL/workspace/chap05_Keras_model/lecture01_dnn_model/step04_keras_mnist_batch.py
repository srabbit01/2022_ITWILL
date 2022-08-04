# -*- coding: utf-8 -*-
"""
step04_keras_mnist_batch.py

1. Mnist dataset 다항분류기 
2. Full batch vs Mini batch 
   - Full batch: 전체 훈련 데이터 공급
   - Mini batch: 훈련 데이터 분할 공급 (데이터 크기가 큰 경우)
"""

from tensorflow.keras.datasets import mnist # mnist load 
from tensorflow.keras.utils import to_categorical # Y변수 : encoding 
from tensorflow.keras import Sequential # keras model 생성 
from tensorflow.keras.layers import Dense # DNN layer 구축 
import matplotlib.pyplot as plt
import time # 기본 모듈

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

# image 출력
plt.imshow(X=x_train[0])
plt.show()

# labels : y변수 
y_train.shape # (60000,)
y_train[0] # 5


# 2. X,y변수 전처리 

# 1) X변수 : 정규화 & reshape(2d -> 1d)
# 정규화
x_train = x_train / 255. # 정규화 
x_val = x_val / 255.

# reshape(2d -> 1d) -> 이미지 1차원화 (2차원의 경우, 추가되는 층이 필요하기에)
x_train = x_train.reshape(-1, 784) # (60000, 28*28)
x_val = x_val.reshape(-1, 784) # (10000, 28*28)

# 2) y변수 : class(10진수) -> one-hot encoding(2진수)
y_train = to_categorical(y_train)
y_val = to_categorical(y_val)


# 3. keras model & layer 구축
start=time.time() # 소요시간 확인
model = Sequential()


# hidden layer1 : w[784, 128]
model.add(Dense(units=128, input_shape=(784,), activation='relu'))# 1층 

# hidden layer2 : w[128, 64]
model.add(Dense(units=64, activation='relu'))# 2층 

# hidden layer3 : w[64, 32]
model.add(Dense(units=32, activation='relu'))# 3층

# output layer : w[32, 10]
model.add(Dense(units=10, activation='softmax'))# 4층

#  model layer 확인 
model.summary()
'''
Model: "sequential_6"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
dense_15 (Dense)             (None, 128)               100480    
_________________________________________________________________
dense_16 (Dense)             (None, 64)                8256      
_________________________________________________________________
dense_17 (Dense)             (None, 32)                2080      
_________________________________________________________________
dense_18 (Dense)             (None, 10)                330       
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
          # batch_size=100, # 1회 공급 데이터 크기 (100) -> 총 600번 반복 = 1epoch
          epochs=10, # 반복학습 횟수 -> 60,000*10=600,000 : Full Batch
          verbose=1, # 출력여부 
          validation_data= (x_val, y_val)) # 검증셋 (10,000)
end=time.time() # 종료시간
'''
Epoch 10/10
1875/1875 [==============================] - 5s 3ms/step
 - loss: 0.0236 - accuracy: 0.9919 - val_loss: 0.1054 - val_accuracy: 0.9740
'''


# 6. model evaluation : val dataset 
print('model evaluation')
model.evaluate(x=x_val, y=y_val)
'''
model evaluation
313/313 [==============================] - 1s 2ms/step
 - loss: 0.1054 - accuracy: 0.9740
'''


# 시작과 종료시간 확인
print(f'시작시간: {start}, 종료시간: {end}')
print('총 소요시간: ',end - start)

# 결론
# 1. Full Batch
'''
시작시간: 1653634059.7455013, 종료시간: 1653634093.0194125
총 소요시간:  33.273911237716675
- loss: 0.1054 - accuracy: 0.9740
'''
# 2. Mini Batch: batch_size=100
'''
시작시간: 1653634233.111786, 종료시간: 1653634249.0594788
총 소요시간:  15.94769287109375
- loss: 0.0924 - accuracy: 0.9752
'''
# 따라서, Mini Batch의 소요시간이 매우 짧으며, 정확도도 매우 좋음
