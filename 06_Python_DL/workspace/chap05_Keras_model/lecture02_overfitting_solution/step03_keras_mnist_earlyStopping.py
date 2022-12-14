# -*- coding: utf-8 -*-
"""
step03_keras_mnist_earlyStopping.py

1. Dropout : 무작위 네트워크 삭제 
2. EarlyStopping : loss value에 변화가 없는 경우 학습 조기종료
"""

from tensorflow.keras.datasets.mnist import load_data # MNIST dataset 
from tensorflow.keras.utils import to_categorical # Y변수 : encoding
from tensorflow.keras import Sequential # model 생성
from tensorflow.keras.layers import Dense, Dropout # DNN layer 구축 
from tensorflow.keras.callbacks import EarlyStopping

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
x_train = x_train.reshape(-1, 784)
# 28 * 28 = 784
x_train.shape # (60000, 784)

x_val = x_val.reshape(-1, 784)
x_val.shape # (10000, 784)


# 2) y변수 : one hot encoding 
y_train = to_categorical(y_train) 
y_val = to_categorical(y_val) 


# 3. keras model & layer 구축
model = Sequential()


input_shape = (784,) 

# hidden layer1 : [784, 128] -> [input, output]
model.add(Dense(units=128, input_shape = input_shape, activation = 'relu')) # 1층 
model.add(Dropout(rate = 0.3)) 

# hidden layer2 : [128, 64] -> [input, output]
model.add(Dense(units=64, activation = 'relu')) # 2층 
model.add(Dropout(rate = 0.1)) 

# hidden layer3 : [64, 32] -> [input, output]
model.add(Dense(units=32, activation = 'relu')) # 3층
model.add(Dropout(rate = 0.1)) 

# output layer : [32, 10] -> [input, output]
model.add(Dense(units=10, activation = 'softmax')) # 4층 



# 4. model compile : 학습과정 설정(다항분류기) 
model.compile(optimizer='adam', 
              loss = 'categorical_crossentropy',  
              metrics=['accuracy'])


# 5. model training : train(60,000) vs val(10,000) 
# 조기종료 지정
callback = EarlyStopping(monitor='val_loss',patience=10) # [추가]
'''
- epoch=10 이후 검증 손실(val_loss)이 개선되지 않으면 조기종료 의미
'''
# 모델 생성
model_fit = model.fit(x=x_train, y=y_train, # 훈련셋 
          epochs=30, # 반복학습
          batch_size = 100, # mini batch
          verbose=1, # 출력여부 
          validation_data=(x_val, y_val),
          callbacks=[callback])
'''
1) 조기종료 X
Epoch 30/30
600/600 [==============================] - 1s 2ms/step
 - loss: 0.0467 - accuracy: 0.9857 - val_loss: 0.0804 - val_accuracy: 0.9789
2) 조기종료 O: patience=10
Epoch 30/30
600/600 [==============================] - 2s 3ms/step
 - loss: 0.0467 - accuracy: 0.9857 - val_loss: 0.0804 - val_accuracy: 0.9789
'''


# 6. model evaluation : val dataset 
print('='*30)
print('model evaluation')
model.evaluate(x=x_val, y=y_val)
'''
1) 조기종료 X
313/313 [==============================] - 0s 1ms/step
 - loss: 0.0804 - accuracy: 0.9789
2) 조기종료 O: patience=10
model evaluation
313/313 [==============================] - 0s 1ms/step
 - loss: 0.0804 - accuracy: 0.9789
'''


# 7. model history 
print(model_fit.history.keys())

# loss vs val_loss : overfitting 시작점 : epoch 2
plt.plot(model_fit.history['loss'], 'y', label='train loss')
plt.plot(model_fit.history['val_loss'], 'r', label='val loss')
plt.xlabel('epochs')
plt.ylabel('loss value')
plt.legend(loc='best')
plt.show()
'''
1) 조기종료 X: 약 15 epochs 이상인 경우, 과적합 발생
2) 조기종료 O:
'''


# accuracy vs val_accuracy : : overfitting 시작점 : epoch 2
plt.plot(model_fit.history['accuracy'], 'y', label='train acc')
plt.plot(model_fit.history['val_accuracy'], 'r', label='val acc')
plt.xlabel('epochs')
plt.ylabel('accuracy')
plt.legend(loc='best')
plt.show()

















