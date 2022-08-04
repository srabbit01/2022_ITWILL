'''
외식업종 관련 dataset 분석

문4) food를 대상으로 다음과 같이 xgboost 모델을 생성하시오.
   <조건1> 6:4 비율 train/test set 생성 
   <조건2> y변수 ; 폐업_2년, x변수 ; 나머지 20개 
   <조건3> 중요변수에 대한  f1 score 출력
   <조건4> 중요변수 시각화  
   <조건5> accuracy와 model report 출력 
'''

import pandas as pd
from sklearn import model_selection, metrics 
from xgboost import XGBClassifier # xgboost 모델 생성 
from xgboost import plot_importance # 중요변수 시각화  

# 중요변수 시각화 
from matplotlib import pyplot
from matplotlib import font_manager, rc # 한글 지원
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)

# 외식업종 관련 data set
path=r"C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML"
food = pd.read_csv(path+"/data/food_dataset.csv", encoding="utf-8", thousands=',')

# 결측치 제거
food=food.dropna()  
print(food.info())
'''
<class 'pandas.core.frame.DataFrame'>
Int64Index: 68796 entries, 0 to 70170
Data columns (total 21 columns):
'''

food['폐업_2년'].value_counts()
'''
0    54284 : 폐업(x)
1    14512 : 폐업(o)
'''


#   <조건1> 6:4 비율 train/test set 생성 
#   <조건2> y변수 ; 폐업_2년, x변수 ; 나머지 20개 
X=food.iloc[:,:20]
y=food.iloc[:,20]

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.4,random_state=123)

# 모델 생성
model = XGBClassifier().fit(X = X_train, y = y_train)
print(model)

#   <조건3> 중요변수에 대한  f1 score 출력
fscore = model.get_booster().get_fscore()
print(fscore)

#   <조건4> 중요변수 시각화  
plot_importance(model)

#   <조건5> accuracy와 model report 출력 
from sklearn.metrics import accuracy_score, classification_report
y_pred=model.predict(X_test)

# 1) accuracy
accuracy_score(y_test,y_pred) # 0.7898542824957302

# 2) classification_report
report=classification_report(y_test,y_pred)
print(report)
'''
              precision    recall  f1-score   support

           0       0.80      0.98      0.88     21730
           1       0.50      0.08      0.14      5789

    accuracy                           0.79     27519
   macro avg       0.65      0.53      0.51     27519
weighted avg       0.74      0.79      0.73     27519
'''