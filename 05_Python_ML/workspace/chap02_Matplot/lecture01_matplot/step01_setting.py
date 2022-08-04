# -*- coding: utf-8 -*-
"""
step01_setting.py

 - matplotlib 사용법 
 - 한글/음수 부호 처리방법 
"""
import numpy as np # 수치 data 생성
import matplotlib.pyplot as plt# 시각화 도구


# 1. 차트 dataset 생성 
data = np.random.randn(100) # 패키지.모듈.함수(): N(0,1)
help(plt.plot)
# 2. 정규분포 시각화 
plt.plot(data,linestyle='dashed') # 기본 차트 생성 (기본: 선 그래프)
plt.title('vaisulize the normal dist') # 제목
plt.xlabel('index') # x축 이름
plt.ylabel('random number') # y축 이름
plt.show() # 차트 출력


# 한글과 음수 부호 지원 

# 차트에서 한글 지원 
plt.rcParams['font.family'] = 'Malgun Gothic' # 글꼴

# 음수 부호 지원 
import matplotlib
matplotlib.rcParams['axes.unicode_minus'] = False


# 3. 정규분포 시각화 : 한글 적용  
plt.plot(data)  # 시각화(선 그래프)
plt.title('정규분포 난수 시각화') 
plt.xlabel('색인')
plt.ylabel('난수')
plt.show() # 보이기 













