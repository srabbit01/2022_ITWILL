# -*- coding: utf-8 -*-
"""
step05_if_while.py

tensorflow logic : if, while문 사용 
"""

import tensorflow.compat.v1 as tf # ver1.x 사용 
tf.disable_v2_behavior() # ver2.0 사용안함

# if
x = tf.constant(10) # x = 10

def true_fn() :
    return tf.multiply(x , 10) # x * 10

def false_fn():
    return tf.add(x, 10) # x + 10
    
y = tf.cond(x > 100, true_fn, false_fn) # y = 20
# tf.cond(조건식, true인경우, false인경우)
'''
True: true_fn 호출 (인수가 없는 함수로 정의)
False: false_fn 호출 (인수가 없는 함수로 정의)
'''


# while
i = tf.constant(0) # i = 0 : 반복변수 

def cond(i) : # i = 반복변수 
    return tf.less(i, 100) # i < 100

def body(i) : # i = 반복변수 
    return tf.add(i, 1) # i += 1

loop = tf.while_loop(cond, body, (i,)) # (조건문, 반복대상, (반복변수,))
'''
tf.while_loop(cond, body, (i,)) 
- cond: 조건문
- body: 조건문이 참인 경우 반복 실행문
- (i,): 반복변수(list, tuple)
'''

sess = tf.Session()

print("if =", sess.run(y))  # if = 20
print("loop =", sess.run(loop)) # loop = 100

sess.close()

