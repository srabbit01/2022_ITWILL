######################################
### 3. 데이터 인코딩 
######################################

"""
데이터 인코딩 : 머신러닝 모델에서 범주형변수를 대상으로 숫자형의 목록으로 변환해주는 전처리 작업
 - 방법 : 레이블 인코딩(label encoding), 원-핫 인코딩(one-hot encoding)   
 - 레이블 인코딩(label encoding) : y변수 대상 10진수로 인코딩 or 트리모형의 x변수 인코딩
 - 원-핫 인코딩(one-hot encoding) : 회귀모형, SVM 계열의 x변수를 2진수(더미변수)로 인코딩 
   -> 회귀모형에서는 인코딩값이 가중치로 적용되므로 원-핫 인코딩(더미변수)으로 변환  
"""


import pandas as pd 

### skin.csv : 카페에서 다운로드
path=r'C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML'
data = pd.read_csv(path+r"\data\skin.csv")
data.info()
'''
RangeIndex: 30 entries, 0 to 29
Data columns (total 7 columns):
 #   Column       Non-Null Count  Dtype 
---  ------       --------------  ----- 
 0   cust_no      30 non-null     int64  -> 변수 제외 
 1   gender       30 non-null     object -> x변수 
 2   age          30 non-null     int64 
 3   job          30 non-null     object
 4   marry        30 non-null     object
 5   car          30 non-null     object
 6   cupon_react  30 non-null     object -> y변수(쿠폰 반응) 
''' 

## 1. 변수 제거 : cust_no
df = data.drop('cust_no', axis = 1) # 열축 기준 제거
# axis 생략 시, axis=0 지정
df.info()

### 2. 레이블 인코딩 : y변수 또는 트리모델 계열의 x변수 인코딩  
# 결과가 10진수로 인코딩되기 때문에 숫자의 의미를 가짐
from sklearn.preprocessing import LabelEncoder # class 인코딩 도구 

# 1) 쿠폰 반응 범주 확인 
df.cupon_react.unique() # array(['NO', 'YES'], dtype=object) 

# 2) 인코딩
encoder = LabelEncoder() # encoder 객체 
# fit_transform: fit() + transform()
label = encoder.fit_transform(df['cupon_react']) # data 반영 
label # 기본 Label: 영문자 오름차순
'''
array([0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0,
       1, 0, 1, 0, 1, 0, 1, 1])
'''

# 3) 칼럼 추가 
df['label'] = label # y변수로 사용하기 위해 추가
df.info()
# cust_no 삭제 -> label 추가
'''
 6   label        30 non-null     int32 
 '''

### 3. 원-핫 인코딩 : 회귀모델 계열의 x변수 인코딩  

# 1) k개 목록으로 가변수(더미변수) 만들기 
df_dummy = pd.get_dummies(data=df) # 기준변수 포함 
# 숫자가 아닌 것 대상   
df_dummy.info()
'''
 #   Column           Non-Null Count  Dtype
---  ------           --------------  -----
 0   age              30 non-null     int64
 1   label            30 non-null     int32
 2   gender_female    30 non-null     uint8
 3   gender_male      30 non-null     uint8
 4   job_NO           30 non-null     uint8
 5   job_YES          30 non-null     uint8
 6   marry_NO         30 non-null     uint8
 7   marry_YES        30 non-null     uint8
 8   car_NO           30 non-null     uint8
 9   car_YES          30 non-null     uint8
 10  cupon_react_NO   30 non-null     uint8
 11  cupon_react_YES  30 non-null     uint8
dtypes: int32(1), int64(1), uint8(10)
'''
# 모든 범주에 대한 칼럼 생성

# 2) k-1개 목록으로 가변수(더미변수) 만들기   
df_dummy2 = pd.get_dummies(data=df, drop_first=True) # 기준변수 제외(권장)
df_dummy2.info()
'''
 #   Column           Non-Null Count  Dtype
---  ------           --------------  -----
 0   age              30 non-null     int64
 1   label            30 non-null     int32
 2   gender_male      30 non-null     uint8
 3   job_YES          30 non-null     uint8
 4   marry_YES        30 non-null     uint8
 5   car_YES          30 non-null     uint8
 6   cupon_react_YES  30 non-null     uint8
 '''
# 기본 범주(칼럼)을 제외한 범주에 대한 칼럼 생성 
# 생성되는 칼럼의 개수 감소(적음)
# 숫자형/날짜형 변수는 자동으로 생략됨

# 3) 숫자형 변수를 대상으로 가변수 만들기
df_dummy3=pd.get_dummies(data=df, drop_first=True,
                         columns=['label','gender','job']) 
df_dummy3.info()
'''
 #   Column       Non-Null Count  Dtype 
---  ------       --------------  ----- 
 0   age          30 non-null     int64 
 1   marry        30 non-null     object
 2   car          30 non-null     object
 3   cupon_react  30 non-null     object
 4   label_1      30 non-null     uint8 
 5   gender_male  30 non-null     uint8 
 6   job_YES      30 non-null     uint8 
 '''
 
##########################################
## 가변수 (Base) 변경하기
##########################################
import seaborn as sn # dataset load

iris=sn.load_dataset('iris')
iris.info()
'''
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   sepal_length  150 non-null    float64
 1   sepal_width   150 non-null    float64
 2   petal_length  150 non-null    float64
 3   petal_width   150 non-null    float64
 4   species       150 non-null    object
dtypes: float64(4), object(1)
'''
# 카테고리형: 레벨(순서) 변경 가능

iris_dummy=pd.get_dummies(data=iris,columns=['species'],drop_first=True)
iris_dummy.info()
'''
 #   Column              Non-Null Count  Dtype  
---  ------              --------------  -----  
 0   sepal_length        150 non-null    float64
 1   sepal_width         150 non-null    float64
 2   petal_length        150 non-null    float64
 3   petal_width         150 non-null    float64
 4   species_versicolor  150 non-null    uint8  
 5   species_virginica   150 non-null    uint8  
'''

# 1개 -> 범주-1인 2개의 칼럼 생성 (기본 칼럼 Species 제거)
iris_dummy.iloc[:,3:].head()

# object -> category형 변환
iris['species'].value_counts()
'''
versicolor    50
virginica     50
setosa        50
'''

# 1) category로 자료형 변환
iris.species=iris['species'].astype('category')
iris.info() #  4   species       150 non-null    category
iris.species # Categories (3, object): ['setosa', 'versicolor', 'virginica']

# 2) base 순서 변경: versicolor > virginica > setosa 순서
iris.species=iris['species'].cat.set_categories(['versicolor','virginica','setosa'])
iris.species # Categories (3, object): ['versicolor', 'virginica', 'setosa']

# 3) 순서 변경 확인
# 전: ['setosa', 'versicolor', 'virginica']
# 후: ['versicolor', 'virginica', 'setosa']