# -*- coding: utf-8 -*-
"""
step03_tensorboard.py

Tensorboard 
 - 그래프 시각화 도구
 - 그래프: 데이터 흐름도 (노드 + 엣지)
"""

import tensorflow.compat.v1 as tf # ver1.x 사용  
tf.disable_v2_behavior() # ver2.x 사용 안함 

# tensorboard 초기화 -> 가장 최근에 만들어진 그래프 시각화 의미
tf.reset_default_graph()

# 상수 정의 
x = tf.constant(1)
y = tf.constant(2)

# 사칙연산식 정의 
a = tf.add(x, y, name='a') # a = x + y
b = tf.multiply(a, 6, name='b') # b = a * 6
c = tf.subtract(20, 10, name='c') # c = 20 - 10
d = tf.div(c, 2, name = 'd') # d = c / 2

g = tf.add(b, d, name='g') # g = b + d
h = tf.multiply(g, d, name='h') # h = g * d

# session 객체 생성 
with tf.Session() as sess :
    h_calc = sess.run(h) # 식 device 할당 : 연산 
    print('h = ', h_calc) # h =  115
    # h를 실행하면 앞에 필요한 모든 식 참조
    # a, b -> c -> d -> g -> h까지 순차적으로 일괄 실행
    
    # Tensorboard Graph 생성
    # 1) 프로그램 모든 정의 모으기
    tf.summary.merge_all() # 상수, 식 모으는 역할
    # 2) 모은 정의에 대한 그래프 시각화 가능한 파일 만들기
    path=r'D:\7. Python DL'
    # path=r"C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\06. Python DL"
    writer=tf.summary.FileWriter(path+r'\graph',sess.graph) # graph 폴더 자동 생성
    # sess.graph:그래프 정보 기입
    writer.close()

'''
# tensoroard 실행 과정 오류 해결 방법
(tensorflow) > pip uninstall google-auth
(tensorflow) > pip install google-auth==1.6.3
(tensorflow) > tensorboard --logdir=D:\7. Python DL\graph
'''