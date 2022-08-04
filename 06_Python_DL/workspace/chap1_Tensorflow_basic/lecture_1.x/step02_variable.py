# -*- coding: utf-8 -*-
"""
step02_variable.py

Tesnorflow 1.0 버전 초기 실행 환경
- Tensorflow 변수
"""
'''
tensorflow
- 패키지 (numpy, pandas 같음)
'''

# Tensorflow code 
import tensorflow.compat.v1 as tf # ver1.x -> ver2.x 마이그레이션 
tf.disable_v2_behavior() # ver2.x 사용 안함 

''' 프로그램 정의 영역 '''
# 상수 정의  
x = tf.constant([1.5, 2.5, 3.5]) # 1차원 상수 
# 상수: 정의된 값 수정 불가능
print(x) # Tensor("Const:0", shape=(3,), dtype=float32)

# 변수 정의 : 반드시 변수 내 초기값 명시 필요
y = tf.Variable([1.0, 2.0, 3.0]) # 1차원 변수 
# 변수: 정의된 값 수정 가능
print(y) # <tf.Variable 'Variable:0' shape=(3,) dtype=float32_ref>
'''
변수=tf.Variable([초기값])
'''

# 계산식 정의
mul = x * y
print(mul) # Tensor("mul:0", shape=(3,), dtype=float32)


''' 프로그램 실행 영역 '''
with tf.Session() as sess : # 세션 객체 생성     
    print('x =', sess.run(x)) # 상수 실행 
    # x = [1.5 2.5 3.5]
    
    ## 프로그램 전역 변수 초기화해야 해당 변수 실행 가능
    sess.run(tf.global_variables_initializer()) # 변수 초기화: 최초로 값 할당
    '''
    - 상수: 초기화 필요 없음
    - 변수: 초기화 필요
    '''

    print('y=', sess.run(y)) # 변수 실행  
    y_re = sess.run(y.assign([2.0, 3.0, 4.0])) 
    print('y_re=', y_re)
    # y= [1. 2. 3.]
    
    print('y=', sess.run(y))
    
    # 식 -> 장치 할당
    # 동일 위치끼리 1:1 연산
    print('mul =', sess.run(mul)) # 식 연산
    # mul = [ 1.5  5.  10.5]
    
# with 키워드 외에서 객체 소멸 -> 별도 close 필요 없음

