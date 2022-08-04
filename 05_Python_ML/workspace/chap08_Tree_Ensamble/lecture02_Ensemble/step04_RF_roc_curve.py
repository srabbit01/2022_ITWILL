'''
step04_RF_roc_curve.py
'''

from sklearn.datasets import load_breast_cancer # dataset
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, roc_curve,roc_auc_score
import matplotlib.pyplot as plt
 

# 1. dataset load 
X, y = load_breast_cancer(return_X_y= True)
y # 0 or 1

# 2. split into train/test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=2)
X_test.shape # (285, 30)
 
# 3. model
model = RandomForestClassifier().fit(X_train, y_train)


# 4. predict probabilities
y_pred = model.predict(X_test) # class 예측

# accuracy scores
acc = accuracy_score(y_test, y_pred)
print('accuracy score = %.5f' % (acc))
# accuracy score = 0.95789

# 확률 예측 
y_pred_probs = model.predict_proba(X_test)
y_pred_probs.shape # (285, 2)
y_pred_probs

# positive 예측결과 추출 
positive_probs = y_pred_probs[:, 1] 
 
 
# 5. calculate roc curves
fpr, tpr, _ = roc_curve(y_test, positive_probs)
'''
   1   0
1  TP FN
0  FP TN

- TPR: 실제 양성 -> 모델 양성 = TP / (TP + FN)
- FPR: 실제 음성 -> 모델 음성 = FP / (FP + TN)
'''

# plot the roc curve for the model
plt.plot([0, 1], [0, 1], linestyle='--', label='ROC AUC = 0.5')
plt.plot(fpr, tpr, marker='.', label='ROC Curve')
 
# axis labels
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate') 
plt.legend() 
plt.show()

# 6. roc_auc_score: 곡선 내 확률의 크기 점수화
roc_auc_score(y_test, positive_probs) # 0.98