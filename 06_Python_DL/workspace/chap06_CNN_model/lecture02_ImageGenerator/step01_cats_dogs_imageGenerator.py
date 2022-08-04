# -*- coding: utf-8 -*-
"""
Cats vs Dogs image classifier 
 - image data generator 이용 : 학습 데이터셋 만들기 
"""
from tensorflow.keras import Sequential # keras model 
from tensorflow.keras.layers import Conv2D, MaxPool2D # Convolution layer
from tensorflow.keras.layers import Dense, Flatten # Affine layer
import os
from sklearn.preprocessing import MinMaxScaler


# image resize
img_h = 150 # height
img_w = 150 # width
input_shape = (img_h, img_w, 3) 

# 1. CNN Model layer 
print('model create')
model = Sequential()

# Convolution layer1 
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu',
                 input_shape = input_shape))
model.add(MaxPool2D(pool_size=(2,2)))

# Convolution layer2 
model.add(Conv2D(64,kernel_size=(3, 3), activation='relu'))
model.add(MaxPool2D(pool_size=(2,2)))

# Convolution layer3 : maxpooling() 제외 
model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
model.add(MaxPool2D(pool_size=(2,2)))

# Flatten layer : 3d -> 1d
model.add(Flatten()) 

# DNN hidden layer(Fully connected layer)
model.add(Dense(256, activation = 'relu'))

# DNN Output layer
model.add(Dense(1, activation = 'sigmoid'))

# model training set  
model.compile(optimizer = 'adam',
              loss = 'binary_crossentropy', 
              metrics = ['accuracy'])


# 2. image file preprocessing : image 생성   
from tensorflow.keras.preprocessing.image import ImageDataGenerator
'''
ImageDataGenerator
- 전처리, 이미지 규격화, 이미지 개수 증식 등
'''
# Cats vs Dogs image: real data (실제 데이터)
# 모든 이미지의 픽셀 크기 다름 -> 이미지 규격화 필요
# Cats or Dogs image 내 noise 존재 -> human(사람)도 보임

# dir setting
base_dir = r"C:/work/Crystal/DataAnalysis/[ITWILL]BigDataAnalysis_ExpertTraining/06_Python_DL/data/images/cats_and_dogs"

train_dir = os.path.join(base_dir, 'train_dir') # 훈련셋 이미지
validation_dir = os.path.join(base_dir, 'validation_dir') # 평가셋 이미지
# os.path.join: 경로 결합

# 훈련셋 이미지 생성기 
train_data = ImageDataGenerator(rescale=1./255) # 정규화 = 1./255

# 평가셋 이미지 생성기
validation_data = ImageDataGenerator(rescale=1./255)

# 훈련셋 이미지 생성
train_generator = train_data.flow_from_directory(
        train_dir, # 훈련셋 이미지 경로
        target_size=(150,150), # (세로, 가로)
        batch_size=20, # 1회 공급 이미지 크기
        class_mode='binary') # 2항 분류

# 평가셋 이미지 생성
validation_generator = validation_data.flow_from_directory(
        validation_dir,
        target_size=(150,150),
        batch_size=20,
        class_mode='binary')


# 3. model training : 생성된 이미지 이용 모델 훈련
model_fit = model.fit_generator(
          train_generator, # 훈련셋 이미지 (2,000)
          steps_per_epoch=100, # batch_size의 step수 = 20*100 = 2,000(1epochs)
          epochs=10, # 2000 * 10 = 20,000
          validation_data=validation_generator, # 평가셋 이미지 (1,000)
          validation_steps=50) # batch_size의 step수  = 20*50 = 1,000(1epochs)
'''
Epoch 10/10
100/100 [==============================] - 54s 543ms/step
 - loss: 0.0965 - accuracy: 0.9650 - val_loss: 1.1951 - val_accuracy: 0.7080
'''

# model evaluation
model.evaluate(validation_generator)
'''
50/50 [==============================] - 8s 167ms/step 
 - loss: 1.1951 - accuracy: 0.7080
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

