# -*- coding: utf-8 -*-
"""
step04_word_embedding.py
 - word embedding(인코딩) + DNN model

 1. encoding 유형 
    1) 희소행렬 
       texts -> 희소행렬 -> DNN model(label 분류)
    2) 단어 임베딩(Embedding)
       texts -> [sequence(정수 색인) -> 패딩 -> Embedding(사상)] -> DNN model(label 분류)
 2. Embedding(input_dim, output_dim, input_length)층
"""

# texts 처리 
import pandas as pd # csv file
import numpy as np # list -> numpy 
import string # texts 전처리  
from sklearn.model_selection import train_test_split # split
from tensorflow.keras.preprocessing.text import Tokenizer # 토큰 생성기 
from tensorflow.keras.preprocessing.sequence import pad_sequences # [추가] 패딩 

# DNN model 
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, Flatten # [추가] 

# 1. csv file laod 
path = r'C:/work/Crystal/DataAnalysis/[ITWILL]BigDataAnalysis_ExpertTraining/06_Python_DL/workspace/chap09_TextVectorization_Classifier/data'
spam_data = pd.read_csv(path + '/temp_spam_data2.csv', header = None)


label = spam_data[0] 
texts = spam_data[1]

# 2. texts와 label 전처리

# 1) label 전처리 
label = [1 if lab=='spam' else 0  for lab in label]

# list -> numpy 형변환 
label = np.array(label)

# 2) texts 전처리 
def text_prepro(texts): # [text_sample.txt] 참고 
    # Lower case
    texts = [x.lower() for x in texts]
    # Remove punctuation
    texts = [''.join(c for c in x if c not in string.punctuation) for x in texts]
    # Remove numbers
    texts = [''.join(c for c in x if c not in string.digits) for x in texts]
    # Trim extra whitespace
    texts = [' '.join(x.split()) for x in texts]
    return texts


# 함수 호출 
texts = text_prepro(texts)
print(texts)


# 3. num_words = 4000 제한
tokenizer = Tokenizer(num_words = 4000) # 4000 단어 제한 

tokenizer.fit_on_texts(texts = texts) # 텍스트 반영 -> token 생성  

words = tokenizer.index_word # 단어 반환 
print(words)

print('전체 단어 수 =', len(words)) # 전체 단어 수 
# 전체 단어 수 = 8629


# 4. [추가] sequence(정수 색인) -> padding(패딩)

# 1) sequence(정수 색인): 단어 순번
seq_vector = tokenizer.texts_to_sequences(texts)
print(seq_vector)

# 2) padding: maxlen 기준, 단어 길이 맞춤
# 최대 길이 확인
max_sent = max([len(sent) for sent in seq_vector]) # 158
# 패딩
x_data = pad_sequences(seq_vector,maxlen=max_sent)
x_data.shape # (5574, 158) = (문장 수, 문장 내 단어 수)


# 5. train/test split : 80% vs 20%
x_train, x_val, y_train, y_val = train_test_split(
    x_data, label, test_size=20)

type(x_train) # numpy.ndarray
type(y_train) # list


# 6. DNN model
model = Sequential() # keras model 

# 1) [추가] Embedding Layer: 2d
voca_size = len(words)+1
model.add(Embedding(input_dim=voca_size,output_dim=32,
                    input_length=max_sent)) # 1층 
'''
- vocab_size: 전체 단어 개수 + 1(padding)
- embedding_dim: 사용자 지정 임베딩 차원
- max_length: 입력되는 문장 내 단어의 길이
'''

# 2) [추가] Flatten Layer(전결합층): 2d -> 1d
model.add(Flatten())

# 3) Hidden & Output Layer

# hidden layer1 : 1d
# model.add(Dense(units=64, activation='relu'))

# hedden layer2 
model.add(Dense(units=32, activation='relu')) # 2층 

# output layer
model.add(Dense(units = 1, activation='sigmoid')) # 3층 
          

# 7. model compile : 학습과정 설정(이항분류기)
model.compile(optimizer='adam', 
              loss = 'binary_crossentropy',
              metrics=['accuracy'])


# 8. model training : train(80) vs val(20) 
model.fit(x=x_train, y=y_train, # 훈련셋 
          epochs=10, # [수정] 반복학습 
          batch_size = 512,
          verbose=1, # 출력여부 
          validation_data=(x_val, y_val)) # 검증셋 
'''
Epoch 10/10
11/11 [==============================] - 0s 36ms/step
 - loss: 0.1191 - accuracy: 0.9829 - val_loss: 0.1141 - val_accuracy: 1.0000
'''


# 9. model evaluation : val dataset 
print('='*30)
print('model evaluation')
model.evaluate(x=x_val, y=y_val)
'''
model evaluation
1/1 [==============================] - 0s 0s/step
 - loss: 0.1141 - accuracy: 1.0000
'''

