# -*- coding: utf-8 -*-
"""
step05_pivot_table.py

피벗테이블(pivot table) 
  - DF 객체를 대상으로 행과 열 그리고 교차 셀에 표시될 칼럼을 지정하여 만들어진 테이블 
   형식) pivot_table(DF, values='교차셀 칼럼',
                index = '행 칼럼', columns = '열 칼럼'
                ,aggFunc = '교차셀에 적용될 함수')  
"""

import pandas as pd 

path = r'C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML\data' # 경로 지정

# csv file 가져오기 
pivot_data = pd.read_csv(path + '/pivot_data.csv')
pivot_data.info()
'''
 0   year     8 non-null      int64  : 년도 
 1   quarter  8 non-null      object : 분기 
 2   size     8 non-null      object : 매출규모 
 3   price    8 non-null      int64  : 매출액 
'''
pivot_data
'''
   year quarter   size  price
0  2016      1Q  SMALL   1000
1  2016      1Q  LARGE   2000
2  2016      2Q  SMALL   1200
3  2016      2Q  LARGE   2500
4  2017      3Q  SMALL   1300
5  2017      3Q  LARGE   2200
6  2017      4Q  SMALL   2300
7  2017      4Q  LARGE   2800
'''

# 1. 핏벗테이블
ptable = pd.pivot_table(data=pivot_data, 
               values='price', 
               index=['year','quarter'], 
               columns='size', aggfunc='sum')
'''
size          LARGE  SMALL
year quarter              
2016 1Q        2000   1000
     2Q        2500   1200
2017 3Q        2200   1300
     4Q        2800   2300
'''


# 2. 핏벗테이블 시각화
import matplotlib.pyplot as plt

# 누적형 가로 막대 차트
ptable.plot(kind='barh', stacked=True)
plt.show()






