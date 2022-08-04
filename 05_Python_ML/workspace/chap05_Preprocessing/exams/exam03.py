# -*- coding: utf-8 -*-
"""
문3) df 데이터프레임을 대상으로 다음과 같은 단계로 가변수(dummay variable)를 만드시오.  
"""

import pandas as pd 

## 데이터 생성 
data = {
    'gender' : ['male','female','male','male','female'],
    'height' : [175,165,180,169,188],
    'nation' : ['USA','Korea','China','Korea','Brazil'],
    'married' : [0,1,1,1,0]
}

df = pd.DataFrame(data)
df.info()
'''
Data columns (total 4 columns):
 #   Column   Non-Null Count  Dtype 
---  ------   --------------  ----- 
 0   gender   5 non-null      object
 1   height   5 non-null      int64 
 2   nation   5 non-null      object
 3   married  5 non-null      int64 
'''
 
# 단계1. 'nation' 칼럼 값의 Brazil -> Korea -> USA -> China 순서로 변경 
# 1) category형 변환
df.nation=df['nation'].astype('category')
# 2) 순서 변경
df.nation=df.nation.cat.set_categories(['Brazil','Korea','USA','China'])
df.nation # ['Brazil', 'Korea', 'USA', 'China']

## 단계2. 'married','gender','nation' 칼럼으로 k-1개 가변수 만들기 
new_df= pd.get_dummies(data=df.loc[:,['married','gender','nation']],drop_first=True)

# 단계3. 가변수의 원래 칼럼('married','gender','nation') 제거 후 확인
new_df=new_df.drop(['married'],axis=1)
new_df.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 5 entries, 0 to 4
Data columns (total 4 columns):
 #   Column        Non-Null Count  Dtype
---  ------        --------------  -----
 0   gender_male   5 non-null      uint8
 1   nation_Korea  5 non-null      uint8
 2   nation_USA    5 non-null      uint8
 3   nation_China  5 non-null      uint8
dtypes: uint8(4)
'''

