# -*- coding: utf-8 -*-
"""
step02_functin_repalce.py

2. 함수(function)사용 권장 
  - 공급형 변수 -> 함수의 인수로 대체 
  - API 정리 : tf.placeholder() 사용 안함 
"""
import tensorflow as tf # ver2.3

## Version 1.x 공급형 변수 사용
'''
# 변수 정의 : 공급형 변수 
a = tf.placeholder(dtype=tf.float32) # shape 생략 
b = tf.placeholder(dtype=tf.float32, shape=[1]) # shape 지정 

# 식 정의 : 변수 참조 
mul = tf.multiply(a, b) 

add = tf.add(mul, 10)

with tf.Session() as sess :
    # 식 실행 : a,b 자료 공급 
    mul_re = sess.run(mul, feed_dict = {a : [2.5, 3.5], b : [3.5]})
    print('mul =', mul_re) 
'''

## Version 2.x
# tf.placeholder -> function 대체 
def mul_fn(a, b) : # python data 넣음
    return tf.multiply(a, b)

def add_fn(mul):
    return tf.add(mul, 10)

# a, b 자료 생성
a = [2.5, 3.5]
b = [3.5]

mul_fn(a,b)
# <tf.Tensor: shape=(2,), dtype=float32, numpy=array([ 8.75, 12.25], dtype=float32)>
mul=mul_fn(a,b).numpy()
print('mul_fn =',mul)
# mul_fn = [ 8.75 12.25]

print('add_fn =',add_fn(mul).numpy()) 
# add_fn = [18.75 22.25]
