
######################################
### 2. 이상치 처리 
######################################
"""
 이상치(outlier) 처리 : 정상범주에서 벗어난 값(극단적으로 크거나 작은 값) 처리  
  - 이상치 제거
  - 이상치 상수 대체
  - IQR(Inter Quentile Range) 방식으로 탐색과 대체  
"""

import pandas as pd 

### health_insurance.csv : 카페에서 다운로드  
path=r'C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML'
data = pd.read_csv(path+"/data/health_insurance.csv")
data.info()
'''
RangeIndex: 1338 entries, 0 to 1337
Data columns (total 7 columns):
 #   Column    Non-Null Count  Dtype  
---  ------    --------------  -----  
 0   age       1338 non-null   int64  
 1   sex       1338 non-null   object 
 2   bmi       1338 non-null   float64
 3   children  1338 non-null   int64  
 4   smoker    1338 non-null   object 
 5   region    1338 non-null   object 
 6   charges   1338 non-null   float64
'''
 
# 1-1. 이상치 탐색 : 범주형 
data.sex.unique() # array(['female', 'male']
data.smoker.unique() #  array(['yes', 'no']
data.region.unique() # array(['southwest', 'southeast', 'northwest', 'northeast']
# [결과] 이상 없음 

# 이상치 외 값 제거
data[data['sex'].isin(['female','male'])]

# plt.pie(data['sex'].value_counts())
# plt.hist(data.sex)

# 1-2. 이상치 탐색 : 숫자 변수 대상 요약통계량 (문자형 등 자동 제외)
des = data.describe()
print(des)
'''
               age          bmi     children       charges
count  1338.000000  1338.000000  1338.000000   1338.000000
mean     39.730194    30.524488     1.094918  13270.422265
std      20.224425     6.759717     1.205493  12110.011237
min      18.000000   -37.620000     0.000000   1121.873900
25%      27.000000    26.220000     0.000000   4740.287150
50%      39.000000    30.332500     1.000000   9382.033000
75%      51.000000    34.656250     2.000000  16639.912515
max     552.000000    53.130000     5.000000  63770.428010
[age] 변수: 최댓값 문제 발견
[bmi] 변수: 음수값 발견
'''
# 최대/최소 중 상식적으로 나올 수 없는 값이 존재하는지 확인하기

# 1-3. boxplot 이상치 탐색 
import matplotlib.pyplot as plt

plt.boxplot(data[['age']]) # 나이 변수 이상치  
plt.show()

plt.boxplot(data['bmi']) # 비만도 지수 변수 이상치  
plt.show()

plt.boxplot(data['charges']) # 의료비 변수 이상치  
plt.show()

# plt.boxplot(data) 불가능? -> 문자형/논리형 등 자동 제거 X
plt.boxplot(data[['age','bmi','children','charges']])

# 2. 이상치 제거 : 관측치가 적고, 해당 변수의 의미를 알고있는 경우 

# 1) bmi 변수 음수값 확인
data[data['bmi']<0] # 3명 확인
'''
    age     sex    bmi  children smoker     region     charges
16   52  female -30.78         1     no  northeast  10797.3362
48   60  female -24.53         0     no  southeast  12629.8967
82   22    male -37.62         1    yes  southeast  37165.1638
'''

# 2) bmi 변수 음수값 제거
new_data=data[data['bmi']>0]
new_data.info()
# Int64Index: 1335 entries, 0 to 1337

# 3. 이상치 대체 : 해당 변수의 의미를 알고있는 경우 

# 1) age 변수 100세 이상 확인
data[data['age']>100] # 3명 확인
'''
     age   sex     bmi  children smoker     region      charges
12   123  male  34.400         0     no  southwest   1826.84300
114  552  male  32.205         3     no  northeast  11488.31695
180  158  male  28.595         0     no  northwest  11735.87905
'''

# 2) age 변수 100세 이상 -> 100세로 대체
idx=new_data[new_data['age']>100].index # 행 index(위치)만 반환
idx # [12, 114, 180]
# 명칭 기반 index 값 대체
new_data.loc[idx,'age']=100
new_data.info()
# Int64Index: 1335 entries, 0 to 1337

# 3) 결과 확인
new_data.describe()
'''
              age          bmi     children       charges
count  1335.00000  1335.000000  1335.000000   1335.000000
mean     39.31985    30.662693     1.095880  13254.855876
std      14.31401     6.099756     1.206469  12105.743894
min      18.00000    15.960000     0.000000   1121.873900
25%      27.00000    26.302500     0.000000   4729.002375
50%      39.00000    30.400000     1.000000   9361.326800
75%      51.00000    34.687500     2.000000  16622.107580
max     100.00000    53.130000     5.000000  63770.428010
-> 객관적으로 판단된 이상치가 처리되었음을 확인 가능
-> charge의 경우, 통계적인 이상치 탐색을 통해 확인하기
'''

# 4. IQR방식 이상치 발견 및 대체 : 해당 변수의 의미를 모르는 경우 

# 1) IQR = 제3사분위수(Q3) - 제1사분위수(Q1)
des = data.describe()
Q1=des.loc['25%','age'] # 27
Q3=des.loc['75%','age'] # 51

IQR = Q3 - Q1 # 24

# 2) outlier 상한값/하한값 구하기
outlier_step=IQR*1.5 # 36

maxval=Q3+outlier_step # 87
minval=Q1-outlier_step # -9

print('상한값:',maxval,'하한값:',minval)

# 따라서, 정상범주: Q1-outlier_step ~ Q3+outlier_step

# 3) 이상치 확인
data[(data['age']<minval)|(data['age']>maxval)] # or
'''
     age   sex     bmi  children smoker     region      charges
12   123  male  34.400         0     no  southwest   1826.84300
114  552  male  32.205         3     no  northeast  11488.31695
180  158  male  28.595         0     no  northwest  11735.87905
'''

# 4) 이상치 대체: maxval 대체
idx=data[(data['age']<minval)|(data['age']>maxval)].index
data.loc[idx,'age']=maxval

data.loc[idx]
'''
      age   sex     bmi  children smoker     region      charges
12   87.0  male  34.400         0     no  southwest   1826.84300
114  87.0  male  32.205         3     no  northeast  11488.31695
180  87.0  male  28.595         0     no  northwest  11735.87905
'''
