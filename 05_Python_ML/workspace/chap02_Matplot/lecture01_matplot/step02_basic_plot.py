# -*- coding: utf-8 -*-
"""
step02_basic_plot.py

 - 기본 차트 그리기 
"""

import numpy as np # 수치 data 생성 
import matplotlib.pyplot as plt # data 시각화 

# 차트에서 한글 지원 
plt.rcParams['font.family'] = 'Malgun Gothic'
# 음수 부호 지원 
import matplotlib
matplotlib.rcParams['axes.unicode_minus'] = False


# 1. 차트 자료 생성 
data = np.arange(-3, 7) # (start, stop)
print(data) # [-3 -2 -1  0  1  2  3  4  5  6]
len(data) # 10
'''
파이썬의 range와 비슷
range(start,stop): range(1,11) = 1 ~ 10
'''

# 2. 기본 차트 
help(plt.plot)
'''
plot(x, y)        # plot x and y using default line style and color
plot(x, y, 'bo')  # plot x and y using blue circle markers
plot(y)           # plot y using x as index array 0..N-1 # 색인
plot(y, 'r+')     # ditto, but with red plusses
'''
plt.plot(data) # 선색 : 파랑, 스타일 : 실선 
plt.title('선 색 : 파랑, 선 스타일 : 실선 ')
plt.show()


# 3. 색상 : 빨강, 선스타일(+)
plt.plot(data, 'r+')
plt.title('선 색 : 빨강, 선 스타일 : +')
plt.show()

# 4. x축, y축 선 스타일과 색상
data2=np.random.randn(10) # 정규 분포를 따르는 임의의 난수 10개 생성
plt.plot(data,data2) # plot(x,y)
plt.show()

# 5. color, marker 사용
plt.plot(data,data2,'bo')
plt.show()

