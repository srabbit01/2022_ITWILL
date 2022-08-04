'''
문2) weatherAUS.csv 파일을 시용하여 NB 모델을 생성하시오
  단계1> NaN 값을 가진 모든 row 삭제 
  단계2> 1,2,8,10,11,22,23 칼럼 제외 
  단계3> 변수 선택  : y변수 : RainTomorrow, x변수 : 나머지 변수(16개)
  단계4> 7:3 비율 train/test 데이터셋 구성   
  단계5> GaussianNB 모델 생성 
  단계6> model 평가 : accuracy, confusion matrix, classification_report
'''
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

path=r'C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML'
data = pd.read_csv(path+r'/data/weatherAUS.csv')
print(data.head())
print(data.info())

# 단계1> NaN 값을 가진 모든 row 삭제
data=data.dropna()
print(data.head())

# 조건2> 1,2,8,10,11,22,23 칼럼 제외 
cols = list(data.columns) # 전체 칼럼 추출 
colnames = [] # 사용할 칼럼 저장 

for i in range(24) :
    if i not in [0,1,7,9,10,21,22] : # 해당 칼럼 제외 
        colnames.append(cols[i]) 
    
new_data = data[colnames] # [[칼럼명]]: 중첩 리스트
print(new_data.info()) # x+y

# 단계3> 변수 선택  : y변수 : RainTomorrow, x변수 : 나머지 변수(16개)
y = new_data.RainTomorrow
X = new_data.iloc[:,:16]
X = StandardScaler().fit_transform(X)

# 단계4> 7:3 비율 train/test 데이터셋 구성
X_train, X_test, y_train, y_test = train_test_split(
     X, y, test_size=0.3, random_state=123)

# 단계5> GaussianNB 모델 생성 
model = GaussianNB().fit(X_train, y_train)

# 단계6> model 평가 : accuracy, confusion matrix, classification_report
y_pred=model.predict(X_test)
y_true=y_test

# 1) accuracy
model.score(X_test,y_test) # 0.8068661296509397

# 2) confusion matrix
con_mat=confusion_matrix(y_true,y_pred)
print(con_mat)
'''
[[3397  658]
 [ 349  810]]
'''

# 3) classification_report
report=classification_report(y_true,y_pred) 
print(report)
'''
              precision    recall  f1-score   support

          No       0.91      0.84      0.87      4055
         Yes       0.55      0.70      0.62      1159

    accuracy                           0.81      5214
   macro avg       0.73      0.77      0.74      5214
weighted avg       0.83      0.81      0.81      5214
'''