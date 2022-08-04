# -*- coding: utf-8 -*-
"""
step02_timeSeries_RNN.py

 - 시계열데이터 + RNN model = 시계열분석 
"""
import pandas as pd # csv file read 
import matplotlib.pyplot as plt # 시계열 시각화 
import numpy as np # ndarray
import tensorflow as tf # seed 값 
from tensorflow.keras import Sequential # model 
from tensorflow.keras.layers import SimpleRNN, LSTM, Dense # RNN layer 

tf.random.set_seed(123) # seed값 지정 

# 1. csv file read : 주식데이터 
path = r'C:/work/Crystal/DataAnalysis/[ITWILL]BigDataAnalysis_ExpertTraining/06_Python_DL/workspace/chap10_RNN_model/data'
timeSeries = pd.read_csv(path + '/timeSeries.csv')
timeSeries.info()
'''
 0   no      100 non-null    int64  
 1   data    100 non-null    float64 -> 주식 데이터
'''

data = timeSeries['data'] # 주식 데이터만 추출
print(data) # 주가 정규화 자료
# 실제 금액 단위 정규화 후, 사용
print(len(data)) # 100

# 주식에 대한 시계열 자료 시각화
plt.plot(data,'g--',label='Time Series')
plt.legend()
plt.show()
# 상승 -> 하강 -> 상승
'''
# 하나씩 증가하면서 계산: 900번 학습
처음: 0~9
마지막: 마지막-10~마지막
'''

# 2. RNN 적합한 dataset 생성 : (batch_size, time_steps, features)
x_data = [] # 입력값
for i in range(len(data)-10) : # 90번 반복: 0 ~ 89
    for j in range(10) : # 10번 반복: 0 ~ 9
        x_data.append(data[i+j]) # 900번 반복: 90 * 10 = 900
# 900개의 중첩 리스트 생성
# 리스트는 'x_data.shape' 자료 모양 확인 불가능
# list -> array
x_data = np.array(x_data)
x_data.shape # (900,) = 900개의 학습 데이터 생성
'''
 i,  j      -> x_data: 10개 씩 데이터 추출
 0,  0 ~ 9  -> x_data[0~9]
 1,  1 ~ 10 -> x_data[1~10]
 2,  2 ~ 11 -> x_data[2~11]
 :
 89, 89 ~ 98 -> x_data[89~98]
'''

y_data = []
for i in range(len(data)-10) : # 90번 반복: 0 ~ 89
    y_data.append(data[i+10]) # 90
# list -> array
y_data = np.array(y_data)
y_data.shape # (90,) = 90개의 정답 데이터 생성
'''
 i  ->  y_data
 0  ->  y_data[10]
 1  ->  y_data[11]
 2  ->  y_data[12]
 :
 89 ->  y_data[99]
'''


# train(700)/val(200) split 
test_size=900*200/900
x_train = x_data[:700].reshape(70,10,1) # = 700개
x_val = x_data[700:].reshape(-1,10,1) # = reshape(20,10,1) = 200개

x_train.shape # (70, 10, 1) 
x_val.shape # (20, 10, 1)

# train(70)/val(20) split 
y_train = y_data[:70].reshape(70
y_val = y_data[70:].reshape(20)



# 3. model 생성 
model = Sequential()

input_shape = (10, 1)

# RNN layer 추가 
model.add(SimpleRNN(units=8, input_shape=input_shape, 
                    activation ='tanh'))

# DNN layer 추가 
model.add(Dense(units=1)) # 출력 - 회귀모델

# model 학습환경 
model.compile(optimizer='sgd', 
              loss='mse', metrics=['mae'])

# model 학습 
model.fit(x=x_train, y=y_train, epochs=400, verbose=1)
'''
Epoch 400/400
3/3 [==============================] - 0s 2ms/step
 - loss: 0.0852 - mae: 0.2312
'''


# model 예측 
y_pred = model.predict(x_val) 
print(y_pred)


# y_true vs y_pred 
plt.plot(y_val, 'y--', label='real value')
plt.plot(y_pred, 'r--', label='predicted value')
plt.legend(loc='best')
plt.show()


#######################################
### 훈련셋과 예측값 결합 시계열 시각화  
#######################################

# ones_like() : 특정 shape갖는 데이터를 이용하여 1를 갖는 배열 생성  
threshold = np.ones_like(y_pred, dtype='bool') # 1 -> True 변경 
# ones_like: ones와 비슷하게 y_pred와 동일한 크기의 1만 갖는 배열 생성
# 즉, 벡터 초기화 (1=True)
threshold[:-future] = False # 1~70 : False, 71~90 : True 
# = 존재하는 데이터 False, 예측 데이터 True

# 1차원 reshape
pred_x = np.arange(len(y_pred)).reshape(-1, 1) # x축(시간축)
pred_y = y_pred # y축(통계량) 

pred_x.shape # (90, 1)
pred_y.shape # (90, 1) 

# 한글 & 음수부호 지원 
plt.rcParams['font.family'] = 'Malgun Gothic'
import matplotlib
matplotlib.rcParams['axes.unicode_minus'] = False

# y_true vs y_pred 
# 즉, 실제 데이터 색상 light blue
plt.plot(y_data, color='lightblue', linestyle='--', marker='o', label='real value')
# 예측 데이터 색성 red
plt.plot(pred_x[threshold], pred_y[threshold], 'r--', marker='o', label='predicted value')
plt.legend(loc='best')
plt.title(f'{20}개의 시계열 예측결과')
plt.show()
