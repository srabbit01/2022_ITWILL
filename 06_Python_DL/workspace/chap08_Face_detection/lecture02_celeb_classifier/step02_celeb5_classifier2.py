# -*- coding: utf-8 -*-
"""
step02_celeb5 image classifier2.py 
 - DroupOut 적용
 - EarlyStopping 적용
 - epoch size 증가
"""
from tensorflow.keras import Sequential # keras model 
from tensorflow.keras.layers import Conv2D, MaxPool2D # Convolution layer
from tensorflow.keras.layers import Dense, Flatten, Dropout # [추가] Affine layer
import os
from tensorflow.keras.callbacks import EarlyStopping # [추가]

import tensorflow as tf
import numpy as np
import random as rd
###########################
### keras 내부 seed 적용
###########################
tf.random.set_seed(123)
np.random.seed(123)
rd.seed(123)

# image resize
img_h = 150 # height
img_w = 150 # width
input_shape = (img_h, img_w, 3) 

# 1. CNN Model layer 
print('model create')
model = Sequential()

# Convolution layer1 : [5,5,3,32] = 32개 특징 생성
model.add(Conv2D(32, kernel_size=(5, 5), activation='relu',
                 input_shape = input_shape))
model.add(MaxPool2D(pool_size=(2,2)))
model.add(Dropout(rate=0.3)) # [추가]

# Convolution layer2 : [3,3,32,64]
model.add(Conv2D(64,kernel_size=(3, 3), activation='relu'))
model.add(MaxPool2D(pool_size=(2,2)))


# Convolution layer3 제외 : 정제된 image
# 이미 전처리 되어 있기 때문에 합성곱층 깊지 않아도 됨

# Flatten layer : 3d(h, w, c) -> 1d(n = h*w*c)
model.add(Flatten()) 

# DNN hidden layer(Fully connected layer): [n, 64]
model.add(Dense(64, activation = 'relu'))

# DNN Output layer
model.add(Dense(5, activation = 'softmax')) # 범주 5 classes (0~4)

# model training set  
model.compile(optimizer = 'adam',
              loss = 'categorical_crossentropy', 
              metrics = ['accuracy'])


# 2. image file preprocessing : image 생성   
from tensorflow.keras.preprocessing.image import ImageDataGenerator
'''
ImageDataGenerator
- 전처리, 이미지 규격화, 이미지 개수 증식 등
'''

# dir setting
base_dir = r"C:/work/Crystal/DataAnalysis/[ITWILL]BigDataAnalysis_ExpertTraining/06_Python_DL/workspace/chap08_Face_detection/celeb5__image"

train_dir = os.path.join(base_dir, 'train_celeb5') # 훈련셋 이미지
validation_dir = os.path.join(base_dir, 'val_celeb5') # 평가셋 이미지
# os.path.join: 경로 결합

# 훈련셋 이미지 생성기 
train_data = ImageDataGenerator(rescale=1./255) # 정규화 = 1./255
# 이미지 증식 필요 없음

# 평가셋 이미지 생성기
validation_data = ImageDataGenerator(rescale=1./255)

# 훈련셋 이미지 생성
# Found 990 images belonging to 5 classes.
train_generator = train_data.flow_from_directory(
        train_dir, # 훈련셋 이미지 경로
        target_size=(150,150), # (세로, 가로)
        batch_size=20, # 1회 공급 이미지 크기
        class_mode='categorical') # 다항 분류

# 평가셋 이미지 생성
# Found 250 images belonging to 5 classes.
validation_generator = validation_data.flow_from_directory(
        validation_dir,
        target_size=(150,150),
        batch_size=20,
        class_mode='categorical') # 다항 분류


# 3. model training : 생성된 이미지 이용 모델 훈련
callback = EarlyStopping(monitor='val_loss',patience=5) # [추가]
model_fit = model.fit_generator(
          train_generator, # 훈련셋 이미지 (990)
          steps_per_epoch=50, # batch_size의 step수 = 99*10 = 990(1epochs)
          epochs=10, # [수정] 1,000 * 10 = 10,000
          validation_data=validation_generator, # 평가셋 이미지 (250)
          validation_steps=13, # batch_size의 step수  = 20*15 = 250(1epochs)
          callbacks=[callback])
# 비슷하나 그 이상의 숫자 기입
'''
Epoch 10/10
50/50 [==============================] - 23s 466ms/step
 - loss: 0.0318 - accuracy: 0.9949 - val_loss: 0.0090 - val_accuracy: 1.0000
'''

model.summary()
'''
Model: "sequential_2"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d_4 (Conv2D)            (None, 146, 146, 32)      2432      
_________________________________________________________________
max_pooling2d_4 (MaxPooling2 (None, 73, 73, 32)        0         
_________________________________________________________________
dropout_2 (Dropout)          (None, 73, 73, 32)        0         
_________________________________________________________________
conv2d_5 (Conv2D)            (None, 71, 71, 64)        18496     
_________________________________________________________________
max_pooling2d_5 (MaxPooling2 (None, 35, 35, 64)        0         
_________________________________________________________________
flatten_2 (Flatten)          (None, 78400)             0         
_________________________________________________________________
dense_6 (Dense)              (None, 64)                5017664   
_________________________________________________________________
dense_7 (Dense)              (None, 5)                 325       
=================================================================
Total params: 5,038,917
Trainable params: 5,038,917
Non-trainable params: 0
_________________________________________________________________
'''

# model evaluation
model.evaluate(validation_generator)
'''
13/13 [==============================] - 1s 95ms/step
 - loss: 0.0090 - accuracy: 1.0000
=> 분류 정확도가 더 향상된 모델 생성
'''

# 4. model history graph
import matplotlib.pyplot as plt
 
print(model_fit.history.keys())

loss = model_fit.history['loss'] # train
acc = model_fit.history['accuracy']
val_loss = model_fit.history['val_loss'] # validation
val_acc = model_fit.history['val_accuracy']


## 3epoch 과적합 시작점 
epochs = range(1, len(acc) + 1) # range(1, 11)

# acc vs val_acc   
plt.plot(epochs, acc, 'b--', label='train acc')
plt.plot(epochs, val_acc, 'r', label='val acc')
plt.title('Training vs validation accuracy')
plt.xlabel('epoch')
plt.ylabel('accuray')
plt.legend(loc='best')
plt.show()

# loss vs val_loss 
plt.plot(epochs, loss, 'b--', label='train loss')
plt.plot(epochs, val_loss, 'r', label='val loss')
plt.title('Training vs validation loss')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend(loc='best')
plt.show()

