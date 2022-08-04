# -*- coding: utf-8 -*-
"""
step04_Entropy.py

지니불순도(Gini-impurity), 엔트로피(Entropy)
  Tree model에서 중요변수 선정 기준
 확률 변수 간의 불확실성을 나타내는 수치
 무질서의 양의 척도, 작을 수록 불확실성이 낮다.

  지니불순도와 엔트로피 수식  
 Gini-impurity = sum(p * (1-p))
 Entropy = -sum(p * log(p))

  지니계수와 정보이득  
  gini_index = base - Gini-impurity # 0.72
  info_gain = base - Entropy
"""
# 지니계수 클 수록 불확실성 낮음
# base: 전체 엔트로피

import numpy as np

# 1. 불확실성이 큰 경우(x1:앞면, x2:뒷면)
x1, x2 = 0.5, 0.5 # 독립사건 = 1

gini = sum([x1 * (1-x1), x2 * (1-x2)])
print(gini) # 0.5

entropy = -sum([x1 * np.log2(x1), x2 * np.log2(x2)])
print(entropy) # 1.0

# 2. 불확실성이 작은 경우(x1:앞면, x2:뒷면)
x1, x2 = 0.9, 0.1 # 독립사건 = 1

gini2 = sum([x1 * (1-x1), x2 * (1-x2)])
print(gini2) # 0.18

entropy2 = -sum([x1 * np.log2(x1), x2 * np.log2(x2)])
print(entropy2) # 0.4689955935892812

base = 0.9
gini_index = base - gini # 0.4
gini_index2 = base - gini2 # 0.72 

info_gain = base - entropy # -0.099999
info_gain2 = base - entropy2 # 0.4310044064107188


##########################
### dataset 적용 
##########################
import numpy as np
# 1. data set 생성 함수
def createDataSet():
    dataSet = [[1, 1, 'yes'],
    [1, 1, 'yes'],
    [1, 0, 'no'],
    [0, 1, 'no'],
    [0, 1, 'no']]
    columns = ['dark_clouds','gust'] # X1,X2,label
    return dataSet, columns


# 함수 호출 
dataSet, columns = createDataSet()

# list -> numpy 
dataSet = np.array(dataSet)
dataSet.shape # (5, 3)
print(dataSet)
'''
[['1' '1' 'yes']
 ['1' '1' 'yes']
 ['1' '0' 'no']
 ['0' '1' 'no']
 ['0' '1' 'no']]
'''
print(columns) # ['dark_clouds', 'gust']

# 변수 선택 
X = dataSet[:, :2]
y = dataSet[:, -1]

# 'yes' = 1 or 'no' = 0
label = [1 if i == 'yes' else 0 for i in y] 
label # [1, 1, 0, 0, 0]

from sklearn.tree import DecisionTreeClassifier # model 
from sklearn.metrics import confusion_matrix # 평가 
# 시각화 도구 
from sklearn.tree import plot_tree, export_graphviz 


# model 생성 
obj = DecisionTreeClassifier(criterion='entropy')
model = obj.fit(X = X, y = label)

y_pred = model.predict(X)
print(y_pred) # [1 1 0 0 0]

con_mat = confusion_matrix(label, y_pred)
print(con_mat)
'''
[[3 0]
 [0 2]]
# 100% 예측
'''

# tree 시각화 
plot_tree(model, feature_names=columns)

# tree graph 
export_graphviz(decision_tree=model, 
                out_file='tree_graph.dot',
                max_depth=3,
                feature_names=columns,
                class_names=True)
# dot file load 
file = open("tree_graph.dot3") 
dot_graph = file.read()
'''
entropy: 정보이득
'''
# tree 시각화 : Console 출력  
Source(dot_graph) 


## criterion='gini'
# model 생성 
obj2 = DecisionTreeClassifier(criterion='gini')
model2 = obj2.fit(X = X, y = label)
# tree 시각화
plot_tree(model2, feature_names=columns)
# entropy와 거의 비슷함을 볼 수 있음

