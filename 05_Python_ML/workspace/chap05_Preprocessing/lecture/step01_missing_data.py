######################################
### 1. 결측치 처리
######################################

'''
x변수 결측치 처리 
y변수 레이블 인코딩: 문자형 or 숫자형 -> 더미변수(10진수) 
'''

import pandas as pd 
pd.set_option('display.max_columns', 50) # 최대 50 칼럼수 지정

# 암 진단 관련 데이터셋 
# 출처 : https://www.kaggle.com/uciml/breast-cancer-wisconsin-data?select=data.csv
# 캐글에서 다운로드한 암 진단 관련 데이터
### brastCencer.csv : 카페에서 다운로드 
path=r'C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML'
cencer = pd.read_csv(path+'/data/brastCencer.csv')
cencer.info()
'''
RangeIndex: 699 entries, 0 to 698
Data columns (total 11 columns):
 #   Column           Non-Null Count  Dtype 
---  ------           --------------  ----- 
 0   id               699 non-null    int64 -> 제거
 1   clump            699 non-null    int64 -> x 변수
 2   cell_size        699 non-null    int64 
 3   cell_shape       699 non-null    int64 
 4   adhesion         699 non-null    int64 
 5   epithlial        699 non-null    int64 
 6   bare_nuclei      699 non-null    object -> 숫자형 변환
 7   chromatin        699 non-null    int64 
 8   normal_nucleoli  699 non-null    int64 
 9   mitoses          699 non-null    int64 
 10  class            699 non-null    int64 -> y 변수
'''
# 대부분 id(식별자)/날짜 등은 사용하지 않기 떄문에 제거하기
print(cencer)
type(cencer)

# 기계 학습에서 사용되지 않는 칼럼 제거 (필요한 칼럼 선택)

# 1) 자료형 변환
cencer['bare_nuclei'] # 숫자 -> object
# object: 숫자형으로 보이나, 문자형, 특수문자 등 포함되어 있으면 우선 문자형으로 모두 변환

# 2) 재인코딩
cencer['class'].unique() # array([2, 4], dtype=int64)
# 2 -> 1, 4 -> 2로 재변환

# 1. 불필요한 변수 제거
dir(cencer)
df=cencer.drop('id',axis=1) # 열축 기준: id 칼럼 제거
# cencer.drop('id',axis=1, inplace=True) # 현재 객체 적용
# inplace: True면 현재 객체 지정하지 않아도 반영, False면 반영하지 않음
df.info()

# 2. x변수 숫자형 변환
# 1) 확인
df['bare_nuclei'].unique()
'''
array(['1', '10', '2', '4', '3', '9', '7', '?', '5', '8', '6'],
      dtype=object)
-> '?' 특수문자에 의해 모든 값 문자형 변환
'''
# '?' 결측치 처리 후, 숫자형으로 변환

# object -> int64: 특수문자, 문자 등 들어있으면 ValueError 발생 (목록 중 숫자가 아닌 값 포함 시)
# df['bare_nuclei'].astype('int64')

# 2) 결측치 대체/확인/처리

# df.drop(df['bare_nuclei']=='?',axis=0)

# (1) 결측치 대체: ? -> NaN
import numpy as np
df['bare_nuclei']=df['bare_nuclei'].replace('?',np.nan) # ? -> nan

# (2) 결측치 확인
df.isnull().any() # 전체 칼럼 단위 결측치 유무 반환 -> True/False
# bare_nuclei        True
df.isnull().sum() # 전체 칼럼 단위 결측치 개수 반환 -> 있으면 개수, 없으면 0 반환
# bare_nuclei        16

# (3) 결측치 처리

# (3-1) 결측치 제거: 지정 컬럼 
dropna=df.dropna(subset=['bare_nuclei'],axis=0) # subset 생략하면 전체 칼럼 대상
dropna.shape # (683, 10)
df.shape # (699, 10)
# 699 -> 683개로 16개의 행이 제거됨

# (3-2) 결측치 제거: 전체 컬럼
dropna2=df.dropna()
dropna2.shape # (683, 10)
dropna2['bare_nuclei'].dtype
# object -> int 자료형 변환
dropna2['bare_nuclei']=dropna2['bare_nuclei'].astype('int64')
dropna2['bare_nuclei'].dtype
dropna2.info()

# (3-3) 결측치 대체: 0 또는 상수
df2=df.copy() # 원본 복제

df2['bare_nuclei']=df2['bare_nuclei'].fillna(0) # DF['칼럼명'].fillna(상수)
df2.shape # (699, 10)

df2['bare_nuclei'].dtype # dtype('O')
# object -> int 자료형 변환
df2['bare_nuclei']=df2['bare_nuclei'].astype('int64')
df2['bare_nuclei'].dtype # dtype('int64')
df2.info()
'''
 0   clump            699 non-null    int64
 1   cell_size        699 non-null    int64
 2   cell_shape       699 non-null    int64
 3   adhesion         699 non-null    int64
 4   epithlial        699 non-null    int64
 5   bare_nuclei      699 non-null    int64
 6   chromatin        699 non-null    int64
 7   normal_nucleoli  699 non-null    int64
 8   mitoses          699 non-null    int64
 9   class            699 non-null    int64
 '''
 
# (3-4) 결측치 대체: 통계값(대표값)
df3=df.copy() # 내용 복사
# df3['bare_nuclei']=df3['bare_nuclei'].fillna(df3['bare_nuclei'].mean())
# 주의: NaN 존재하면 NaN 반환

df3['bare_nuclei']=df3['bare_nuclei'].fillna(0) # [1] 0 대체
df3['bare_nuclei']=df3['bare_nuclei'].astype('int64') # [2] 숫자형 변환
# [3] 0 -> 평균 대체
df3['bare_nuclei'].mean() # 평균: 3.463519313304721
df3['bare_nuclei']=df3['bare_nuclei'].replace(0,df3['bare_nuclei'].mean())
df3.info()
df3['bare_nuclei'].value_counts() # 3.463519      16

# 최빈수
df3['bare_nuclei'].mode().values[0] # 최빈수: 1.0 -> key=value 형식으로 반환
df3['bare_nuclei']=df3['bare_nuclei'].replace(0,df3['bare_nuclei'].mode().values[0])
# 중앙값
df3['bare_nuclei'].median() # 중앙값: 1.0
df3['bare_nuclei']=df3['bare_nuclei'].replace(0,df3['bare_nuclei'].median())

# 3. y 변수 레이블 인코딩(Label Encoding): 문자형/숫자형 -> 10진수 더미변수
# 10진수 변환(0~n-1)
from sklearn.preprocessing import LabelEncoder # class

encoder=LabelEncoder() # 생성자 -> 객체 생성
encoder.fit(df['class']) # dataset 반영
labels=encoder.transform(df['class']) # 레이블 인코딩
print(labels)

# 칼럼 추가
df['labels']=labels
df.info()
