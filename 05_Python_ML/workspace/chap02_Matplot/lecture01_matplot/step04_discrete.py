# -*- coding: utf-8 -*-
"""
step04_discrete.py

 - 이산형 변수 시각화 : 막대차트, 원차트 
"""
import numpy as np # 수치 data 생성 
import matplotlib.pyplot as plt # data 시각화 

# 차트에서 한글 지원 
plt.rcParams['font.family'] = 'Malgun Gothic'
# 음수 부호 지원 
import matplotlib
matplotlib.rcParams['axes.unicode_minus'] = False


# 차트 자료 생성 
data = [127, 90, 201, 150, 250] # 국가별 수출현황 
idx = np.arange(len(data)) # 0 ~ 4: 색인
labels = ['싱가폴','태국','한국','일본','미국'] 

# 1. 세로막대 
plt.bar(x = idx+2000, height=data) # x:년도, y:수출현황 
plt.title('국가별 수출현황')
plt.xlabel('년도별')
plt.ylabel('수출현황(단위 : 달러)')
plt.show()


# 2. 가로막대 
plt.barh(y= idx+2000, width = data)# x:년도, y:수출현황 
plt.title('국가별 수출현황')
plt.xlabel('수출현황(단위 : 달러)')
plt.ylabel('년도별')
plt.show()


# 3. 원차트
plt.pie(x = data, labels = labels)
plt.show()














