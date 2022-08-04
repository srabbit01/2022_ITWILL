# -*- coding: utf-8 -*-
"""
[과제] 타이타닉 데이터셋을 이용한 데이터 전처리와 로지스틱회귀모델 만들기
"""

import pandas as pd # csv file read 
from sklearn.preprocessing import minmax_scale # 최소-최대 정규화 
from sklearn.linear_model import LogisticRegression # model
pd.set_option('display.max_columns',15) # 최대 15개 칼럼 출력


# 데이터셋 카페에서 다운로드 : titanic_train.csv 

### 1단계 : train.csv 가져오기
path = r'C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML' # file path 
train = pd.read_csv(path+r"\data\titanic_train.csv")
train.info()
'''
 0   PassengerId  891 non-null    int64   -> 제거 
 1   Survived     891 non-null    int64   -> y변수 
 2   Pclass       891 non-null    int64  
 3   Name         891 non-null    object  -> 제거
 4   Sex          891 non-null    object 
 5   Age          714 non-null    float64
 6   SibSp        891 non-null    int64  
 7   Parch        891 non-null    int64  
 8   Ticket       891 non-null    object  -> 제거
 9   Fare         891 non-null    float64
 10  Cabin        204 non-null    object  
 11  Embarked     889 non-null    object
'''
train.shape # (891, 12)

# y변수 전처리 되어 있음 
train['Survived'].unique() # array([0, 1], dtype=int64)


### 2단계 : PassengerId, Name, Ticket 칼럼 제거 후 new_train 만들기 
new_train = train.drop(['PassengerId','Name','Ticket'], axis =1)
print(new_train.info())
type(new_train)

### 3단계 : 결측치 확인 및 처리 

# 1) new_train의 전체 칼럼 단위 결측치(NaN) 확인
new_train.isnull().sum()
'''
Survived      0
Pclass        0
Sex           0
Age         177
SibSp         0
Parch         0
Fare          0
Cabin       687
Embarked      2
'''

# 2) 결측치가 가장 많은 칼럼 제거 후 new_train에 반영     
new_train.dropna(subset=['Cabin'],inplace=True)
new_train.shape # (204, 9)

# 3) Age 칼럼의 결측치를 평균으로 대체 후 new_train에 반영 
new_train['Age']=new_train['Age'].fillna(new_train['Age'].mean(skipna=True))
new_train.isnull().sum()

# 4) Embarked 칼럼의 결측치를 가장 많이 출현한 값으로 대체 후 new_train에 반영 


new_train['Embarked']=new_train['Embarked'].fillna(new_train['Embarked'].mode().values[0])
new_train['Embarked'].isnull().any()

### 4단계 : 파생변수 만들기
'''
 나이(Age)가 10세 미만이고, 성별(Sex)이 여성인 경우 1, 
 아닌 경우 0로 파생변수('child_women') 만들기 
'''

# 1) 파생변수 만들기 & new_train에 추가 
child_women=[]
for i in range(len(new_train)):
    if new_train.Age.iloc[i]<10 and new_train.Sex.iloc[i]=='female':
        child_women.append(1)
    else:
        child_women.append(0)
        
## another solution
'''
result = (new_train.Age<10) & (new_train.Sex=='female') -> 조건에 만족 True, 아니면 False
# boolean(T/F) -> int(1/0)
new_train['child_women']=result.astype(int) -> True면 1, False면 0 반환
new_train['child_women'].value_counts()
print(new_train.columns)
'''

# 2) new_train에 추가된 파생변수의 빈도수 확인 
new_train['child_women']=child_women
new_train.info()
#  9   child_women  204 non-null    int64  
new_train.child_women.value_counts()
'''
0    200
1      4
'''

### 단계5 : X변수 전처리     

# 1) X변수 만들기 : new_train에서 'Survived' 칼럼을 제외한 X 만들기 
X=new_train.iloc[:,1:]

# 2) X의 object형 변수를 대상으로 k-1개 가변수 만들기(원핫 인코딩)
# (1) 2   Sex          204 non-null    object 
# (2) 7   Cabin        204 non-null    object 
# (3) 8   Embarked     202 non-null    object 
import pandas as pd
X=pd.get_dummies(data=X,columns=['Sex','Cabin','Embarked'],drop_first=True)
X.info()
'''
<class 'pandas.core.frame.DataFrame'>
Int64Index: 204 entries, 1 to 889
Columns: 155 entries, Pclass to Embarked_S
dtypes: float64(2), int64(4), uint8(149)
memory usage: 50.8 KB
'''

# 3) X의 Fare칼럼 이상치 처리 
'''
 - 정상범위를 넘는 이상치를 정상범위의 상한값으로 대체
 - 정상범위의 상한값 = 평균 + 3*표준편차
'''
import matplotlib.pyplot as plt
plt.boxplot(X['Fare']) # 상한값 이상 이상치 처리
max_val=X.Fare.mean()+3*X.Fare.std()
max_=X[(X.Fare>max_val)].index
X.loc[max_,'Fare']=max_val
plt.boxplot(X['Fare'])

# 4) X의 정규화
'''
 - X변수를 대상으로 최소-최대 정규화 
 - 정규화 결과에 칼럼명을 적용하여 X_train으로 데이터프레임 만들기  
'''
from sklearn.preprocessing import minmax_scale 
X_train=minmax_scale(X)


### 6단계 y변수 만들기  
'''
 - y변수 만들기 : 'Survived' 칼럼으로 y_train 변수 만들기
'''
y_train=new_train.iloc[:,0]

### 7단계 로지스틱회귀모델 생성 & model 평가 
'''
 - 로지스틱회귀모델 생성 : X_train, y_train 이용 
 - 결정계수를 이용하여 모델 평가하기   
'''
# 1) 모델 생성
model=LogisticRegression(random_state=123,max_iter=300,verbose=1)
model=model.fit(X=X_train,y=y_train) 

# 2) 예측 결과
y_pred=model.predict(X=X_train)
y_true=y_train

# 3) 모델 평가

# (1) 혼동행렬
from sklearn.metrics import confusion_matrix
con_mat=confusion_matrix(y_true,y_pred)
print(con_mat)
'''
[[ 60   8]
 [  6 130]]
'''

# (2) F-Measure
Precision=con_mat[1,1]/con_mat[:,1].sum()
Recall=con_mat[1,1]/con_mat[1,:].sum()
F_measure=2*((Precision*Recall)/(Precision+Recall))
print('F_measure =',F_measure)
# F_measure = 0.9489051094890512
# [해설] 분류 정확도가 높음을 알 수 있음

# (3) ROC 곡선
from sklearn.metrics import roc_curve
ytest_pred_proba=model.predict_proba(X=X_train)[:,1]
fpr,tpr,thresholds=roc_curve(y_true,ytest_pred_proba)
plt.plot(fpr,tpr,color='red',label='ROC Curve')
plt.plot([0,1],[0,1],color='blue',linestyle='--',label='AUC Line')
plt.legend()

##################################
## pickle file save
##################################
import pickle

# binary file save
path=r'C:/work/Crystal/DataAnalysis/[ITWILL]BigDataAnalysis_ExpertTraining/05. Python ML/workspace/subject'
file=open(path+r'\lr_model.pkl',mode='wb')
pickle.dump(model,file)
file.close()

# open saved file
file2=open(path+r'\lr_model.pkl',mode='rb')
model2=pickle.load(file2)
file2.close()
