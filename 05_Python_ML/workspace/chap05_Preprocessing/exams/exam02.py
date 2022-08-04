# 문2) mtcars 자료를 이용하여 다음과 같은 단계로 이상치를 처리하시오.

import pandas as pd 
import seaborn as sn # 데이터셋 로드 
pd.set_option('display.max_columns', 50) # 최대 50 칼럼수 지정
import matplotlib.pyplot as plt # boxplot 시각화 


# 데이터셋 로드 
data = sn.load_dataset('mpg')
data.info()
'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 398 entries, 0 to 397
Data columns (total 9 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   mpg           398 non-null    float64
 1   cylinders     398 non-null    int64  
 2   displacement  398 non-null    float64
 3   horsepower    392 non-null    float64
 4   weight        398 non-null    int64  
 5   acceleration  398 non-null    float64
 6   model_year    398 non-null    int64  
 7   origin        398 non-null    object 
 8   name          398 non-null    object 
dtypes: float64(4), int64(3), object(2)
'''
print(data)

# 단계1. boxplot으로 'acceleration' 칼럼 이상치 탐색 
plt.boxplot(data.acceleration) # 상한값, 하한값 모두 이상치 존재함을 확인
plt.show()

# 단계2. IQR 방식으로 이상치 탐색
data.describe()

Q1=data.describe().loc['25%','acceleration'] # 제1사분면
Q3=data.describe().loc['75%','acceleration'] # 제2사분면

# 1) IQR 수식 작성 
IQR=Q3-Q1

maxval=Q3+IQR*1.5
minval=Q1-IQR*1.5

# 2) 이상치 확인 
data[(data['acceleration']>maxval)|(data.acceleration<minval)]
'''
      mpg  cylinders  displacement  horsepower  weight  acceleration  
7    14.0          8         440.0       215.0    4312           8.5  
9    15.0          8         390.0       190.0    3850           8.5   
11   14.0          8         340.0       160.0    3609           8.0   
59   23.0          4          97.0        54.0    2254          23.5   
299  27.2          4         141.0        71.0    3190          24.8   
326  43.4          4          90.0        48.0    2335          23.7   
394  44.0          4          97.0        52.0    2130          24.6   
'''

# 단계3. 이상치 대체 : 정상범주의 하한값과 상한값 대체 
idx=data[(data['acceleration']>maxval)|(data.acceleration<minval)].index

# 상한값 대체
data.loc[data[data['acceleration']>maxval].index,'acceleration']=maxval

# 하한값 대체
data.loc[data[data.acceleration<minval].index,'acceleration']=minval

# 단계4. boxplot으로 'acceleration' 칼럼 이상치 처리결과 확인 
plt.boxplot(data.acceleration) # 이상치 사라진 것을 확인 가능


