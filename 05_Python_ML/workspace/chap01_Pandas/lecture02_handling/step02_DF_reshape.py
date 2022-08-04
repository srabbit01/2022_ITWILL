# -*- coding: utf-8 -*-
"""
step02_DF_reshape.py

DataFrame 모양 변경 
"""
import pandas as pd 

path = r'C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML\data' # 경로 지정

buy = pd.read_csv(path + '/buy_data.csv')
print(buy.info())
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 22 entries, 0 to 21
Data columns (total 3 columns):
 #   Column       Non-Null Count  Dtype
---  ------       --------------  -----
 0   Date         22 non-null     int64
 1   Customer_ID  22 non-null     int64
 2   Buy          22 non-null     int64
'''

buy.head()
'''
       Date  Customer_ID  Buy
0  20150101            1    3 
1  20150101            2    4
2  20150102            1    2
3  20150101            2    3
4  20150101            1    2
'''
# 자료 모양
buy.shape # (22, 3) = (행, 열)
type(buy) # pandas.core.frame.DataFrame

# 1. [2차원] -> [1차원]  변경
buy_long = buy.stack() 
buy_long.shape # (66,) 
'''
0   Date           20150101
    Customer_ID           1
    Buy                   3
1   Date           20150101
    Customer_ID           2
                        ...
20  Customer_ID           1
    Buy                   9
21  Date           20150107
    Customer_ID           5
    Buy                   7
Length: 66, dtype: int64
'''
type(buy_long) # pandas.core.series.Series
buy_long.index # 색인 추출
'''
MultiIndex([( 0,        'Date'),
            ( 0, 'Customer_ID'),
            ( 0,         'Buy'),
            ( 1,        'Date'),
            ( 1, 'Customer_ID'),
            ( 1,         'Buy'),
            ...]
''' # 멀티 인덱스 생성 -> 2개 이상 인덱스
buy_long.values # 값 추출
# 0, 1, 3, ... 및 Customer_ID, Buy, Date = 색인
buy_long[0]['Date'] # 이름만은 사용 불가능

# 2. [1차원(wide)] -> [2차원(long)] 변경 
buy_wide = buy_long.unstack()
buy_wide.shape # (22, 3)

# 3. 전치행렬 (열축 <-> 행축)
buy_tran = buy.T
buy_tran.shape # (3, 22)
buy_tran

# 4. 중복 행 제거 
buy.duplicated() # 중복 행 여부 반환 
buy2 = buy.drop_duplicates() # 중복 행 제거
# 색인 제거하더라도 색인이 변경되지 않음 (유지)

# [추가] 2개 이상 중복된 경우
Date=[20150103,20150103]
CID=[1,1]
Buy=[5,5]
df=pd.DataFrame({'Date':Date,'Customer_ID':CID,'Buy':Buy})

# rbind
new_buy=pd.concat(objs=[buy,df],axis=0)
new_buy.duplicated()

new_buy2=new_buy.drop_duplicates()
new_buy2
# 중복 데이터 2개 이상인 경우 두번째 중복될 때 부터 True 출력

# 5. 특정 칼럼을 index 지정 
new_buy = buy.set_index('Date') # Date를 색인으로 지정
new_buy.columns # ['Customer_ID', 'Buy']
new_buy.index
'''
Int64Index([20150101, 20150101, 20150102, 20150101, 20150101, 20150103,
            20150102, 20150102, 20150103, 20150103, 20150103, 20150107,
            20150107, 20150103, 20150104, 20150104, 20150104, 20150105,
            20150106, 20150106, 20150107, 20150107],
           dtype='int64', name='Date')
'''
new_buy.head()
'''
          Customer_ID  Buy
Date                      
20150101            1    3
20150101            2    4
20150102            1    2
20150101            2    3
20150101            1    2
'''
new_buy.loc[20150101]
# 편리하게 날짜를 색인으로 검색 가능
'''
          Customer_ID  Buy
Date                      
20150101            1    3
20150101            2    4
20150101            2    3
20150101            1    2
'''

# 6. 특정 칼럼(Date)으로 데이터프레임 정렬

## 전체 칼럼 정렬
print(buy)
buy.sort_values('Date') # 오름차순
buy.sort_values('Date',ascending=False) # 내림차순

# 여러개 칼럼 기준
buy.sort_values(['Date','Customer_ID'],ascending=False) 
# 1차 정렬: Date -> 2차 정렬: Customer_ID (동일한 날짜에 대해 특정 칼럼 정렬)

## 툭정 칼럼만 정렬
buy['Date'].sort_values()
buy['Customer_ID'].sort_values()
buy.Customer_ID.sort_values(ascending=False)
