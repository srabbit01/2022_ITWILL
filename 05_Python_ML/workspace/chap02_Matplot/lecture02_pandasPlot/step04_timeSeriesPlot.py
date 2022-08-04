'''
시계열 데이터 시각화 
'''

from datetime import datetime # 날짜형식 
import pandas as pd
import matplotlib.pyplot as plt

path = r'C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML\data' # 경로 지정

# 1. 날짜형식 수정(다국어)
cospi = pd.read_csv(path+"/cospi.csv")
print(cospi.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 247 entries, 0 to 246
Data columns (total 6 columns):
 #   Column  Non-Null Count  Dtype 
---  ------  --------------  ----- 
 0   Date    247 non-null    object -> 문자형 날짜 -> 날짜형으로 변환하기
 1   Open    247 non-null    int64 
 2   High    247 non-null    int64 
 3   Low     247 non-null    int64 
 4   Close   247 non-null    int64 
 5   Volume  247 non-null    int64
 '''
cospi.head()
Date = cospi['Date'] # cospi.Date 

# 날짜형 변환 : list + for
kDate = [datetime.strptime(date,"%d-%b-%y") for date  in  Date]
cospi['Date'] = kDate
print(cospi.head())
print(cospi.tail())

# 26-Feb-16 -> 2016-02-16

# 2. 시계열 데이터/시각화
cospi.info()
#  0   Date    247 non-null    datetime64[ns] -> 날짜형으로 변환

# 1개 칼럼 추세그래프 
cospi['High'].plot(title = "Trend line of High column")
plt.show()

# 2개 칼럼(중첩list) 추세그래프
cospi[['High', 'Low']].plot(color = ['r', 'b'],
        title = "Trend line of High and Low column")
plt.show() 


# index 수정 : Date 칼럼 이용  
new_cospi = cospi.set_index('Date')
print(new_cospi.info())
print(new_cospi.head())

# 날짜형 색인 
new_cospi.index #  DatetimeIndex(['2016-02-26', '2016-02-25',
print(new_cospi['2016']) # 년도 선택 
print(new_cospi['2016-02']) # 월 선택 
print(new_cospi['2016-02':'2016-01']) # 범위 선택 

# 2016년도 주가 추세선 시각화 
new_cospi_HL = new_cospi[['High', 'Low']]
new_cospi_HL['2016'].plot(title = "Trend line of 2016 year")
plt.show()

new_cospi_HL['2016-02'].plot(title = "Trend line of 2016 year")
plt.show()

new_cospi_HL['2015'].plot(title = "Trend line of 2015 year")
plt.show()

# 4. 이동평균(평활) : 지정한 날짜 단위 평균계산 -> 추세그래프 스무딩  
# 단위 별 평균을 구하여 좀 더 완만한 그래프 그리기

# 5일 단위 평균계산 : 평균계산 후 5일 시작점 이동 
# pd.Series.rolling(column, window=5,center=False).mean()
roll_mean5 = pd.Series.rolling(new_cospi.High,
                               window=5, center=False).mean()
print(roll_mean5)

roll_mean10 = pd.Series.rolling(new_cospi.High,
                               window=10, center=False).mean()
print(roll_mean10) # 좀더 곡선의 완만성이 높도록 만들기

roll_mean20 = pd.Series.rolling(new_cospi.High,
                               window=20, center=False).mean()
print(roll_mean20)

# 1) High 칼럼 시각화 
new_cospi['High'].plot(color = 'blue', label = 'High column')


# 2) rolling mean 시각화 : subplot 이용 - 격자 1개  
fig = plt.figure(figsize=(12,4))
chart = fig.add_subplot()
chart.plot(new_cospi['High'], color = 'blue', label = 'High column')
chart.plot(roll_mean5, color='red',label='5 day rolling mean')
chart.plot(roll_mean10, color='green',label='10 day rolling mean')
chart.plot(roll_mean20, color='orange',label='20 day rolling mean')
plt.legend(loc='best')
plt.show()















