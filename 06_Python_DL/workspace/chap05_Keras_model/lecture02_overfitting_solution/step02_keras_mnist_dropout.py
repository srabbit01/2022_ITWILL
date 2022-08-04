# -*- coding: utf-8 -*-
"""
step02_keras_mnist_dropout.py

Dropout : 무작위 네트워크 삭제 -> 과적합 최소화 
  - 주의사항: output layer는 적용하지 않음
"""

from tensorflow.keras.datasets.mnist import load_data # MNIST dataset 
from tensorflow.keras.utils import to_categorical # Y변수 : encoding
from tensorflow.keras import Sequential # model 생성
from tensorflow.keras.layers import Dense # DNN layer 구축 
from tensorflow.keras.layers import Dropout
import matplotlib.pyplot as plt # images 

import tensorflow as tf
import numpy as np 
import random as rd 

################################
### keras 내부 seed 적용 
################################
tf.random.set_seed(123)
np.random.seed(123)
rd.seed(123)


# 1. mnist dataset laod 
(x_train, y_train), (x_val, y_val) = load_data() # (images, labels)

x_train.shape # (60000, 28, 28) 
y_train.shape # (60000,)



# 2. x,y변수 전처리 

# 1) x변수 : 정규화 & reshape(3d -> 2d)
x_train = x_train / 255.
x_val = x_val / 255.


# 3d -> 2d : [수정]
x_train = x_train.reshape(-1, 784) # 28 * 28 = 784
x_train.shape # (60000, 784)

x_val = x_val.reshape(-1, 784)


# 2) y변수 : one hot encoding 
y_train = to_categorical(y_train) 
y_val = to_categorical(y_val) 



# 3. keras model & layer 구축
model = Sequential()


input_shape = (784,) 

# hidden layer1 : [784, 128] -> [input, output]
model.add(Dense(units=128, input_shape = input_shape, activation = 'relu')) # 1층 
model.add(Dropout(rate = 0.3)) # [추가] 30% 제거 70% 사용 # rate = 임의 제거 비율

# hidden layer2 : [128, 64] -> [input, output]
model.add(Dense(units=64, activation = 'relu')) # 2층 
model.add(Dropout(rate = 0.1)) # [추가] 10% 제거 90% 사용

# hidden layer3 : [64, 32] -> [input, output]
model.add(Dense(units=32, activation = 'relu')) # 3층
model.add(Dropout(rate = 0.1)) # [추가] 10% 제거 90% 사용

# output layer : [32, 10] -> [input, output]
model.add(Dense(units=10, activation = 'softmax')) # 4층 



# 4. model compile : 학습과정 설정(다항분류기) 
model.compile(optimizer='adam',
              loss = 'categorical_crossentropy',  
              metrics=['accuracy'])


# 5. model training : train(60,000) vs val(10,000)
model_fit = model.fit(x=x_train, y=y_train, # 훈련셋 
          epochs=15, # 반복학습 
          batch_size = 100, # mini batch
          verbose=1, # 출력여부 
          validation_data=(x_val, y_val)) # 검증셋 
'''
Epoch 15/15
600/600 [==============================] - 2s 3ms/step
 - loss: 0.0718 - accuracy: 0.9782 - val_loss: 0.0723 - val_accuracy: 0.9790
'''


# 6. model evaluation : val dataset 
print('='*30)
print('model evaluation')
model.evaluate(x=x_val, y=y_val)
'''
model evaluation
313/313 [==============================] - 1s 2ms/step
 - loss: 0.0723 - accuracy: 0.9790
'''

# 7. model history 
print(model_fit.history.keys())


# loss vs val_loss : 교차점이 15 epochs 정도로 높음 -> 0의 수렴 정도가 비슷
plt.plot(model_fit.history['loss'], 'y', label='train loss')
plt.plot(model_fit.history['val_loss'], 'r', label='val loss')
plt.xlabel('epochs')
plt.ylabel('loss value')
plt.legend(loc='best')
plt.show()


# accuracy vs val_accuracy
plt.plot(model_fit.history['accuracy'], 'y', label='train acc')
plt.plot(model_fit.history['val_accuracy'], 'r', label='val acc')
plt.xlabel('epochs')
plt.ylabel('accuracy')
plt.legend(loc='best')
plt.show()
# epochs size가 증가해도 과적합이 발생되지 않음















