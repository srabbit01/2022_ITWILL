# -*- coding: utf-8 -*-
"""
문) 다음과 같이 Celeb image의 분류기(classifier)를 생성하시오.  
   조건1> train image : train_celeb4
   조건2> validation image : val_celeb4
   조건3> image shape : 120 x 120
   조건4> Image Data Generator 이용 image 자료 생성 
   조건5> model layer 
         1. Convolution layer1 : kernel_size=(4, 4), fmap=32
                                        pool_size=(2, 2)
         2. Convolution layer2 : kernel_size=(4, 4), fmap=64
                                         pool_size=(2, 2)
         3. Flatten layer
         4. DNN hidden layer1 : 64 node
         5. DNN hidden layer2 : 32 node
         6. DNN output layer : 4 node
   조건6> 기타 나머지는 lecture 내용 참고       
"""
from tensorflow.keras import Sequential # keras model 
from tensorflow.keras.layers import Conv2D, MaxPool2D,Activation
from tensorflow.keras.layers import Dense, Flatten, Dropout
from tensorflow.keras.callbacks import EarlyStopping
import os

# seed 적용
import tensorflow as tf
import numpy as np
import random as rd
tf.random.set_seed(123)
np.random.seed(123)
rd.seed(123)

# images dir 
celeb4_path = r'C:/work/Crystal/DataAnalysis/[ITWILL]BigDataAnalysis_ExpertTraining/06_Python_DL/workspace/chap08_Face_detection/celeb4__image'
# train image : train_celeb4
train_dir = os.path.join(celeb4_path,'train_celeb5')
# validation image : val_celeb4
val_dir = os.path.join(celeb4_path,'val_celeb5')

# 1. CNN Model layer 
model = Sequential()

# 1) Convolution layer1 : kernel_size=(4, 4), fmap=32, pool_size=(2, 2)
model.add(Conv2D(32, kernel_size=(4, 4), activation='relu',
                 input_shape=(120,120,3)))
model.add(MaxPool2D(pool_size=(2,2)))
model.add(Dropout(rate=0.1))

# 2) Convolution layer2 : kernel_size=(4, 4), fmap=64, pool_size=(2, 2)
model.add(Conv2D(64,kernel_size=(4, 4), activation='relu'))
model.add(MaxPool2D(pool_size=(2,2)))

# 3) Flatten layer
model.add(Flatten()) 

# 4) DNN hidden layer1 : 64 node
model.add(Dense(64, activation = 'relu'))

# 5) DNN hidden layer2 : 32 node
model.add(Dense(32, activation = 'relu'))

# 6) DNN output layer : 4 node
model.add(Dense(4, activation = 'softmax'))

model.compile(optimizer = 'adam',
              loss = 'categorical_crossentropy', 
              metrics = ['accuracy'])


# 2. image file preprocessing : ImageDataGenerator 이용
# image shape : 120 x 120
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# 훈련셋 이미지 생성
train_data = ImageDataGenerator(rescale=1./255)
train_generator = train_data.flow_from_directory(
        train_dir,
        target_size=(120,120),
        batch_size=20,
        class_mode='categorical')
# 200 * 4 = 8000

# 평가셋 이미지 생성
validation_data = ImageDataGenerator(rescale=1./255)
validation_generator = validation_data.flow_from_directory(
        val_dir,
        target_size=(120,120),
        batch_size=20,
        class_mode='categorical')
# 50 * 4 = 200


# 3. model training : ImageDataGenerator 객체 이용  
callback = EarlyStopping(monitor='val_loss',patience=2)
model_fit = model.fit_generator(
          train_generator,
          steps_per_epoch=40,
          epochs=10, 
          validation_data=validation_generator,
          validation_steps=10,
          callbacks=[callback])
'''
Epoch 10/10
40/40 [==============================] - 11s 282ms/step
 - loss: 0.0028 - accuracy: 1.0000 - val_loss: 0.0011 - val_accuracy: 1.0000
'''

model.summary()
'''
Model: "sequential_1"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d_2 (Conv2D)            (None, 117, 117, 32)      1568      
_________________________________________________________________
max_pooling2d_2 (MaxPooling2 (None, 58, 58, 32)        0         
_________________________________________________________________
dropout_1 (Dropout)          (None, 58, 58, 32)        0         
_________________________________________________________________
conv2d_3 (Conv2D)            (None, 55, 55, 64)        32832     
_________________________________________________________________
max_pooling2d_3 (MaxPooling2 (None, 27, 27, 64)        0         
_________________________________________________________________
flatten_1 (Flatten)          (None, 46656)             0         
_________________________________________________________________
dense_3 (Dense)              (None, 64)                2986048   
_________________________________________________________________
dense_4 (Dense)              (None, 32)                2080      
_________________________________________________________________
dense_5 (Dense)              (None, 4)                 132       
=================================================================
Total params: 3,022,660
Trainable params: 3,022,660
Non-trainable params: 0
_________________________________________________________________
'''

# model evaluation
model.evaluate(validation_generator)
'''
10/10 [==============================] - 1s 52ms/step
 - loss: 0.0011 - accuracy: 1.0000
=> 분류 정확도가 매우 높음을 볼 수 있음
'''


# 4. model history graph
import matplotlib.pyplot as plt
 
print(model_fit.history.keys())

loss = model_fit.history['loss'] # train
acc = model_fit.history['accuracy']
val_loss = model_fit.history['val_loss'] # validation
val_acc = model_fit.history['val_accuracy']


## epoch 과적합 시작점 
epochs = range(1, len(acc) + 1)

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