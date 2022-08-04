# -*- coding: utf-8 -*-
"""
step01_tensorflow_basic.py

Tesnorflow 1.0 버전 초기 실행 환경
- tensorflow ver1.x 환경 
- tensorflow 상수와 식 정의 
"""
# Python code
x=10 # 정의와 동식에 할당
y=20
z=x+y
print(z) # 30

# Tensorflow code
# compat: 최신 버전에서 이전 버전의 코드 실행 의미 (v1: 버전1) 
import tensorflow.compat.v1 as tf # ver2.x 환경에서 ver1.x 사용
# tf 모듈 내에서는 v2 코드 사용하지 않음 의미
tf.disable_v2_behavior() # ver2.x 사용 안함 
# 최신 버전의 경우, import tensorflow as tf로 메모리 상 로딩

''' 프로그램 정의 영역  : 모델 구성 '''
# 상수 정의: 식만 작성
x = tf.constant(10) # 숫자 상수 정의 : x = 10 -> 상수가 할당 X
y = tf.constant(20) # 숫자 상수 정의 : y = 20
# <tf.Tensor 'Const_1:0' shape=() dtype=int32>
'''
x = 10
y = 20
'''
# Tensor 정보 확인
# 아직 상수가 할당되지 않았으며 shape=(), 정의된 상태임을 의미
print(x) # Tensor("Const_2:0", shape=(), dtype=int32)
print(y) # Tensor("Const_3:0", shape=(), dtype=int32)

# 식 정의 
z = tf.add(x, y) # z = x + y
# <tf.Tensor 'Add:0' shape=() dtype=int32>
print(z)
# Tensor("Add_1:0", shape=(), dtype=int32)
# 덧셈할 것임을 정의
# Tensor: Tensorflow에서 사용되는 모든 데이터

''' 프로그램 실행 영역 : 모델 실행 '''
# sess: 값 할당
sess = tf.Session() # 세션 생성 

# 장치(cpu 혹은 gpu)에 정의 정보 할당
# run 되어야 상수 만들어져 반환
print('x=', sess.run(x)) # x = 10
print('y=', sess.run(y)) # y = 20
print('z=', sess.run(z)) # z = 30
# sess.run(변수): 변수를 디바이스에 할당할 것 임을 의미
# tensor flow 2.0에서는 정의와 동시에 실행 가능
# 초기 tensorflow 1.0에서는 정의와 실행이 이원화됨
# -> 정의 후 Session객체로 디바이스에 할당 필요
# Session이 매개체 역할을 함

sess.close() # 세션 닫기 
# 프로그램 종료






