# -*- coding: utf-8 -*-
"""
문3) 다음 digits 데이터셋을 이용하여 다항분류기를 작성하시오.
    <조건1> 아래 <출력결과>를 참고하여 학습율과 반복학습 적용
    <조건2> epoch에 따른 loss value 시각화 
   
 <출력결과>
step = 200 , loss = 0.06003735238669643
step = 400 , loss = 0.02922042555340125
step = 600 , loss = 0.01916724251850193
step = 800 , loss = 0.01418028865527556
step = 1000 , loss = 0.011102086315873883
step = 1200 , loss = 0.008942419709185086
step = 1400 , loss = 0.007311927138572721
step = 1600 , loss = 0.006023632246639046
step = 1800 , loss = 0.004981346240771604
step = 2000 , loss = 0.004163072611802871
========================================
accuracy = 0.9648148148148148
"""

import tensorflow as tf # ver 2.0

from sklearn.datasets import load_digits # dataset 
from sklearn.preprocessing import minmax_scale # x_data -> 0~1
from sklearn.preprocessing import OneHotEncoder # y data -> one hot
from sklearn.metrics import accuracy_score # model 평가 
from sklearn.model_selection import train_test_split # dataset split
import matplotlib.pyplot as plt # loss value 시각화
 
'''
digits 데이터셋 : 숫자 필기체 이미지 -> 숫자 예측(0~9)

•타겟 변수 : y
 - 0 ~ 9 : 10진수 정수 
•특징 변수(64픽셀) : X 
 -0부터 9까지의 숫자를 손으로 쓴 이미지 데이터
 -각 이미지는 0부터 15까지의 16개 명암을 가지는 
  8x8=64픽셀 해상도의 흑백 이미지
'''

# dataset load 
digits = load_digits() # dataset load

X = digits.data  # X변수 
y = digits.target # y변수 
print(X.shape) # (1797, 64) 
print(y.shape) # (1797,)


# 1. X, y변수 전처리  

# X변수 : 정규화
x_data = minmax_scale(X) 

# y변수 : one-hot encoding 
obj = OneHotEncoder()
y_data = obj.fit_transform(y.reshape([-1, 1])).toarray()


# 2. digits dataset split
x_train, x_test, y_train, y_test = train_test_split(
    x_data, y_data, test_size=0.3, random_state=123)


# 3. w, b 변수 정의 
w = tf.Variable(tf.random.normal([64, 10], dtype=tf.float64)) # [입력수, 출력수]
b = tf.Variable(tf.random.normal([10], dtype=tf.float64)) # [출력수]


# 5. 회귀방정식 
def linear_model(X) : # train, test
    y_pred = tf.matmul(X, w) + b  
    return y_pred


# 6. softmax 활성함수 적용 
def soft_fn(X):
    y_pred = linear_model(X)
    soft = tf.nn.softmax(y_pred)
    return soft

# 7. 손실 함수 정의 
def loss_fn() : #  인수 없음 
    soft = soft_fn(x_train)   
    loss = -tf.reduce_mean(y_train*tf.math.log(soft)+(1-y_train)*tf.math.log(1-soft))
    return loss


# 8. 최적화 객체 : learning_rate = 0.01
optimizer = tf.optimizers.Adam(lr=0.01) 


# 9. 반복학습
loss_value=[]
for step in range(2000):
    optimizer.minimize(loss_fn, var_list=[w, b])
    if (step+1) % 200 == 0:
        print(f'step = {step+1}, loss = {loss_fn().numpy()}')
    loss_value.append(loss_fn().numpy())
'''
step = 200, loss = 0.048713968104823695
step = 400, loss = 0.024546340073238204
step = 600, loss = 0.01607587978625478
step = 800, loss = 0.011732316214163261
step = 1000, loss = 0.009047678105340923
step = 1200, loss = 0.007193547323871098
step = 1400, loss = 0.005830417609596481
step = 1600, loss = 0.0047998141475908114
step = 1800, loss = 0.0040023668092058935
step = 2000, loss = 0.003375412520620523
'''

    
# 10. 최적화된 model 검증 

# 1) 크로스 엔트로피 확인
def loss_fn() : #  인수 없음 
    soft = soft_fn(x_test)   
    loss = -tf.reduce_mean(y_test*tf.math.log(soft)+(1-y_test)*tf.math.log(1-soft))
    return loss
print(f'loss = {loss_fn().numpy()}')
# loss = 0.0207523192994807

# 2) 예측값 확률
y_test_prob = soft_fn(x_test)
print(y_test_prob)
'''
[[6.53311039e-08 5.42838820e-10 2.91295261e-05 ... 2.79682954e-06
  6.08586088e-08 3.49595395e-04]
 [3.21650686e-06 7.71193614e-07 3.01759639e-06 ... 2.09065498e-05
  4.39434770e-06 2.97829122e-03]
 [6.57769079e-06 3.19690558e-06 2.52667122e-11 ... 3.63707700e-05
  4.66901064e-08 4.87075490e-09]
 ...
 [1.72231211e-05 1.38013384e-08 4.65507221e-06 ... 4.36284207e-06
  2.20710449e-05 9.98483173e-01]
 [3.76765467e-06 2.33139564e-11 3.25702969e-06 ... 8.71432070e-06
  7.23525345e-08 1.41957483e-09]
 [2.15442977e-08 1.13212924e-03 1.15766848e-11 ... 8.05092199e-04
  1.04331967e-08 2.95733804e-09]]
'''

# 3) 예측값 전환
y_test_pred = tf.argmax(y_test_prob,axis=1)
print(y_test_pred)
'''
[3 3 4 4 4 3 ... 1 7 6 9 5 4]
'''
y_test = tf.argmax(y_test,axis=1)

# 4) 분류 정확도 확인
acc = accuracy_score(y_test, y_test_pred)
print('accuracy =', acc)
# accuracy = 0.9629629629629629


# 11. loss value vs epochs 시각화 
plt.plot(loss_value,'r-')
plt.xlabel('Epochs')
plt.ylabel('Loss_value')
plt.show()
# [해설] 약 200부터 loss value = 0에 수렴 (큰 변화 없음) -> epochs = 200 적절