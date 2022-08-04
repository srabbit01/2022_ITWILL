# -*- coding: utf-8 -*-
"""
step05_subplot.py

 subplot 차트 시각화 
"""

import numpy as np # 수치 data 생성 
import matplotlib.pyplot as plt # data 시각화 


# 1. subplot 생성 
fig = plt.figure(figsize = (10, 5)) # 차트 size 지정  # 가로픽셀, 세로픽셀
x1 = fig.add_subplot(2,2,1) # 2행2열 1번 
x2 = fig.add_subplot(2,2,2) # 2행2열 2번 
x3 = fig.add_subplot(2,2,3) # 2행2열 3번 
x4 = fig.add_subplot(2,2,4) # 2행2열 4번 

# 2. 각 격차 차트 그리기
data1 = np.random.randn(100)
data2 = np.random.randint(1, 100, 100)
cdata = np.random.randint(1, 4, 100)


# 각 격자 위치 내 그래프 입력
x1.hist(data1) # 히스토그램
x2.scatter(data1,data2,c=cdata) # 산점도
x3.plot(data1) # 기본 선 그래프
x4.plot(data1,data2,'g--') # 선색 및 스타일 적용
plt.show()







