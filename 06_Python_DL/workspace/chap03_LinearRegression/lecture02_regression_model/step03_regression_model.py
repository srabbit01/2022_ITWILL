# -*- coding: utf-8 -*-
"""
step03_regression_model.py
  - 회귀모델 : 딥러닝 최적화 알고리즘 

tensorflow 가상환경에서 numpy 설치     
(base) > conda activate tensorflow
(tensorflow) > conda install numpy
(tensorflow) > conda install pandas
"""

import tensorflow as tf # 딥러닝 최적화 알고리즘 사용  
import numpy as np  # dataset 생성
# 1. X, y변수 생성 
X = np.array([1, 2, 3]) # 독립변수(입력) : [n] -> n: 관측치
y = np.array([2, 4, 6]) # 종속변수(출력) : [n] -> n: 관측치

# 2. w, b변수 정의 
tf.random.set_seed(123)
w  = tf.Variable(tf.random.normal([1])) # 가중치 : 난수 
b  = tf.Variable(tf.random.normal([1])) # 편향 : 난수 


# 3. 회귀모델 
def linear_model(X) :
    # global w, b -> 전역변수 지정 생략 가능
    y_pred = tf.math.multiply(X, w) + b # 단순선형 회귀방정식 
    return y_pred 


# 4. 손실/비용 함수(loss/cost function) : 손실반환(MSE)
def loss_fn() : # 인수 없음 
    global X # 생략 가
    y_pred = linear_model(X) # 예측치 
    err = tf.math.subtract(y, y_pred) # 정답 - 예측치  
    loss = tf.reduce_mean(tf.square(err)) # MSE  
    return loss


# 5. model 최적화 객체 : 오차의 최소점을 찾는 객체 
dir(tf.optimizers)
'''
['Adadelta',
 'Adagrad',
 'Adam', -> 현재 사용되는 최적화 객체
 'Adamax',
 'Ftrl',
 'Nadam',
 'Optimizer',
 'RMSprop',
 'SGD', -> 과거 많이 사용
 '''
# SGD: 경사하강 알고리즘: 숫자가 클 수록 수렴 위치 빨리 찾음
# optimizer = tf.optimizers.SGD(learning_rate=0.1) # lr 기본: 0.01
# learning_rate: 학습률
print(f'기울기(w) 초기값 = {w.numpy()}, 절편(b) 초기값 = {b.numpy()}')
# 기울기(w) 초기값 = [-0.8980837], 절편(b) 초기값 = [0.33875433]

# [다른 알고리즘] Adam 알고리즘 사용
optimizer = tf.optimizers.Adam(learning_rate=0.4) # lr 기본: 0.001
# 기본 0.001은 매우 큰 오차를 보임
'''
1. tf.optimizers.Adam(learning_rate=0.001): 기본
   - step = 100 , loss value = 31.849894
   - 기울기(w) = [-0.7989749], 절편(b) = [0.43780878]
2. tf.optimizers.Adam(learning_rate=0.01)
   - step = 100 , loss value = 10.356687
   - 기울기(w) = [-0.00062146], 절편(b) = [1.2284533]
3. tf.optimizers.Adam(learning_rate=0.1)
   - step = 100 , loss value = 0.3030051
   - 기울기(w) = [1.3520416], 절편(b) = [1.4479202]
4. tf.optimizers.Adam(learning_rate=0.1)
   - step = 100 , loss value = 0.00044377428
   - 기울기(w) = [1.9891989], 절편(b) = [0.04073321]
'''
# SGD보다 0에 수렴정도가 더 높으며 최적화 객체로 많이 사용


# 6. 반복학습 : 100회
for step in range(100) : # 반복학습 횟수 지정
    optimizer.minimize(loss=loss_fn, var_list=[w, b]) #(손실값, update 대상변수)
    # loss_fn 괄호 생략 필수: minimize 함수 내 괄호 없는 함수 괄 쓰면 Error 발생
    # var_list: 가중치 및 편향 (update 대상변수 = 조절변수)
    # step 단위 -> 손실값 -> a,b 출력 
    print('step =', (step+1), ", loss value =", loss_fn().numpy())
    # a, b 변수 update 
    print(f'기울기(w) = {w.numpy()}, 절편(b) = {b.numpy()}')
'''
step = 1 , loss value = 0.1612598
기울기(w) = [1.5335835], 절편(b) = [1.0602307] -> 초기값
step = 2 , loss value = 0.16048528
기울기(w) = [1.5347065], 절편(b) = [1.0576828]
...
step = 99 , loss value = 0.10061276
기울기(w) = [1.6315976], 절편(b) = [0.83746505]
step = 100 , loss value = 0.10012954
기울기(w) = [1.6324832], 절편(b) = [0.83545184] -> weight & bias update
# 기울기와 절편 조금씩 개선
'''
# 결과적으로, 손실이 0에 수렴됨을 알 수 있음
# 이미 최적화된 상태로 기울기와 절편 지정

# [학습률 수정] learning rate == 0.1
# 학습률이 높을 수록 0의 수렴 속도 빠름
# 그러나, 정확한 위치 지나칠 수 있음
'''
1. tf.optimizers.SGD(learning_rate=0.001)
   - step = 100 , loss value = 4.022634
   - 기울기(w) = [0.6644551], 절편(b) = [0.98778546]
2. tf.optimizers.SGD(learning_rate=0.01): 기본
   - step = 100 , loss value = 0.1620378
   - 기울기(w) = [1.5324576], 절편(b) = [1.0627847]
3. tf.optimizers.SGD(learning_rate=0.1): 0의 수렴속도 빠름 -> 최소점 위치를 넘어갈 우려
   - step = 100 , loss value = 0.002018992
   - 기울기(w) = [1.9478129], 절편(b) = [0.11863367]
'''
# loss = 0.002018992이면 최적화되었음을 알 수 있음


# 7. 최적화된 model 검증

# 1) Test
# test set 만들기
X_test = [2.5]

# 가중치 및 편향 지정
# w=1.9478129
# b=0.11863367

ytest_pred=linear_model(X_test)
print('X_test =', X_test)
print('y_test_pred', ytest_pred.numpy()) # 4.988166
'''
X_test = [2.5]
y_test_pred [4.988166]
'''

# 2) 회귀선 그리기
import matplotlib.pyplot as plt
y_pred=linear_model(X)
plt.plot(X,y,'y--')
plt.plot(X,y_pred,'g-')
plt.show()
