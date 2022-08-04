# -*- coding: utf-8 -*-
"""
step04_ham_spam_classifier.py

NB vs SVM 성능평가 
"""

import numpy as np 
from sklearn.naive_bayes import MultinomialNB # nb model
from sklearn.svm import SVC  # svm model 
from sklearn.metrics import accuracy_score, confusion_matrix # 평가 
import time # 학습시간

path = r"C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML\data"
X_train, X_test, y_train, y_test = np.load(path + '/spam_train_test.npy', allow_pickle = True)
X_train.shape # (3901, 5000)
X_test.shape # (1673, 5000)

#######################
### NB model
#######################
print('NB model')
nb = MultinomialNB()

chktime = time.time()
model = nb.fit(X = X_train, y = y_train)
chktime = time.time() - chktime
print('NB model 실행 시간 : ', chktime)

y_pred = model.predict(X = X_test) # 예측치 
y_true = y_test # 관측치

acc = accuracy_score(y_true, y_pred)
print('NB 분류정확도 =', acc)

con_mat = confusion_matrix(y_true, y_pred)
print(con_mat)
print()
'''
NB model 실행 시간 :  0.06477189064025879 -> 속도 매우 빠름
NB 분류정확도 = 0.9719067543335326 -> 정확도가 상대적으로 높음
[[1435    0]
 [  47  191]]
'''

#######################
### SVM model
#######################
print('SVM model')
svm = SVC(kernel = 'linear')

chktime = time.time()
model2 = svm.fit(X = X_train, y = y_train)
chktime = time.time() - chktime
print('SVM model 실행 시간 : ', chktime)

y_pred2 = model2.predict(X = X_test)
acc = accuracy_score(y_true, y_pred2)
print('svm 분류정확도 =', acc)

con_mat = confusion_matrix(y_true, y_pred2)
print(con_mat)
'''
SVM model
SVM model 실행 시간 :  14.958300352096558 -> 속도가 NB model에 비해 느림
svm 분류정확도 = 0.9790794979079498 -> 정확도가 NB model에 비해 살짝 높음
[[1433    2]
 [  33  205]]
'''

# [결론]
# 훈련 속도는 NB model이 빠르나, 정확도는 SVM model이 높음
# 따라서, 자료의 양이 매우 많은 경우 SVM model이 불리