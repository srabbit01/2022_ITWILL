# -*- coding: utf-8 -*-
"""
reshape : 모양 변경 
 - 1차원 -> 2차원 
 - 2차원 -> 다른 형태의 2차원
 - 3차원 -> 2차원  
T : 전치행렬 (행과 열 축 변환)
swapaxis : 축 변경 
transpose : 축 번호 순서로 구조 변경 
"""

import numpy as np

# 1. 모양변경
lst = list(range(1, 13)) # 1차원 배열
 
arr1d = np.array(lst)
arr2d=arr1d.reshape(3, 4) # 모양변경 (1d -> 2d)
print(arr2d)
arr2d.shape # (3,4)

# 주의: 원소의 size 변경 불가
arr1d.reshape(2,6) # 가능
# arr1d.reshape(2,5) # ValueError

# 2. 전치행렬
print(arr2d.T)
print(arr2d.T.shape) # (4, 3)
arr2d_new=arr2d.T
arr2d_new
'''
array([[ 1,  5,  9],
       [ 2,  6, 10],
       [ 3,  7, 11],
       [ 4,  8, 12]])
'''

# 3. swapaxes : 축 변경 
print('swapaxes')
print(arr2d.swapaxes(0, 1)) # 2차원의 경우 전치 행렬과 동일
# 2차원: 행=0, 열=1
# 변수.swapaxes(교환축1,교환축2) # 3차원이면 축의 숫자 표현
'''
1차원: 효과 없음
2차원: 전치행렬과 동일
3차원: 축 순서를 이용하여 자료구조 변경
'''


# 4. transpose
'''
3차원 : 축 순서를 이용하여 자료 구조 변경 
'''
arr3d = np.arange(1, 25).reshape(4, 2, 3)#(4면2행3열)
#print(arr3d)
print(arr3d.shape) # (4,2,3)
arr3d[0]
arr3d[-1]

# default : (면,행,열) -> (열,행,면)
arr3d_def = arr3d.transpose() # 파리미터 없음
print(arr3d_def.shape) # (4,2,3) -> (3,2,4)
print(arr3d_def)

# 0: 면축, 1: 행축, 2: 열축 -> (2:열, 0:면, 1:행)
arr3d.transpose(2,0,1).shape # (3,4,2)
