# -*- coding: utf-8 -*-
"""
step02_logisticRegression_multiClass.py

 - 다항분류기(multi class classifier)  
"""
from sklearn.datasets import load_digits # dataset
from sklearn.linear_model import LogisticRegression # model 
from sklearn.model_selection import train_test_split # dataset split 
from sklearn.metrics import confusion_matrix, accuracy_score # model 평가 


# 1. dataset loading 
digits = load_digits()

image = digits.data # x변수 
label = digits.target # y변수 

image.shape # (1797, 64) 
label.shape # (1797,) 

# 2. train_test_split
img_train, img_test, lab_train, lab_test = train_test_split(
                 image, label, 
                 test_size=0.3, 
                 random_state=123)


# 3. model 생성 
lr = LogisticRegression(random_state=123,
                   solver='lbfgs',
                   max_iter=3000, 
                   multi_class='multinomial',verbose=1)
# hyper parameter: 사용자가 지정하는 parameter

model = lr.fit(X=img_train, y=lab_train)


# 4. model 평가 
y_pred = model.predict(img_test) # class 예측 

# 혼동행렬(confusion matrix)
con_mat = confusion_matrix(lab_test, y_pred)

# 분류정확도(Accuracy)
accuracy = accuracy_score(lab_test, y_pred)
print('Accuracy =', accuracy) 


# heatmap 시각화 
import matplotlib.pyplot as plt
import seaborn as sn
  
# confusion matrix heatmap 
plt.figure(figsize=(6,6)) # size
sn.heatmap(con_mat, annot=True, fmt=".3f",
           linewidths=.5, square = True) 
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
all_sample_title = 'Accuracy Score: ', format(accuracy,'.6f')
plt.title(all_sample_title, size = 18)
plt.show()

