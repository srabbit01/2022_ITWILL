# -*- coding: utf-8 -*-
"""
indexing/slicing 
 - 1차원 indexing: list와 동일
 - 2,3차원 indexing
 - boolean indexing 
"""

import numpy as np

# 1. 색인(indexing) : object의 자료 참조  

# 1) list 배열 색인
ldata = [0,1,2,3,4,5]
print(ldata[:]) # 전체 원소 
print(ldata[3]) # 특정 원소 1개 
print(ldata[:3]) # 범위 선택 (0~n-1)
print(ldata[-1]) # 오른쪽 기준(-)

# 2) numpy 다차원 배열 색인 : list 동일 
arr = np.arange(10) # 0~9
print(arr[:])
print(arr[3])
print(arr[:3])
print(arr[-1])


# 2. slicing : 특정 부분을 잘라서 new object
arr = np.arange(10) # 0~9

# 주소 복사 
arr_obj = arr[1:4] # 주소 반환
print(arr_obj) # [1 2 3]
print(id(arr),id(arr_obj)) # 2806846283088 2806846388240
# 두 주소 다름 -> 일부 원소만 복사한 것이기 때문에 숫자는 다르나 동일 주소임

arr_obj[:] = 100 # 전체 100으로 수정(o)
print(arr_obj) # [100 100 100]

print(arr) # 원본 변경 

arr_obj2=arr[:]
print(id(arr),id(arr_obj2)) # 2806846747248 2806845808784
# id(변수) 주소가 다른 이유는 두 객체 자체의 주소는 다름 (독립된 객체)
# 그러나 그 객체 내 주소 복사

# 내용 복사
arr_obj3=arr[1:4].copy() # 값 반환
arr_obj3 # array([1, 2, 3])
# 완전 다른 객체

arr_obj3[:]=50

print(arr) # 원본 변경 없음

arr_obj4=arr.copy()

# 3. 고차원 색인(indexing)

# 1) 2차원 indexing : ppt. 21참조 
arr2d = np.array([[1,2,3],[4,5,6],[7,8,9]]) # 중첩list
print(arr2d) # 3행3열
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''
# 형식) obj[행,열]
arr2d[0][:]

# 행 index(기본)
print(arr2d[0, :]) # 1행 전체 
print(arr2d[0]) # 행 index(기본)
print(arr2d[0][1:]) # [2 3] -> 1행 지정 -> 2~3열 지정
print(arr2d[1:,1:])
print(arr2d[::2]) # 홀수행 선택(start:stop:step)

# 비연속 행렬
print(arr2d[[0,2]])

print(arr2d[[0,2], [0,2]]) # 1행1열, 3행3열 


# 2) 3차원 indexing 
arr3d = np.array([[[1,2,3],[4,5,6]], [[7,8,9], [10,11,12]]])
print(arr3d)
print(arr3d.shape) # (2, 2, 3) - (면,행,열)

# 면 index(기본)
print(arr3d[0]) # 1면 전체 
print(arr3d[0, 1])  # 1면의 1행 전체 : [4 5 6]
print(arr3d[0, 1, 1:])  # 1면 1행 2~3열 : [5 6]

# 4차원: 주로 image 처리 = [size,h,w,c]
# h: 세로, w: 가로
# c: 칼럼 이미지 (삼원색: RGB)

# 4. 조건식 색인(boolean index)
dataset = np.random.randn(3, 4) # 12개 
print(dataset)
'''
[[ 1.31757489 -0.38784468 -0.08494841  0.57136138]
 [-1.85763682  0.00219376  0.98089281 -2.00417053]
 [-0.61041334 -0.71765377 -1.09149542 -0.1069251 ]]
'''

# 0.7 이상 경우 
print(dataset[dataset >= 0.7])
# [1.31757489 0.98089281]

# 0.1 ~ 0.7: 범위 조건식 -> 논리식 표현 불가
# print(dataset[dataset>=0.1 and dataset<=0.7]) -> Error 발생

# numpy 논리식 함수 
'''
np.logical_and() # 논리곱 
np.logical_or() # 논리합
np.logical_not() # 부정 
np.logical_xor() # 배타적 논리합 
'''

result = dataset[np.logical_and(dataset >= 0.1, dataset <= 1.5)]
print('0.1 ~ 1.5 : 범위 조건식')
print(result) # [1.31757489 0.57136138 0.98089281]
len(result) # 3

# NOT(반대)
result2 = dataset[np.logical_not(np.logical_and(dataset >= 0.1, dataset <= 1.5))]
print(result2)
len(result2) # 9


# Pandas 객체 이용
import pandas as pd
ser=pd.Series([2,1,3,4,5])

ser[ser>=3]
# ser[ser>=2 and ser<=4] Value Error
ser[np.logical_and(ser>=2,ser<=4)]



