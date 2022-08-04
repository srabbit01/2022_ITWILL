# -*- coding: utf-8 -*-
"""
step03_keras_cnn_cifar10.py

CNN model 생성 
 1. image dataset load 
 2. image dataset 전처리 
 3. CNN model 생성  
 4. CNN model 평가
 5. CMM model history 
"""
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from tensorflow.keras.datasets.cifar10 import load_data # color image dataset 
from tensorflow.keras.utils import to_categorical # one-hot encoding 
from tensorflow.keras import Sequential # model 생성 
from tensorflow.keras.layers import Conv2D, MaxPool2D # Conv layer 
from tensorflow.keras.layers import Dense, Flatten # DNN layer 
import matplotlib.pyplot as plt 

# 1. image dataset load 
(x_train, y_train), (x_val, y_val) = load_data()

x_train.shape # image : (50000, 32, 32, 3) - (size, h, w, c)
y_train.shape # label : (50000, 1)


x_val.shape # image : (10000, 32, 32, 3)
y_val.shape # label : (10000, 1)


# 2. image dataset 전처리

# 1) image pixel 실수형 변환 : 자료형 맞추기
x_train = x_train.astype(dtype ='float32')  # Weight와 Bias가 'float32'기에
x_val = x_val.astype(dtype ='float32')

# 2) image 정규화 : 0~1
x_train = x_train / 255
x_val = x_val / 255
print(x_train)


# 3) label 전처리 : 10진수 -> one hot encoding(2진수) 
y_train = to_categorical(y_train, num_classes=10)
y_val = to_categorical(y_val, num_classes=10)
# num_classes=10:


# 3. CNN model & layer 구축 
input_shape = (32, 32, 3) # input images : 이미지 모양 입력
# = (세로, 가로, 색상수) # 색상 개수 = 1(흑백)/3(컬러)

# 1) model 생성 
model = Sequential()

# 2) layer 구축 
# [1층] Conv layer1 : Conv2d -> relu -> MaxPool2d
# filter[5,5,3,32]
model.add(Conv2D(filters=32, kernel_size=(5,5), 
                 input_shape = input_shape, activation='relu')) # image[28x28]
'''
- filters: 특징 이미지 개수 (추출할 특징 맵의 개수)
- kernel_size: 필터의 크기
- input_shape: 대상 이미지 모양
- activation: 활성함수 = 'relu'
'''
model.add(MaxPool2D(pool_size=(3,3), strides=(2,2))) # image[13x13]
'''
- pool_size: 윈도우 크기
- strides: 윈도우 이동
'''

# [2층] Conv layer2 : Conv2d -> relu -> MaxPool2d
model.add(Conv2D(filters=64, kernel_size=(5,5), activation='relu')) # image[9x9]
model.add(MaxPool2D(pool_size=(3,3), strides=(2,2))) # image[4x4]

# [3층] Conv layer3  : Conv2d -> relu
model.add(Conv2D(filters=128, kernel_size=(3,3), activation='relu'))# image[2x2]


# 전결합층 : Flatten layer : 3d or 2d -> 1d
model.add(Flatten())
'''
3d [h,w,c] -> 1d[n=h*w*c]
'''

# [4층] DNN1 : hidden layer : w[n, 64]
model.add(Dense(units=64, activation='relu'))

# [5층] DNN2 : output layer : w[63, 10]
model.add(Dense(units = 10, activation='softmax'))
                  

# 4. model compile : 학습과정 설정(다항분류기) 
model.compile(optimizer='adam', 
              loss = 'categorical_crossentropy',  
              metrics=['accuracy']) # 평가 방법: 분류 정확도
import time
start=time.time()
# 5. model training : train(105) vs val(45) 
model_fit = model.fit(x=x_train, y=y_train, # 훈련셋 
          epochs=10, # 반복학습 (50,000*10=500,000)
          batch_size = 100, # mini batch: 1회 공급 image size (1epoch=100*500) 
          verbose=1, # 출력여부 
          validation_data=(x_val, y_val)) # 검증셋 
'''
Epoch 10/10
500/500 [==============================] - 40s 80ms/step
 - loss: 0.7781 - accuracy: 0.7284 - val_loss: 0.9959 - val_accuracy: 0.6650
'''
# 상대적으로 정확도가 매우 높지 않음을 알 수 있음
# 이미지에 노이즈가 많은 경우, 분류 정확도 높지 않을 수 있음
# 이미지가 뚜렷한 경우 분류 정확도 높음
end=time.time()
print('총 소요시간 :', end-start)
# 총 소요시간 : 472.7871947288513

model.summary()
'''
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d (Conv2D)              (None, 28, 28, 32)        2432      [1층]
_________________________________________________________________
max_pooling2d (MaxPooling2D) (None, 13, 13, 32)        0         
_________________________________________________________________
conv2d_1 (Conv2D)            (None, 9, 9, 64)          51264     [2층]
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 4, 4, 64)          0         
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 2, 2, 128)         73856     [3층]
_________________________________________________________________
flatten (Flatten)            (None, 512)               0         
_________________________________________________________________
dense (Dense)                (None, 64)                32832     [4층]
_________________________________________________________________
dense_1 (Dense)              (None, 10)                650       [5층]
=================================================================
Total params: 161,034
Trainable params: 161,034
Non-trainable params: 0
_________________________________________________________________
'''


# 6. CNN model 평가 : val dataset 
print('='*30)
print('model evaluation')
model.evaluate(x=x_val, y=y_val)
'''
model evaluation
313/313 [==============================] - 2s 8ms/step
 - loss: 0.9959 - accuracy: 0.6650
'''

 
# 7. CMM model history 
print(model_fit.history.keys()) # key 확인 
# dict_keys(['loss', 'accuracy', 'val_loss', 'val_accuracy'])

# loss vs val_loss 
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


# 8. test data 예측
import tensorflow as tf
y_prob=model.predict(x_val)
y_pred=tf.argmax(y_prob,axis=1)
y_val2=tf.argmax(y_val,axis=1)






