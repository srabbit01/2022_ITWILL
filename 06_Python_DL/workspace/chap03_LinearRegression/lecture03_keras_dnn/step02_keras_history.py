# -*- coding: utf-8 -*-
"""
step02_keras_history.py

keras history 기능
 - model 학습과정과 검증과정의 손실값 기억하는 기능 
"""

# dataset 
from sklearn.datasets import load_iris # dataset
from sklearn.model_selection import train_test_split # split 
from sklearn.metrics import mean_squared_error, r2_score # 평가 

# keras model 
import tensorflow as tf
from tensorflow.keras import Sequential # keara model 
from tensorflow.keras.layers import Dense # DNN layer 
import numpy as np 
import random as rd 

# tensorflow version
print(tf.__version__) # 2.3.0
# keras version 
print(tf.keras.__version__) # 2.4.0

## karas 내부 weight seed 적용 
tf.random.set_seed(123) # global seed 
np.random.seed(123) # numpy seed
rd.seed(123) # random seed 

# 1. dataset laod 
X, y = load_iris(return_X_y=True)


# 2. 공급 data 생성 : 훈련셋, 검증셋 
x_train, x_val, y_train, y_val = train_test_split(
    X, y, test_size=0.3, random_state=123)


# 3. DNN model 생성 
model = Sequential() # keras model 
print(model) # Sequential object


# 4. DNN model layer 구축 
# hidden layer1 
model.add(Dense(units=12, input_shape=(4,), activation='relu')) # 1층 

# hidden layer2
model.add(Dense(units=6, activation='relu')) # 2층

# output layer 
model.add(Dense(units=1)) # 3층 

# model layer 확인 
print(model.summary())
'''
Model: "sequential_5"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
dense_10 (Dense)             (None, 12)                60        
_________________________________________________________________
dense_11 (Dense)             (None, 6)                 78        
_________________________________________________________________
dense_12 (Dense)             (None, 1)                 7         
=================================================================
Total params: 145
Trainable params: 145
Non-trainable params: 0
_________________________________________________________________
'''

# 5. model compile : 학습과정 설정 
model.compile(optimizer='adam', loss='mse', metrics=['mae'])


# 6. [수정] model training : train(105) vs test(45)
model_fit = model.fit(x=x_train, y=y_train, # 훈련셋 
          epochs=100, # 학습횟수 
          verbose=1,  # 출력여부 
          validation_data=(x_val, y_val)) # 검증셋  
'''
Epoch 99/100
4/4 [==============================] - 0s 6ms/step
 - loss: 0.0406 - mae: 0.1501 - val_loss: 0.0431 - val_mae: 0.1495
Epoch 100/100
4/4 [==============================] - 0s 6ms/step
 - loss: 0.0409 - mae: 0.1513 - val_loss: 0.0395 - val_mae: 0.1436
'''


# 7. model evaluation : validation data 
loss_val, mae = model.evaluate(x_val, y_val)
'''
2/2 [==============================] - 0s 1ms/step - loss: 0.0395 - mae: 0.1436
'''
print('loss value =', loss_val)
# loss value = 0.039474692195653915
print('mae =', mae)
# mae = 0.1435794234275818


# [추가] 8. model history : epoch에 따른 손실값 확인 
print(model_fit.history.keys())
# dict_keys(['loss', 'mae', 'val_loss', 'val_mae'])

# 각각 출력
model_fit.history['loss'] # 훈련셋 손실값
model_fit.history['mae'] # 훈련셋 평가결과
model_fit.history['val_loss'] # 평가셋 손실값
model_fit.history['val_mae'] # 평가셋 평가결과

import matplotlib.pyplot as plt

# model 손실 : loss vs val_loss
plt.plot(model_fit.history['loss'], 'y', label='train loss value')
plt.plot(model_fit.history['val_loss'], 'r', label='val loss value')
plt.xlabel('epochs')
plt.ylabel('loss value')
plt.legend(loc='best')
plt.show()

# model 평가 결과 : mae vs val_mae
plt.plot(model_fit.history['mae'], 'y', label='train mae value')
plt.plot(model_fit.history['val_mae'], 'r', label='val mae value')
plt.xlabel('epochs')
plt.ylabel('mae value')
plt.legend(loc='best')
plt.show()

# 9. model 평가: mean_squared_error, r2_score 

# 1) mean_squared_error
mse = mean_squared_error(y_val,y_pred)
print('MSE =', mse)
# MSE = 0.03947469712946161

# 2) r2_score
r2 = r2_score(y_val,y_pred)
print('r2_score =', r2)
# r2_score = 0.9492145732610167
