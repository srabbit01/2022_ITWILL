# -*- coding: utf-8 -*-
"""
step04_variable_feed.py

 Tensorflow 변수 유형 
 1. 초기값을 갖는 변수 
   형식) tf.Variable(초기값)
 2. 초기값을 공급하는 변수: 초기값 결정되지 않았으며, 변수를 사용하고자 할 때 값 공급
   형식) tf.placeholder(자료형(dtype), 모양(shape))
"""

import tensorflow.compat.v1 as tf # ver1.x 사용  
tf.disable_v2_behavior() # ver2.x 사용 안함 

# 변수 정의 : 공급형 변수 
a = tf.placeholder(dtype=tf.float32) # shape 생략 
b = tf.placeholder(dtype=tf.float32, shape=[1]) # shape 지정 

# 식 정의 : 변수 참조 
mul = tf.multiply(a, b) 

add = tf.add(mul,10)


with tf.Session() as sess :
    # a, b 자료 공급 일정한 경우
    feed_data = {a : [2.5, 3.5], b : [3.5]}
    
    # 식 실행 : a,b 자료 공급 
    mul_re = sess.run(mul, feed_dict = feed_data)
    print('mul =', mul_re) # mul = [ 8.75 12.25]
    # broadcast 연산
    
    # add 식 실행: a, b 자료 공급 필요
    add_re=sess.run(add, feed_dict={a:[2.5, 3.5,1.5],b:[3.5]})
    print('add_re =',add_re) # add_re = [18.75 22.25 15.25]
    
    









