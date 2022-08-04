# -*- coding: utf-8 -*-
"""
step03_DecisionTree_dummy.py

Tree 계열 모델에서 문자형 변수 인코딩   
 - x변수: k개 더미변수(one-hot encoding) -> 2진수
   cf) 회귀계열: k-1개 더미변수, 트리계열: k개 더미변수
 - y변수: label encoding 0-> 10진수
"""

import pandas as pd  
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


# 1. 화장품 데이터(skin.csv) 가져오기 
path=r"C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML"
df = pd.read_csv(path+r"\data\skin.csv")
df.info()
'''
RangeIndex: 30 entries, 0 to 29
Data columns (total 7 columns):
 #   Column       Non-Null Count  Dtype 
---  ------       --------------  ----- 
 0   cust_no      30 non-null     int64  -> 제외 
 1   gender       30 non-null     object -> F/M   : x변수  
 2   age          30 non-null     int64  -> 연속형 
 3   job          30 non-null     object -> YES/NO
 4   marry        30 non-null     object -> YES/NO
 5   car          30 non-null     object -> YES/NO
 6   cupon_react  30 non-null     object -> YES/NO : y변수(화장품 구입여부) 
'''
   

#  범주형 변수의 범주 확인  
def category(df, col_names) :
    for name in col_names :
        print('{0} -> {1}'.format(name, df[name].unique()))

category(df, list(df.columns[1:])) # cust_no 제외 
'''
gender -> ['male' 'female']
age -> [30 20 40]
job -> ['NO' 'YES']
marry -> ['YES' 'NO']
car -> ['NO' 'YES']
cupon_react -> ['NO' 'YES']
'''
 
# 2. X, y변수 선택 
X = df.drop(['cust_no', 'cupon_react'], axis = 1) # 사용한 변수와 y변수 제거 
y = df['cupon_react'] 

###########################
## 인코딩 과정
###########################
# 1) 독립변수(X) one-hot encoding
import pandas as pd
X=pd.get_dummies(data=X,drop_first=False)
X.info()
'''
 #   Column         Non-Null Count  Dtype
---  ------         --------------  -----
 0   age            30 non-null     int64
 1   gender_female  30 non-null     uint8
 2   gender_male    30 non-null     uint8
 3   job_NO         30 non-null     uint8
 4   job_YES        30 non-null     uint8
 5   marry_NO       30 non-null     uint8
 6   marry_YES      30 non-null     uint8
 7   car_NO         30 non-null     uint8
 8   car_YES        30 non-null     uint8
 '''
# 독립변수(X)가 5개 -> 9개로 증가

# 2) 종속변수(y) label encoding
from sklearn.preprocessing import LabelEncoder
y=LabelEncoder().fit_transform(y)
print(y)
'''
[0 0 0 0 0 0 0 1 1 1 0 0 0 1 1 0 1 0 0 1 1 0 1 0 1 0 1 0 1 1]
'''

# 칼럼 이름 추출
x_names = list(X.columns) # x변수명 추출 : 중요변수 시각화에 이용 
print(x_names)
# ['age', 'gender_female', 'gender_male', 'job_NO', 'job_YES', 'marry_NO', 'marry_YES', 'car_NO', 'car_YES']

# 3. DecisionTree 분류기 
                                                                                     
# 훈련 데이터 75, 테스트 데이터 25으로 나눈다. 
X_train, X_test, y_train, y_test = train_test_split(
    X, y, random_state = 123)


# 의사결정트리 분류기
model = DecisionTreeClassifier().fit(X_train, y_train) 
# ValueError: 만일, 독립변수(X) 혹은 종속변수(y) 내 문자가 존재하는 경우 오류 발생
# -> 즉, 제대로 인코딩 되지 않은 경우

# 4. 중요 변수 
print("중요도 : \n{}".format(model.feature_importances_))
'''
[0.32806604 0.03459119 0.10377358 0.10377358 0.13836478 0.2132015
 0.         0.         0.07822932]
'''

# 중요변수 시각화 : age > job_YES > marry_YES 
import matplotlib.pyplot as plt 

x_size = X.shape[1] # x변수 개수 
 
# 가로막대 차트: 변수가 많은 경우에는 시각화하기
plt.barh(range(x_size), model.feature_importances_) # x축: 중요도, y축: 칼럼 이름
# y축 눈금 : x변수명 적용  
plt.yticks(range(x_size), x_names)
plt.xlabel('feature_importances')
plt.show()
# 인코딩된 칼럼의 경우, 동일 칼럼에서 추출된 범주의 점수가 높으면
# 영향력이 더 높음을 의미

# 5. 모델 평가  
y_pred= model.predict(X_test) # 예측치

# 정확도 확인하는 코드 
accuracy = accuracy_score( y_test, y_pred)
print( accuracy) # 0.875 

# 혼동 행렬
conf_matrix= confusion_matrix(y_test, y_pred)
print(conf_matrix)    

# 정밀도 , 재현율, f1 score 확인 
report = classification_report(y_test, y_pred)
print(report)

