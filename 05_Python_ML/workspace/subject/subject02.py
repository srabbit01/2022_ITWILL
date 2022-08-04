# -*- coding: utf-8 -*-
"""
[과제2] 로지스틱회귀모델을 테스트셋(test) 적용하여 각 관측별로 
        생존(1) 확률을 콘솔에 출력하고, csv file로 저장하시오.
        
  0. [과제1]에서 생성한 로지스트회귀모델을 pickle 파일로 저장하기 
     -> python-I > chap08_FileIO 참고 
   
  1. 테스트셋(test)을 대상으로 불필요한 칼럼제거 
  2. 결측치(NaN) 확인 후 평균으로 대체 
  3. 파생변수(child_women) 추가     
  4. X변수 전처리 : 훈련셋(train) X변수와 동일함 
  5. pickle 파일로 저장한 로지스틱회귀모델 가져오기(load)
  6. y 예측치 구하기 : 로지스틱회귀모델을 테스트셋의 X변수에 적용      
  7. y 예측치를 콘솔 출력(콘솔 출력 예시 참고)
  8. 콘솔에 출력된 결과와 동일하게 csv file 저장  
  
  <콘솔 출력 예시>
  # 생존 확률만 출력됨
         y_pred
  0    0.095280
  1    0.493321
  2    0.154807
  3    0.083254
  4    0.561610
  ..        ...
  413  0.079458
  414  0.951034
  415  0.070681
  416  0.079458
  417  0.092423
"""

import pandas as pd
from sklearn.preprocessing import minmax_scale

# titanic_test.csv : 카페에서 다운로드 

### 테스트셋 가져오기 
path=r'C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML'
test = pd.read_csv(path+r"\data\titanic_test.csv")
print(test.info())
'''
 0   PassengerId  418 non-null    int64   - 제거 
 1   Pclass       418 non-null    int64  
 2   Name         418 non-null    object  - 제거 
 3   Sex          418 non-null    object  - 더미변수 
 4   Age          332 non-null    float64
 5   SibSp        418 non-null    int64  
 6   Parch        418 non-null    int64  
 7   Ticket       418 non-null    object  - 제거 
 8   Fare         417 non-null    float64
 9   Cabin        91 non-null     object  - 제거 
 10  Embarked     418 non-null    object  - 더미변수 
 ※ 테스트셋에는 y변수 없음 
'''

# 1. 테스트셋(test)을 대상으로 불필요한 칼럼제거 
test=test.drop(['PassengerId','Name','Ticket','Cabin'],axis=1)
test.info()

# 2. 결측치(NaN) 확인 후 평균으로 대체 
test.isnull().any()
'''
Pclass      False
Sex         False
Age          True
SibSp       False
Parch       False
Fare         True
Embarked    False
'''
test['Age']=test['Age'].fillna(test['Age'].sum(skipna=True))
test['Fare']=test['Fare'].fillna(test['Fare'].sum(skipna=True))

# 3. 파생변수(child_women) 추가    
'''
 나이(Age)가 10세 미만이고, 성별(Sex)이 여성인 경우 1, 
 아닌 경우 0로 파생변수('child_women') 만들기 
''' 
# train과 test의 변수(칼럼) 이름은 동일해야 함
child_women=(test.Age<10) & (test.Sex=='Female')
test['child_women']=child_women.astype(int)
test.info()

# 4. X변수 전처리 : 훈련셋(train) X변수와 동일함 
path=r'C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML'
train = pd.read_csv(path+r"\data\titanic_train.csv")
train.info()

# (1) 불필요한 칼럼 제거
train=train.drop(['PassengerId','Name','Ticket','Cabin'],axis=1)

# (2) 결측치(NaN) 확인 후 평균으로 대체 
train.isnull().any()
train['Age']=train['Age'].fillna(train['Age'].sum(skipna=True))
train['Fare']=train['Fare'].fillna(train['Fare'].sum(skipna=True))
train['Embarked']=train['Embarked'].fillna(train['Embarked'].mode().values[0])

# (3) 파생변수(child_women) 추가    
child_women2=(train.Age<10) & (train.Sex=='Female')
train['child_women']=child_women2.astype(int)
train.info()
X_train=train.iloc[:,1:]
X_train.info()
y_train=train.iloc[:,0]

# (4) 범주형 문자변수 -> 숫자형 변수로 원핫 인코딩
from sklearn.linear_model import LogisticRegression
import pandas as pd
X_train=pd.get_dummies(data=X_train,columns=['Sex','Embarked'],drop_first=True)

# (5) 이상치 상한값으로 대체
max_val=X_train.Fare.mean()+3*X_train.Fare.std()
max_=X_train[(X_train.Fare>max_val)].index
X_train.loc[max_,'Fare']=max_val
plt.boxplot(X_train['Fare'])

# (6) 정규화
from sklearn.preprocessing import minmax_scale 
X_train=minmax_scale(X_train)

# 5. pickle 파일로 저장한 로지스틱회귀모델 가져오기(load)
import pickle
path=r'C:/work/Crystal/DataAnalysis/[ITWILL]BigDataAnalysis_ExpertTraining/05. Python ML/workspace/subject'
file=open(path+r'\lr_model.pkl',mode='rb')
model2=pickle.laod(file)
file.close()

# 6. y 예측치 구하기 : 로지스틱회귀모델을 테스트셋의 X변수에 적용      
model=LogisticRegression(random_state=123,max_iter=300,verbose=1)
model=model.fit(X=X_train,y=y_train) 

# 7. y 예측치를 콘솔 출력(콘솔 출력 예시 참고)

# (1) 범주형 문자변수 -> 숫자형 변수로 원핫 인코딩
from sklearn.linear_model import LogisticRegression
import pandas as pd
X_test=pd.get_dummies(data=X_test,columns=['Sex','Embarked'],drop_first=True)

# (2) 이상치 상한값으로 대체
max_val=X_test.Fare.mean()+3*X_test.Fare.std()
max_=X[(X_test.Fare>max_val)].index
X_test.loc[max_,'Fare']=max_val
plt.boxplot(X_test['Fare'])

# (3) 정규화
from sklearn.preprocessing import minmax_scale 
X_test=minmax_scale(X_test)

# (4) y 예측치 출력
y_pred=model.predict(X_test)
y_predD=pd.DataFrame(y_pred,colums=['y_pred'])
print(y_predD)
'''
         y_pred
  0    0.095280
  1    0.493321
  2    0.154807
  3    0.083254
  4    0.561610
  ..        ...
  413  0.079458
  414  0.951034
  415  0.070681
  416  0.079458
  417  0.092423
  '''

# 8. 콘솔에 출력된 결과와 동일하게 csv file 저장  
result=X_test.copy()
result=pd.DataFrame(result,columns=test.columns)
result['Survived']=y_pred
result.info()
# 파일 저장
path=r'C:/work/Crystal/DataAnalysis/[ITWILL]BigDataAnalysis_ExpertTraining/05. Python ML/workspace/subject'
result.to_csv(path+'/titanic_test_LogisRegressResult.csv',index=False)
