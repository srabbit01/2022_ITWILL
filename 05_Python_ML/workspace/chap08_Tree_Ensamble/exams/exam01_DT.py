'''
 문1) load_breast_cancer 데이터 셋을 이용하여 다음과 같이 Decision Tree 모델을 생성하시오.
 <조건1> 75:25비율 train/test 데이터 셋 구성 
 <조건2> y변수 : cancer.target, x변수 : cancer.data
 <조건3> tree 최대 깊이 : 5 
 <조건4> decision tree 시각화 & 중요변수 확인 

'''
from sklearn import model_selection
from sklearn.datasets import load_breast_cancer
from sklearn.tree import DecisionTreeClassifier
# tree 시각화 
from sklearn.tree import export_graphviz
from graphviz import Source # pip install graphviz

# 데이터 셋 load 
cancer = load_breast_cancer()
type(cancer)

# <단계1> y변수 : cancer.target, x변수 : cancer.data 
y=cancer.target
X=cancer.data

# <단계2> 75:25비율 train/test 데이터 셋 구성
from sklearn.model_selection import train_test_split 
X_train,X_test,y_train,y_test=train_test_split(
    X,y,random_state=123,test_size=0.25)

# <단계3> tree 최대 깊이 : 5
tree = DecisionTreeClassifier(criterion='gini',
                               random_state=123, 
                               max_depth=5,
                               min_samples_split=2)

model = tree.fit(X=X_train, y=y_train)
model.get_depth() # 5

# <단계4> decision tree 시각화 & 중요변수 확인 
dir(cancer)
x_names=cancer.feature_names
labels=cancer.target_names
# tree 시각화 
graph = export_graphviz(model,
                out_file="tree_graph.dot",
                feature_names=x_names,
                class_names=labels,
                rounded=True,
                impurity=True,
                filled=True)
# dot file load 
file = open("tree_graph.dot") 
dot_graph = file.read()
# tree 시각화 : Console 출력  
Source(dot_graph) 

# <단계5> model 평가: 분류정확도, 혼동행렬

# 1) 분류 정확도
model.score(X_train,y_train) # 0.9953051643192489
model.score(X_test,y_test) # 0.972027972027972
# 정확도가 매우 높음을 알 수 있음

# 2) 혼동행렬
from sklearn.metrics import confusion_matrix
ytest_pred=model.predict(X_test)
con_mat=confusion_matrix(y_test,ytest_pred)
print(con_mat)
'''
[[52  2]
 [ 2 87]]
'''
# 정분류가 오분류보다 훨씬 더 많음을 볼 수 있음