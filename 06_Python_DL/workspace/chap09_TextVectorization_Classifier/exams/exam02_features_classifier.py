
"""
 문2) newsgroups 데이터셋을 대상으로 5개 뉴스 그룹만 선택하여 희소행렬을 
     생성한 후 DNN model을 생성하시오.
     조건1> DNN layer
        hidden layer1 : [4000, 126]
        hidden layer2 : [126, 64] 
        hidden layer3 : [64, 32] 
        output layer : [32, 5]
     조건2> 과적합(overfitting)을 고려한 Dropout 적용 
     조건3> model compile 학습환경 :   
           optimizer='rmsprop'
           loss='sparse_categorical_crossentropy',             
           metrics=['sparse_categorical_accuracy']     
     조건4> model training : epochs=10,  batch_size=400
     조건5> model validation : score, accuracy 적용  
"""


from sklearn.datasets import fetch_20newsgroups # news 데이터셋 
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
import time

start_time = time.time() 

# 1. hyper parameters
num_words = 40000 # 40,000개 단어 선정 


# 2. news dataset 가져오기 
newsgroups = fetch_20newsgroups(subset='all') # train/test load 
print(newsgroups.target_names)
print(len(newsgroups.target_names)) # 20개 뉴스 그룹 

# 1) train set : 5개 뉴스 그룹 선택   
cats = list(newsgroups.target_names)[:5]
news_train = fetch_20newsgroups(subset='train',categories=cats)
x_train = np.array(news_train.data) # texts
y_train = np.array(news_train.target) # 0 ~ 4
len(x_train) # 뉴스 text : 2823
y_train # [4, 2, 3, ..., 4, 1, 2] 

# train set sparse matrix 생성 
tokenizer = Tokenizer(num_words = num_words) # 1) 40,000개 선정 
tokenizer.fit_on_texts(x_train) # 2) text 적용 
word_index = tokenizer.word_index 
print('word length : ', len(word_index)) # word length :67576

sparse_train = tokenizer.texts_to_matrix(texts=x_train, mode='tfidf') # 3) 희소행렬
print(sparse_train.shape) # (2823, 40000)


# 2) test set dataset 5개 뉴스그룹 대상 : 희소행렬
news_test = fetch_20newsgroups(subset='test', categories=cats)
x_val = np.array(news_test.data) # texts
y_val = np.array(news_test.target) # 0 ~ 4

# test set sparse matrix 생성
sparse_test = tokenizer.texts_to_matrix(texts=x_val, mode='tfidf') # 3) 희소행렬
print(sparse_test.shape)


model = Sequential()

# 3. <조건1><조건2> model layer 

# hidden layer1 : [40000, 126]
model.add(Dense(units=126, input_shape=(40000, ), activation='relu'))
model.add(Dropout(rate=0.7)) # 고차원

# hidden layer2 : [126, 64] 
model.add(Dense(units=64, activation='relu'))
model.add(Dropout(rate=0.5))

# hidden layer3 : [64, 32] 
model.add(Dense(units=32, activation='relu'))
model.add(Dropout(rate=0.3))

# output layer : [32, 5]
model.add(Dense(units=5, activation='softmax'))

# 4. <조건3><조건4> model 생성과 평가 

# model compile
'''
optimizer='rmsprop'
loss='sparse_categorical_crossentropy',             
metrics=['sparse_categorical_accuracy'] 
'''
model.compile(optimizer='rmsprop', 
              loss = 'sparse_categorical_crossentropy', 
              metrics=['sparse_categorical_accuracy'])
'''
1) optimizer
  - adam
  - rmsprop: 자연어 처리 시 사용하는 optimizer
2) loss
  - categorical_crossentropy: 일반 손실 계산 (y변수 -> one-hot encoding: 2진수 형태)
  - sparse_categorical_crossentropy: 희소행렬 대상 손실 계산
    -> y변수 one-hot encoding하지 X (10진수 형태 -> 단어 사전)
3) metrics
  - accuracy: 일반 손실 계산 (y변수 -> one-hot encoding: 2진수 형태)
  - sparse_categorical_accuracy: 희소행렬 대상 분류 정확도 계산
'''

# model training : epochs=10,  batch_size=400
model.fit(x=sparse_train, y=y_train, # 훈련셋 
          epochs=10, # 반복학습 
          batch_size = 400,
          verbose=1, # 출력여부 
          validation_data=(sparse_test, y_val)) # 검증셋 
'''
Epoch 10/10
8/8 [==============================] - 1s 116ms/step
 - loss: 0.0028 - sparse_categorical_accuracy: 0.9986
 - val_loss: 0.6047 - val_sparse_categorical_accuracy: 0.8345
'''


# 5. <조건5> model 평가 
print('='*30)
print('model evaluation')
model.evaluate(x=sparse_test, y=y_val)
'''
model evaluation
59/59 [==============================] - 0s 7ms/step
 - loss: 0.6047 - sparse_categorical_accuracy: 0.8345''
'''