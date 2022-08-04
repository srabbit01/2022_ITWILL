# -*- coding: utf-8 -*-
"""
step07_dummy_encoding.py

1. 더미변수 만들기
   - 범주형(문자형 변수) -> 2진수(0,1)
   - 회귀분석에서 독립변수(X) 대상
   - ex) X(no,yes) -> 1 0/ 0 1 = one-hot-encoding
2. 레이블 인코딩
   - 범주형(문자형) 변수 -> 10진수(0~n-1)
   - 분류분석에서 종속변수(Y) 대상
   - 나온 순서대로 숫자 배정
   - ex) 서울(1), 경기도(2), 인천(3), ...
"""

import pandas as pd # csv file load
import matplotlib.pyplot as plt # 차트 시각화

# file 경로
path = r'C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML\data' # 경로 지정

insurance=pd.read_csv(path+'/insurance.csv') # 의료비 파일 불러오기
insurance.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 1338 entries, 0 to 1337
Data columns (total 7 columns):
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   age       1338 non-null   int64  
 1   sex       1338 non-null   object  -> 범주형(2개)
 2   bmi       1338 non-null   float64
 3   children  1338 non-null   int64  
 4   smoker    1338 non-null   object  -> 범주형(2개)
 5   region    1338 non-null   object  -> 범주형(4개)
 6   charges   1338 non-null   float64 = 의료비
dtypes: float64(2), int64(2), object(3)
memory usage: 73.3+ KB
'''

## 1. 더미변수 만들기: 2진수로 인코딩
insurance.smoker.unique() # ['yes', 'no']
insurance.smoker.value_counts()
'''
no     1064
yes     274
Name: smoker, dtype: int64
'''

# 1) dummy
# 자동으로 영문자 기준 오름차순 정렬
dummy=pd.get_dummies(data=insurance.smoker)
print(dummy) # one-hot encoding
'''
      no  yes
0      0    1 -> 해당되면 1, 해당되지 않으면 0으로 출력(2진수)
1      1    0
2      1    0
3      1    0 
4      1    0
  ..  ...
1333   1    0
1334   1    0
1335   1    0
1336   1    0
1337   0    1

[1338 rows x 2 columns]
'''
# formula = charges ~ age + bmi + children + smoker_no + smoker_yes ...


# 2) insurance + dummy = new_df
new_df=pd.concat(objs=[insurance,dummy],axis=1) # cbind
new_df.info()
'''
 7   no        1338 non-null   uint8  
 8   yes       1338 non-null   uint8 -> u: 부호없음, int: 정수형, 8: 8비트
 '''
new_df.head()

## 2. 레이블 인코딩: 10진수 인코딩
# 1) Labeling
from sklearn.preprocessing import LabelEncoder # class

encoder=LabelEncoder() # 생성자
encoder.fit(insurance.smoker) # data 적용
labels=encoder.transform(insurance.smoker) # 레이블 인코딩
labels # array([1, 0, 0, ..., 0, 0, 1])

# fit_transform: 동시에 적용 및 레이블 인코딩
# encoder.fit_transform(insurance.region) -> 한 번에 적용 및 레이블 인코딩 가능

# 2) 시각화(산점도): 포인트 color = 흡연유무
# 나이 vs 의료비
plt.scatter(x=insurance.age,y=insurance.charges,
            c=labels,marker='o')
# 나이가 증가할 수 록 의료비 증가 및 흡연자(노란색)가 더 많이 냄
plt.title('scatter plot')
plt.show()
# 흡연자(노란색)가 비흠연자(보라색)에 비해 더 많은 의료비 지출

# 칼럼 추가
insurance['smoker2']=labels 
insurance.iloc[:,4:]
'''
     smoker     region      charges  smoker2
0       yes  southwest  16884.92400        1
1        no  southeast   1725.55230        0
2        no  southeast   4449.46200        0
3        no  northwest  21984.47061        0
4        no  northwest   3866.85520        0
    ...        ...          ...      ...
1333     no  northwest  10600.54830        0
1334     no  northeast   2205.98080        0
1335     no  southeast   1629.83350        0
1336     no  southwest   2007.94500        0
1337    yes  northwest  29141.36030        1
'''
smoker_no=insurance[insurance.smoker2==0]
smoker_yes=insurance[insurance.smoker2==1]

smoker_no.shape # (1064, 8)
smoker_yes.shape # (274, 8)

# 비흡연자 의료비 평균
smoker_no.charges.mean() # 8434.268297856199
# 흡연자 의료비 평균
smoker_yes.charges.mean() # 32050.23183153285

## 3. 범주 3개 이상인 경우
insurance['region'].unique() # ['southwest', 'southeast', 'northwest', 'northeast']

# 1) 더미변수
dummy2=pd.get_dummies(data=insurance.region)
print(dummy2)
'''
      northeast  northwest  southeast  southwest
0             0          0          0          1 -> One-Hot Encoding
1             0          0          1          0
2             0          0          1          0
3             0          1          0          0
4             0          1          0          0
        ...        ...        ...        ...
'''

# 2) 레이블 인코딩
encoder=LabelEncoder() # 생성자
labels2=encoder.fit_transform(insurance.region) # 데이터 적용 및 인코딩
labels2 # array([3, 2, 2, ..., 2, 3, 1])

