# -*- coding: utf-8 -*-
"""
step01_DF_merge.py

1. DF 병합(merge)
   ex) DF1(id) + DF2(id) = DF3
2. DF 결합(concat)
   ex) DF1(6) + DF2(10) = DF3(16)
"""

import pandas as pd 
pd.set_option('display.max_columns', 100) # 콘솔에서 보여질 최대 칼럼 개수 

path = r'C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML\data' # 경로 지정

wdbc = pd.read_csv(path + '/wdbc_data.csv')
wdbc.info() # 32개의 칼럼 존재

cols = list(wdbc.columns) # 칼럼 이름 -> 리스트 형태로 변환

# DF1(16) + DF2(16)
DF1 = wdbc[cols[:16]] # 16개 
DF1.info()
DF1.shape # (569, 16)

DF2 = wdbc[cols[16:]] # 16개
DF2.info()
DF2.shape # (569, 16)

# 1. DF 병합(merge)
DF2['id'] = wdbc.id # id 칼럼 추가 

DF3 = pd.merge(left=DF1, right=DF2, on='id') # how = "inner" (기본)
DF3.shape # (569, 32)
DF3.info()

# 2. DF 결합(concat)
DF2 = wdbc[cols[16:]]
DF2.shape # (569, 16)

DF4 = pd.concat(objs=[DF1,DF2], axis = 1) # cbind
DF4.info()

# 3. Inner Join vs Outer Join
names=['hong','lee','park','kim']
ages=[35,20,45,35]
df1=pd.DataFrame({'age':ages,'name':names},columns=['name','age'])
df1
'''
   name  age
0  hong   35
1   lee   20
2  park   45
3   kim   35
'''

names2=['hong','lee','kim']
ages2=[35,20,35]
pays=[250,350,400]
df2=pd.DataFrame({'age':ages2,'name':names2,'pay':pays},columns=['name','age','pay'])
df2
'''
   name  age  pay
0  hong   35  250
1   lee   20  350
2   kim   35  400
'''

# 1) Inner Join: 양쪽 모두 자료가 있는 행의 경우만 병합
inner_df=pd.merge(left=df1,right=df2,on=['name','age'],how='inner') # 2개의 공통 칼럼 존재
inner_df
'''
   name  age  pay
0  hong   35  250
1   lee   20  350
2   kim   35  400
'''

# 2) Outer Join: 양쪽 중 한쪽 이상 자료가 있는 경우 병합
# 존재하지 않는 정보는 NaN 입력
outer_df=pd.merge(left=df1,right=df2,on=['name','age'],how='outer') # 2개의 공통 칼럼 존재
outer_df
'''
   name  age    pay
0  hong   35  250.0
1   lee   20  350.0
2  park   45    NaN -> 정보가 없어 결측치 생성
3   kim   35  400.0
'''

# 4. cbind vs rbind
# 1) cbind
cbind = pd.concat(objs=[df1,df2], axis = 1)
'''
   name  age  name   age    pay
0  hong   35  hong  35.0  250.0
1   lee   20   lee  20.0  350.0
2  park   45   kim  35.0  400.0
3   kim   35   NaN   NaN    NaN
'''
# 2) rbind
rbind = pd.concat(objs=[df1,df2], axis = 0)
'''
   name  age    pay
0  hong   35    NaN
1   lee   20    NaN
2  park   45    NaN
3   kim   35    NaN
0  hong   35  250.0
1   lee   20  350.0
2   kim   35  400.0
'''