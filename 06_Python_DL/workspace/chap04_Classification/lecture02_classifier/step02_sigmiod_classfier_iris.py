# -*- coding: utf-8 -*-
"""
step02_sigmiod_classfier_iris.py

이항분류기 : 실제 데이터(iris) 적용 
"""

import tensorflow as tf
from sklearn.datasets import load_iris # dataset
from sklearn.preprocessing import minmax_scale # x변수 정규화 
from sklearn.preprocessing import OneHotEncoder # y변수 인코딩
from sklearn.metrics import accuracy_score #  model 평가 


# 1. x, y 공급 data 
X, y = load_iris(return_X_y=True)
X.shape # (150, 4)

# x, y변수 선택 : 이항분류 data 선정 (종속변수 범주 2개)
x_data = X[:100]
y_data = y[:100] 
y_data.shape # (100, 1)

# x, y 변수 전처리

# x변수 정규화 
x_data = minmax_scale(x_data) 


# y변수 인코딩 : 원 핫 인코딩 -> 0 = [1, 0], 1 = [0, 1]
obj = OneHotEncoder() # 객체 생성
y_data = obj.fit_transform(y_data.reshape([-1, 1])).toarray()
y_data.shape # (100, 2)
print(y_data) # 0 or 1


# 2. X, y변수 정의 : type 일치 - float32
X = tf.constant(x_data, tf.float32)  # [100, 4] - [관측치, x변수]
y = tf.constant(y_data, tf.float32) # [100, 2] - [관측치, y변수]


# 3. w, b변수 정의 : 초기값(난수) -> update 
tf.random.set_seed(123) # w,b 난수 seed값 지정
w = tf.Variable(tf.random.normal(shape=[4, 2])) # [입력수, 출력수] 
b = tf.Variable(tf.random.normal(shape=[2])) # [출력수]


# 4. 회귀모델 
def linear_model(X) :
    model = tf.linalg.matmul(X, w) + b # [100, 4] @ [4, 2] + b
    return model 
    
# 5. sigmoid 함수   
def sig_fn(X) :
    model = linear_model(X)
    y_pred = tf.nn.sigmoid(model) 
    return y_pred 
    
# 6. 손실함수  
def loss_fn() : # 인수 없음 
    y_pred = sig_fn(X)
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
step = 10 , loss val =  0.45891312
step = 20 , loss val =  0.27239054
step = 30 , loss val =  0.16356829
step = 40 , loss val =  0.11121315
step = 50 , loss val =  0.08113701
step = 60 , loss val =  0.06374382
step = 70 , loss val =  0.052323904
step = 80 , loss val =  0.044318132
step = 90 , loss val =  0.038383108
step = 100 , loss val =  0.03377265
'''

# 9. 최적화된 model 검증
y_pred = sig_fn(X) # sigmoid 함수 호출
print(y_pred) # 0~1 확률값
'''
[[9.84343648e-01 3.37204039e-02] -> 0.984, 0.0337
 [9.75571156e-01 8.59161913e-02]
 [9.88636494e-01 4.77036536e-02]
 [9.85392451e-01 6.83519542e-02]
 [9.88621473e-01 2.61522830e-02]
 ...
 [1.26175582e-02 9.48259830e-01]
 [4.85536456e-03 9.62372184e-01]
 [1.31359339e-01 8.72061849e-01] -> 0.013, 0.872
 [1.23030543e-02 9.53442931e-01]]-> 0.012, 0.953 
'''

# T/F -> 1/0
y_pred=tf.cast(sig_fn(X).numpy()>0.5,dtype=tf.float32).numpy()
print(y_pred)
'''
[[1. 0.]
 [1. 0.]
 [1. 0.]
 [1. 0.]
 ...
 [0. 1.]
 [0. 1.]
 [0. 1.]
 [0. 1.]]
'''

# 분류 정확도 확인
acc = accuracy_score(y, y_pred)
print('accuracy =', acc)
# accuracy = 1.0