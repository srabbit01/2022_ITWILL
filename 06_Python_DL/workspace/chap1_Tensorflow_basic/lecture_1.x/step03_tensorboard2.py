# -*- coding: utf-8 -*-
"""
step03_tensorboard2.py

name_scope 이용
 - 영역별 tensorboard 시각화 
 - name_scope: 영역에 이름 붙이기
 - 영역별 코드가 어떤 역할을 하는지 블록화
"""

import tensorflow.compat.v1 as tf # ver1.x 사용 
tf.disable_v2_behavior() # ver2.x 사용 안함 

# tensorboard 초기화 
tf.reset_default_graph()

# name : 한글, 공백, 특수문자 사용불가 
X = tf.constant(5.0, name = 'x_data') # 입력변수 
a = tf.constant(10.1, name = 'a') # 기울기 
b = tf.constant(4.45, name = 'b') # 절편 
Y = tf.constant(55.0, name = 'y_data') # 출력(정답)변수 

# name_scope : 한글, 공백, 특수문자 사용불가  
with tf.name_scope('regress_model') as scope :
    model = (X * a) + b # 회귀방정식 : 예측치  
    
with tf.name_scope('model_error') as scope :
    model_err = model - Y # err = 측치-정답 

with tf.name_scope('model_eval') as scope :
    square = tf.square(model_err) # 오차 제곱 
    mse = tf.reduce_mean(square) # 오차 제곱 평균 : MSE

# 프로그램 실행
with tf.Session() as sess :
    # 각 영역별 실행 결과 
    print('Y = ', sess.run(Y))
    y_pred = sess.run(model)
    print('y pred =', y_pred)
    err = sess.run(model_err)
    print('model error =', err)
    print('MSE = ', sess.run(mse))    
    
    # Tensorboard Graph 생성
    # 1) 프로그램 모든 정의 모으기
    tf.summary.merge_all() # 상수, 식 모으는 역할
    # 2) 모은 정의에 대한 그래프 시각화 가능한 파일 만들기
    path=r'C:'
    # path=r"C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\06. Python DL"
    writer=tf.summary.FileWriter(path+r'\graph',sess.graph) # graph 폴더 자동 생성
    # sess.graph:그래프 정보 기입
    writer.close()
'''
Y =  55.0
y pred = 54.95
model error = -0.049999237
MSE =  0.0024999238
'''
    