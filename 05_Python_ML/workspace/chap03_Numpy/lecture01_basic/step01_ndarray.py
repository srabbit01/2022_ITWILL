# -*- coding: utf-8 -*-
"""
Numpy 패키지 
  - 수치 과학용 데이터 처리 목적으로 사용 
  - 선형대수(벡터, 행렬) 연산 관련 함수 제공 
  - N차원 배열, 선형대수 연산, 고속 연산  
  - 수학/통계 함수 제공 
  - indexing/slicing (순서 존재)   
  - broadcast 연산: list + for = list 내포 굳이 하지 않아도 됨
"""

import numpy as np # 별칭 


# 1. list 배열 vs numpy 다차원 배열 

# 1) list 배열
lst = [1, 2, 3, 3.5] # 정수와 실수 자료형
print(lst) # 다양한 자료형 
print(lst * 3 ) # 3번 반복
sum(lst) # 외부 함수 

# 2) numpy 다차원 배열 
arr = np.array(lst) # array([list])  
type(arr) # numpy.ndarray
print(arr) # 동일한 자료형
print(arr * 0.5) # broadcast 연산 : 각 원소에 0.5 곱셈
arr.sum() # 자체 제공 

lst=[1,2,3,3.5,'4']
np.array(lst) # ['1', '2', '3', '3.5', '4']

# 원소 개수 확장(늘리기): numpy -> list 변환 후 늘리기
dir(arr) # tolist 활용
arr_lst=arr.tolist()
arr_lst * 3

# 2. array() : 다차원 배열 생성 

# 단일 list -> 1차원 배열 
lst1 = [3, 5.2, 4, 7]
print(lst1) # 단일 리스트 배열 

arr1d = np.array(lst1) # array(단일list)
print(arr1d.shape) # 자료구조 확인: (4,) -> 1차원
# [3, 5.2, 4, 7]

print('평균 =', arr1d.mean()) 
print('분산=', arr1d.var())
print('표준편차=', arr1d.std()) 
'''
평균 = 4.8
분산= 2.2199999999999998
표준편차= 1.489966442575134
'''

# 2) 중첩 list -> 2차원 배열
lst2=[[1,2,3,4],[5,6,7,8]]

arr2d=np.array(lst2)
arr2d.shape # (2,4) = (행,열)
print(arr2d)
'''
array([[1, 2, 3, 4],
       [5, 6, 7, 8]])
'''
print('평균 =', arr2d.mean()) 
print('분산=', arr2d.var())
print('표준편차=', arr2d.std()) 
'''
평균 = 4.5
분산= 5.25
표준편차= 2.29128784747792
'''

# 3. broadcast 연산 
# - 작은 차원이 큰 차원으로 늘어난 후 연산 

# scala(0) vs vector(1)
print(0.5 * arr1d) # 상수=0차원
# [1.5 2.6 2.  3.5]

# scala(0) vs matrix(2)
print(0.5 * arr2d)
'''
[[0.5 1.  1.5 2. ]
 [2.5 3.  3.5 4. ]]
'''

# vector(1) vs matrix(2)
print(arr1d * arr2d)
'''
[[ 3.  10.4 12.  28. ]
 [15.  31.2 28.  56. ]]
'''

# 모분산 vs 표본분산

'''
모집단 분산 = sum((x-mu)**2) / n
표본 분산 = sum((x-mu)**2) / n-1
'''

mu = arr1d.mean() # 4.8
diff = (arr1d - mu)**2  # 1d - scala : 브로드케스트  
var = sum(diff) / len(arr1d)
var=sum((arr1d-mu)**2)/arr1d.size # 함축적으로 작성 가능
print('모분산 =', var) # 2.2199999999999998
var2 = sum(diff) / (len(arr1d)-1)
print('표본분사 =',var2) # 2.9599999999999995
arr1d.var() # 2.2199999999999998


# 4. zeros or ones 
# zeros: 모든 값들이 0으로 채워진 행렬 (인수는 튜플)


zerr = np.zeros( (3, 10) ) # 3행5열 
print(zerr) # 희소행렬 : doc(3) vs word(10) 빈도수 
'''
[[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
 [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]]
'''

onearr = np.ones( (3, 10) ) # 3행5열 
print(onearr)
'''
[[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]]
'''


# 5. arange 
arr = np.arange(-1.2, 5.5) # float 사용 가능, 배열 객체  
# range(-1.2,5.5)
print(arr) # [-1.2 -0.2  0.8  1.8  2.8  3.8  4.8]
'''
range vs np.arange
- 공통: 일련의 정수 배열 생성 (이름과 기능 비슷)
  range(10): 0 ~ 9
  np.arange(10): 0 ~ 9
- 차이점
    - range: 정수형만 생성 가능 -> range(시작,끝,스텝)
    - np.arange: 정수형뿐만 아니라 실수형도 생성 가능
'''
# np.arange(끝), np.arange(시작,끝), np.arange(시작,끝,스텝)
np.arange(1,10) 
list(range(1,10)) # 위와 동일
np.arange(10)

# ex) x의 수열에 대한 2차 방정식 
x = np.arange(-1.0, 2, 0.1)
y = x**2 + 2*x + 3 # f(x) 함수 
print(y)

len(x) # 30
len(y) # 30

# f(x) 함수
def f(x):
    return x**2 + 2*x + 3

# 2차 방정식 그래프 그리기
import matplotlib.pyplot as plt

plt.plot(x,f(x)) # (x,y) 입력 -> y=f(x) 호출
plt.show() # 곡선 형태의 2차 방정식

# 색인 이용
zerr = np.zeros((3, 10))
zerr

cnt=0
for i in np.arange(3): # 행 index
    for j in np.arange(10): # 열 index
        cnt+=1 # 카운터
        zerr[i,j]=cnt
print(zerr)
'''
[[ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]
 [11. 12. 13. 14. 15. 16. 17. 18. 19. 20.]
 [21. 22. 23. 24. 25. 26. 27. 28. 29. 30.]]
'''
