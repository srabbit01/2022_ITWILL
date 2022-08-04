# -*- coding: utf-8 -*-
"""
step04_groupby
 
1. 집단변수(범주형 변수) 기준 subset 만들기 
2. 집단변수 기준 그룹 & 통계량 
3. 그룹 & 통계량 시각화
"""

import pandas as pd 
 
path = r'C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML\data' # 경로 지정

# 1. dataset load & 변수 확인
wine = pd.read_csv(path + '/winequality-both.csv')
print(wine.info())
'''
RangeIndex: 6497 entries, 0 to 6496
Data columns (total 13 columns):
0   type                  6497 non-null   object : 집단변수 (범주형 변수) -> label    
 :
12  quality               6497 non-null   int64 : 와인질 
'''    
# type: 와인의 유형 (문자형) -> 적으면 범주형, 많으면 일반 문자형 (식별용 변수는 범주형 X)
# int: 정수 -> 대부분 이산변수
# float: 실수 -> 대부분 연속변수

# 칼럼 공백 -> '_' 교체 
# 공백 혹은 점은 '_'로 교체
wine.columns = wine.columns.str.replace(' ', '_')
wine.head()
print(wine.info())

# 5개 변수 선택 : subset 만들기 
wine_df = wine.iloc[:, [0,1,4,11,12]] # 전체 행, 일부 열
print(wine_df.info())

## 특정 칼럼명 수정 
wine_df.columns # Index(['type', 'acidity', 'sugar', 'alcohol', 'quality'], dtype='object')

# 전체 칼럼명 수정
wine_df.columns=['type', 'fixed_acidity', 'residual_sugar', 'alcohol', 'quality'] # 반드시 전체 수정해야 함

# 특정 칼럼명 일부만 수정 수정
columns = {'fixed_acidity':'acidity', 'residual_sugar':'sugar'} 
wine_df = wine_df.rename(columns = columns) 
wine_df.info()
    
# 집단변수(범주형 변수) 확인 : 와인유형   
print(wine_df.type.unique()) # ['red' 'white']
print(wine_df.type.nunique()) # 범주 개수: 2
print(wine_df['type'].value_counts()) # 빈도수
'''
white    4898
red      1599
Name: type, dtype: int64
'''
# 이산 변수 확인
wine_df.quality.unique() # array([5, 6, 7, 4, 8, 3, 9], dtype=int64)

wine_df[['type','alcohol']][0:13]

# 2. 집단변수(범주형 변수) 기준 subset 만들기 
# DF[부울리언색인] - DF['column'] 관계식

# 1) 1개 집단 기준: 특정 집단 내 특정 범주 하나만 추출
red_wine = wine_df[wine['type']=='red'] # 레드 와인만 선택 
red_wine.shape # (1599, 6)
print(red_wine.info())
print(red_wine.head())
print(red_wine.tail())

white_wine = wine_df[wine['type']=='white']
white_wine.shape # (4898, 5)
print(white_wine.head()) # 원본의 인덱스 그대로 유지
print(white_wine.tail())

# 2) 2개 이상 집단 기준 : tyoe(red, white, blue) 3개 중 2개만 추출할 경우 - DF['column].isin('값')
two_wine_type = wine_df[wine_df['type'].isin(['red','white'])] # 레드, 화이트 와인 선택 
two_wine_type.head()

two_wine_type['type'].unique() 
two_wine_type['type'].value_counts()
'''
white    4898
red      1599
'''

# 3) 집단변수 기준 특정 칼럼 선택 : 1차원 구조
# loc: 명칭 기반 -> DF.loc['행','열']
# type 칼럼 내 red행 선택 후 quality 칼럼 값만 추출
red_wine_quality = wine.loc[wine['type']=='red', 'quality'] # 레드와인 품질  
red_wine_quality.shape # (1599,)
print(red_wine_quality)


# 3. 집단변수 기준 group & 통계량

# 1) 집단변수 1개 이용 그룹화 
# 형식) DF.groupby('집단변수')
type_grp = wine_df.groupby('type')
print(type_grp) # 정보만 제공 # 실제값 알 수 없음
type(type_grp)

# 그룹 빈도수 
print(type_grp.size()) # 각 집단별 빈도수 


# 그룹별 추출 : group객체.get_group('그룹이름')
red_df = type_grp.get_group('red')
white_df = type_grp.get_group('white')
red_df.shape # (1599, 5)
white_df.shape # (4898, 5)

    
# 집단별 통계량 : 숫자 변수만 대상
print(type_grp.sum()) 
print(type_grp.mean())
'''
        acidity     sugar    alcohol   quality
type                                          
red    8.319637  2.538806  10.422983  5.636023 # 신맛 높음
white  6.854788  6.391415  10.514267  5.877909 # 당도/알코올 농도/품질 높음
'''
# 평균 : white wide 알콜 높고, 품질 우수 


# 그룹의 특정 칼럼 기준 요약통계량 
print(type_grp['alcohol'].mean())
print(type_grp['alcohol'].describe())
print(type_grp.describe())


# 2) 집단변수 2개 이용 : 나머지 변수(11개)가 그룹 대상 
# 형식) DF.groupby(['집단변수1', '집단변수2']) # 1차 -> 2차 
wine_grp = wine_df.groupby(['type','quality']) # 2개 x 7개 = 최대 14  
print(wine_grp) # object info 

len(wine_grp) # 13

# 그룹 크기
wine_grp.size()
'''
1차 그룹 -> 2차 그룹 -> 빈도수
type   quality
red    3            10
       4            53
       5           681
       6           638
       7           199
       8            18
white  3            20
       4           163
       5          1457
       6          2198
       7           880
       8           175
       9             5
dtype: int64
'''
wine_grp.size().shape # (13,) = 범주수

# 4. 그룹 & 통계량 시각화
import matplotlib.pyplot as plt # 별칭

# 1) 그룹의 통계량 
# 지정된 그룹 변수를 제외한 모든 값이 칼럼
grp_mean=wine_grp.mean()
'''
                acidity     sugar    alcohol
type  quality                               
red   3        8.360000  2.635000   9.955000
      4        7.779245  2.694340  10.265094
      5        8.167254  2.528855   9.899706
      6        8.347179  2.477194  10.629519
      7        8.872362  2.720603  11.465913
      8        8.566667  2.577778  12.094444
white 3        7.600000  6.392500  10.345000
      4        7.129448  4.628221  10.152454
      5        6.933974  7.334969   9.808840
      6        6.837671  6.441606  10.575372
      7        6.734716  5.186477  11.367936
      8        6.657143  5.671429  11.636000
      9        7.420000  4.120000  12.180000
'''
# 특정 칼럼만 선택 가능
grp_mean[['sugar','alcohol']]
type(grp_mean[['sugar','alcohol']]) # pandas.core.frame.DataFrame

# DF.plot(kind=차트종류)
grp_mean[['sugar','alcohol']].plot(kind='bar') # kind='hist'/'bar'/'pie'/...
plt.show()
