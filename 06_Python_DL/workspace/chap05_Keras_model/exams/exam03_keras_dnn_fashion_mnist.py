# -*- coding: utf-8 -*-
"""
문3) fashion_mnist 데이터셋을 이용하여 다음과 같이 keras 모델을 생성하시오.
    
  조건1> keras layer
       L1 =  (28, 28) x 128
       L2 =  128 x 64
       L3 =  64 x 32
       L4 =  32 x 16
       L5 =  16 x 10
  조건2> output layer 활성함수 : softmax     
  조건3> optimizer = 'Adam',
  조건4> loss = 'categorical_crossentropy'
  조건5> metrics = 'accuracy'
  조건6> epochs = 15, batch_size = 32   
  조건7> model evaluation : validation dataset
"""
from tensorflow.keras.utils import to_categorical # one hot
from tensorflow.keras.datasets import fashion_mnist # fashion
from tensorflow.keras import Sequential # keras model 
from tensorflow.keras.layers import Dense, Flatten # model layer
import matplotlib.pyplot as plt
from tensorflow.keras.layers import Dropout
from tensorflow.keras.callbacks import EarlyStopping

# 1. MNIST dataset loading
(train_img, train_lab),(val_img, val_lab)=fashion_mnist.load_data() # (images, labels)
train_img.shape # (60000, 28, 28) 
train_lab.shape # (60000,) 
 


# 2. x, y변수 전처리 
# x변수 : 정규화(0~1)
train_img = train_img / 255.
val_img = val_img / 255.
train_img[0] # first image(0~1)
val_img[0] # first image(0~1)


# y변수 : one hot encoding 
train_lab = to_categorical(train_lab)
val_lab = to_categorical(val_lab)
val_lab.shape # (10000, 10)

# 입력 : 28x28
# 출력 : 10개 


# 3. keras model
model = Sequential() 


# 4. DNN model layer 구축 
model.add(Flatten(input_shape=(28,28)))

# L1 =  (28, 28) x 128
model.add(Dense(units=128, input_shape=(784,), activation='relu'))
model.add(Dropout(rate=0.3))

# L2 =  128 x 64
model.add(Dense(units=64, activation='relu'))
model.add(Dropout(rate=0.1))

# L3 =  64 x 32
model.add(Dense(units=32, activation='relu'))
model.add(Dropout(rate=0.1))

# L4 =  32 x 16
model.add(Dense(units=16, activation='relu'))
model.add(Dropout(rate=0.1))

# L5 =  16 x 10
model.add(Dense(units=10, activation='softmax'))


# 5. model training 

# model compile : 학습과정 설정(다항분류기) 
model.compile(optimizer='adam', 
              loss='categorical_crossentropy', 
              metrics=['accuracy'])

# model early stopping
early_stop=EarlyStopping(monitor='val_loss',patience=2)

# model training : train(70) vs val(30)
model_fit=model.fit(x=train_img, y=train_lab, # 훈련셋 
                    epochs=15, # 반복학습 횟수: 60,000 * 15 = 900,000
                    batch_size=32, # 1회 공급data 크기 = 32 images 
                    verbose=1, # 출력여부 
                    validation_data= (val_img, val_lab),
                    callbacks=[early_stop]) # 검증셋
'''
1) No Early Stopping: Epochs 15
Epoch 15/15
1875/1875 [==============================] - 3s 2ms/step
 - loss: 0.3490 - accuracy: 0.8754 - val_loss: 0.3558 - val_accuracy: 0.8747
2) Early Stopping: patience 2 -> Epochs 15
Epoch 15/15
1875/1875 [==============================] - 3s 2ms/step
 - loss: 0.3499 - accuracy: 0.8747 - val_loss: 0.3716 - val_accuracy: 0.8729
'''


# 6. model evaluation : validation dataset
print('model evaluation')
model.evaluate(x=val_img, y=val_lab)
'''
1) No Early Stopping: Epochs 15
model evaluation
313/313 [==============================] - 0s 873us/step
 - loss: 0.3558 - accuracy: 0.8747
2) Early Stopping: patience 2 -> Epochs 15
model evaluation
313/313 [==============================] - 0s 1ms/step
 - loss: 0.3716 - accuracy: 0.8729
'''


# 7. model history : train vs val -> overfitting 시작점 확인
print(model_fit.history.keys())
# dict_keys(['loss', 'accuracy', 'val_loss', 'val_accuracy'])

# loss vs val_loss : overfitting 시작점 : 10 epochs
plt.plot(model_fit.history['loss'], 'y', label='train loss')
plt.plot(model_fit.history['val_loss'], 'r', label='val loss')
plt.xlabel('epochs')
plt.ylabel('loss value')
plt.legend(loc='best')
plt.show()

# accuracy vs val_accuracy : : overfitting 시작점 : 10 epochs
plt.plot(model_fit.history['accuracy'], 'y', label='train acc')
plt.plot(model_fit.history['val_accuracy'], 'r', label='val acc')
plt.xlabel('epochs')
plt.ylabel('accuracy')
plt.legend(loc='best')
plt.show()