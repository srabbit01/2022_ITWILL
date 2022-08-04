# -*- coding: utf-8 -*-
"""
step04_softmax_classfier_iris.py

다항분류기 : 실제 데이터(iris) 적용
"""

import tensorflow as tf
from sklearn.datasets import load_iris
from sklearn.preprocessing import minmax_scale # x_data -> 0~1
from sklearn.preprocessing import OneHotEncoder # y_data -> encoding
from sklearn.metrics import accuracy_score #  model 평가 
# from sklearn.model_selection import train_test_split

tf.random.set_seed(123) # seed 고정 - 동일 결과 

# 1. x, y 공급 data 
X, y = load_iris(return_X_y=True)
X.shape


# x변수 정규화 
x_data = minmax_scale(X)

# y변수 : reshape, 인코딩 
obj = OneHotEncoder()
y_data = obj.fit_transform(y.reshape([-1, 1])).toarray()
print(y_data)
'''
1 0 0 - class1
0 1 0 - class2
0 0 1 - class3
'''
# train_test_split는 tf.constant 객체로 만들기 이전에 분류하기

# 2. X, Y변수 정의 : type 일치 - float32
X = tf.constant(x_data, tf.float32) # [150, 4]
y = tf.constant(y_data, tf.float32) # [150, 3]


# 3. w, b변수 정의 : 초기값(난수) -> update 
w = tf.Variable(tf.random.normal(shape=[4, 3])) # [입력수, 출력수]
b = tf.Variable(tf.random.normal(shape=[3])) # [출력수]


# 4. 회귀모델 
def linear_model(X) :
    model = tf.linalg.matmul(X, w) + b  
    return model 


# 5. softmax 함수   
def soft_fn(X) :
    model = linear_model(X)
    y_pred = tf.nn.softmax(model) # softmax + model
    return y_pred 


# 6. 손실함수 
def loss_fn() : # 인수 없음 
    y_pred = soft_fn(X)
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
step = 10 , loss val =  0.095455974
step = 20 , loss val =  0.09129082
step = 30 , loss val =  0.087587096
step = 40 , loss val =  0.08427003
step = 50 , loss val =  0.08128057
step = 60 , loss val =  0.07857131
step = 70 , loss val =  0.07610363
step = 80 , loss val =  0.07384584
step = 90 , loss val =  0.07177163
step = 100 , loss val =  0.06985895
'''

    
# 9. 최적화된 model 검증

# 예측 확률
y_prob = soft_fn(X)    
print(y_prob)
'''
    vari
[[9.67301726e-01 3.26799490e-02 1.83358552e-05]
 [9.02912199e-01 9.70308334e-02 5.69516014e-05]
 [9.61269617e-01 3.87098417e-02 2.05204924e-05]
 [9.48999524e-01 5.09678908e-02 3.25807523e-05]
 ...
 [8.79263040e-04 2.84891367e-01 7.14229345e-01]
 [1.57342281e-03 2.04846248e-01 7.93580353e-01]
 [2.13499670e-03 8.20433050e-02 9.15821671e-01]
 [8.66977125e-03 3.35628957e-01 6.55701280e-01]]
'''

# 예측 결과
y_pred = tf.argmax(y_prob,axis=1)
print(y_pred)
'''
[0 0 0 ... 2 2 2 2 2 2]
'''
y_test = tf.argmax(y, axis=1)


# 분류 정확도
acc=accuracy_score(y, y_pred)
print('accuracy =', acc)
# accuracy = 0.9533333333333334

# 전체 평가지표
report=classification_report(y, y_pred)
print(report)
'''
              precision    recall  f1-score   support

           0       1.00      1.00      1.00        50
           1       0.92      0.94      0.93        50
           2       0.94      0.92      0.93        50

    accuracy                           0.95       150
   macro avg       0.95      0.95      0.95       150
weighted avg       0.95      0.95      0.95       150
'''    

# 혼동행렬
from sklearn.metrics import confusion_matrix
confusion_matrix(y, y_pred)
'''
array([[50,  0,  0],
       [ 0, 47,  3],
       [ 0,  4, 46]], dtype=int64)
'''

