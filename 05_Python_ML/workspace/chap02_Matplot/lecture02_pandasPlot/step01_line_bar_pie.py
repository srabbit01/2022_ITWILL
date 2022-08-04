# -*- coding: utf-8 -*-
"""
step01_line_bar_pie.py

Pandas 객체 이산변수 시각화 도구: kind='bar','pie','barh'
- bar: 세로막대
- barh: 가로막대
- pie: 파이 차트

형식) object.plot(kind='유형', 속성) 
- object: Series(1차원) 객체, DataFrame(2차원) 객체
- kind: 'bar','barh','pie','scatter','kde'(커널 밀도 곡선),'box'
- 속성: 제목, 축 이름, label, 범례 등

"""

import pandas as pd 
import numpy as np  
import matplotlib.pyplot as plt # 시각화: plt.show() 하기 위해

# 1. 기본 차트 시각화 

# 1) Series 객체 시각화 
ser = pd.Series(np.random.randn(10),
          index = np.arange(0, 100, 10))
ser # 1차원

ser.plot() # 선 그래프 
plt.show()

# 2) DataFrame 객체 시각화
df = pd.DataFrame(np.random.randn(10, 4),
                  columns=['one','two','three','fore'])

# 기본 차트 : 선 그래프 
df.plot()  
plt.show()

# kind = '유형' 지정하기
# 세로막대 차트 & 개별형 차트
df.plot(kind='bar',title='bar chart')
# 가로세로막대 & 누적형 차트
df.plot(kind='barh',title='barh chart',stacked=True)

# 2. dataset 이용 
path = r'C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML\data' # 경로 지정

tips = pd.read_csv(path + '/tips.csv')
tips.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 244 entries, 0 to 243
Data columns (total 7 columns):
 #   Column      Non-Null Count  Dtype  
---  ------      --------------  -----  
 0   total_bill  244 non-null    float64 -> 연속형
 1   tip         244 non-null    float64 -> 연속형
 2   sex         244 non-null    object 
 3   smoker      244 non-null    object 
 4   day         244 non-null    object 
 5   time        244 non-null    object 
 6   size        244 non-null    int64   -> 이산형
dtypes: float64(2), int64(1), object(4)
memory usage: 13.5+ KB
'''

# 행사 요일별 : 파이 차트 
cnt = tips['day'].value_counts() # 빈도수
'''
Sat     87
Sun     76
Thur    62
Fri     19
'''
cnt.plot(kind = 'pie')
plt.show()

# 범주형 변수 빈도수
tips['day'].unique() # ['Sun', 'Sat', 'Thur', 'Fri']
tips['size'].unique() # [2, 3, 4, 1, 6, 5]

# 교차분할표 생성
table=pd.crosstab(index=tips['day'],columns=tips['size'])
print(table)
'''
size  1   2   3   4  5  6
day                      
Fri   1  16   1   1  0  0
Sat   2  53  18  13  1  0
Sun   0  39  15  18  3  1
Thur  1  48   4   5  1  3
'''
type(table) # pandas.core.frame.DataFrame = 데이터프레임

tab_sub=table.loc[:,2:5] # = table.iloc[:,2:6]
tab_sub
'''
size   2   3   4  5
day                
Fri   16   1   1  0
Sat   53  18  13  1
Sun   39  15  18  3
Thur  48   4   5  1
'''
tab_sub.plot(kind='barh',stacked=True,title='day vs size plotting')
plt.show()
