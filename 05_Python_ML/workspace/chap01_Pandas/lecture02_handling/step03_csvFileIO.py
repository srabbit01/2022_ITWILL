# -*- coding: utf-8 -*-
"""
step03_csvFileIO.py

1. csv file read
2. csv file write
"""
import pandas as pd 
path = r'C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML\data' # 경로 지정

# 1. csv file read

# 1) 칼럼명이 없는 경우 
st = pd.read_csv(path + '/student.csv', header=None)
# header=None: 칼럼명이 없는 경우

# 칼럼명 수정 
col_names = ['sno','name','height','weight']
st.columns = col_names
print(st)

# 2) 칼럼명 특수문자(.) or 공백 
iris = pd.read_csv(path + '/iris.csv')
print(iris.info())

# iris.Sepal.Length # AttributeError

# 점(.) -> 언더바(_) 교체 
iris.columns = iris.columns.str.replace('.','_')
iris.info() # Sepal_Length
iris.Sepal_Length

# 3) 특수구분자(tab키), 천단위 콤마 
# pd.read_csv('file', delimiter='\t', thousands=',')

# 2. data 처리: 파생변수 추가
'''
비만도 지수(bmi)
bmi = 몸무게/(키**2)
몸무게 단위: kg
키 단위: cm -> m
'''
bmi=st.weight/((st.height*0.01)**2)
st['bmi']=bmi
st.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 4 entries, 0 to 3
Data columns (total 5 columns):
 #   Column  Non-Null Count  Dtype  
---  ------  --------------  -----  
 0   sno     4 non-null      int64  
 1   name    4 non-null      object 
 2   height  4 non-null      int64  
 3   weight  4 non-null      int64  
 4   bmi     4 non-null      float64
dtypes: float64(1), int64(3), object(1)
memory usage: 288.0+ bytes
'''
st

# bmi 결과 확인
'''
bmi 지수
- 18 ~ 23: 정상
- 23 이상: 비만
- 18 미만: 마름
label 파생 변수 만들기: normal, fat, thin
'''
label=[]
for b in st.bmi:
    if 18<=b and b<23: # 정상
        label.append('normal')
    elif b>=23: # 비만
        label.append('fat')
    else: # 마름
        label.append('thin')
st['label']=label
st
'''
   sno  name  height  weight        bmi   label
0  101  hong     175      65  21.224490  normal
1  201   lee     185      85  24.835646     fat
2  301   kim     173      60  20.047446  normal
3  401  park     180      70  21.604938  normal
'''
    
# 3. csv file write
# index = None : 행 이름 제외 
st.to_csv(path + '/st_info.csv', index = None, encoding='utf-8')

st_new = pd.read_csv(path  + '/st_info.csv', encoding='utf-8')
print(st_new)






















