# -*- coding: utf-8 -*-
"""
step03_softmax_classfier.py

다항분류기 : 테스트 데이터 적용 

- 활성함수: softmax 함수
- 손실함수: cross entropy 함수
"""

import tensorflow as tf # 분류 분석
from sklearn.metrics import accuracy_score #  model 평가 
import numpy as np  # data 생성

# 1. x, y 공급 data 
# [털, 날개]
x_data = np.array(
    [[0, 0], [1, 0], [1, 1], [0, 0], [0, 1], [1, 1]]) # [6, 2]

# [기타, 포유류, 조류] : [6, 3] 
y_data = np.array([ # one hot encoding 
    [1, 0, 0],  # 기타[0]
    [0, 1, 0],  # 포유류[1]
    [0, 0, 1],  # 조류[2]
    [1, 0, 0],  # 기타[0]
    [1, 0, 0],  # 기타[0]
    [0, 0, 1]   # 조류[2]
])


# 2. X, Y변수 정의 : type 일치 - float32
X = tf.constant(x_data, tf.float32) # [6, 2] - [관측치, x변수]
y = tf.constant(y_data, tf.float32) # [6, 3] - [관측치, y변수]


# 3. w, b변수 정의 : 초기값(난수) -> update 
tf.random.set_seed(123)
w = tf.Variable(tf.random.normal(shape=[2, 3])) # [입력수, 출력수]
b = tf.Variable(tf.random.normal(shape=[3])) # [출력수]


# 4. 회귀모델 
def linear_model(X) :
    model = tf.linalg.matmul(X, w) + b # 회귀방정식 
    return model 


# 5. softmax 함수   
def soft_fn(X) :
    model = linear_model(X)
    y_pred = tf.nn.softmax(model) # softmax(y예측치)
    return y_pred 


# 6. 손실함수 : 손실값 반환 
def loss_fn() : # 인수 없음 
    y_pred = soft_fn(X)
    # cross entropy : loss value 
    loss = -tf.reduce_mean(y * tf.math.log(y_pred) + (1-y) * tf.math.log(1-y_pred))
    return loss


# 7. 최적화 객체 
opt = tf.optimizers.Adam(learning_rate=0.1)


# 8. 반복학습 
for step in range(100) :
    opt.minimize(loss=loss_fn, var_list=[w, b])
    
    # 10배수 단위 출력 
    if (step+1) % 10 == 0 :
        print('step =', (step+1), ", loss val = ", loss_fn().numpy())
'''
step = 10 , loss val =  0.42504713
step = 20 , loss val =  0.24003288
step = 30 , loss val =  0.1296693
step = 40 , loss val =  0.08315238
step = 50 , loss val =  0.05832547
step = 60 , loss val =  0.04411757
step = 70 , loss val =  0.035440013
step = 80 , loss val =  0.029500918
step = 90 , loss val =  0.02518392
step = 100 , loss val =  0.021901028
'''
  
# 9. 최적화된 model 검증

# 예측 확률
y_prob = soft_fn(X)    
print(y_prob)
'''
     기타(0)       포유류(1)       조류(2)
[[9.7958988e-01 1.8227112e-02 2.1830460e-03]  -> 1번 관측치
 [1.0391075e-02 9.4032526e-01 4.9283687e-02]
 [1.3134375e-02 1.6666975e-02 9.7019863e-01]
 [9.7958988e-01 1.8227112e-02 2.1830460e-03]
 [9.6621275e-01 2.5210174e-04 3.3535108e-02]
 [1.3134375e-02 1.6666975e-02 9.7019863e-01]] -> 6번 관측치
'''

# 예측 결과: 가장 큰 확률 -> 색인 반환(10진수)
y_pred_idx = tf.argmax(y_prob,axis=1)
print(y_pred_idx) # [0 1 2 0 0 2]
# 실제 결과 변환
y_idx = tf.argmax(y,axis=1)
print(y_idx) # tf.argmax(y_prob,axis=1)

# 분류 정확도
acc=accuracy_score(y_idx, y_pred_idx)
print('accuracy =', acc)
# accuracy = 1.0 

# 전체 평가지표
from sklearn.metrics import classification_report
report=classification_report(y_idx, y_pred_idx)
print(report)
'''
              precision    recall  f1-score   support

           0       1.00      1.00      1.00         3
           1       1.00      1.00      1.00         1
           2       1.00      1.00      1.00         2

    accuracy                           1.00         6
   macro avg       1.00      1.00      1.00         6
weighted avg       1.00      1.00      1.00         6
 '''