'''
step02_DecisionTree_parameter.py

DecisionTreeClassifier 관련 문서 : 
https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html

DecisionTree Hyper parameter 
'''
from sklearn.model_selection import train_test_split # data_split
from sklearn.datasets import load_iris # dataset
from sklearn.tree import DecisionTreeClassifier # 분류기
# tree 시각화 
from sklearn.tree import export_graphviz
from graphviz import Source  

############################
### Hyper parameter 
############################
iris = load_iris()
x_names = iris.feature_names # x변수 이름 
'''
['sepal length (cm)',
 'sepal width (cm)',
 'petal length (cm)',
 'petal width (cm)']
'''
labels = iris.target_names # ['setosa', 'versicolor', 'virginica']

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=123)

# help(DecisionTreeClassifier)
'''
1. criterion='gini' : 중요변수 선정 기준, 
 -> criterion : {"gini", "entropy"}, default="gini"
2. splitter='best' : 각 노드에서 분할을 선택하는 데 사용되는 전략, # 기본: best
3. max_depth=None : tree 최대 깊이, 
 -> max_depth : int(정수), default=None
 -> max_depth=None : min_samples_split의 샘플 수 보다 적을 때 까지 tree 깊이 생성 
                     = 계속 생성
 -> max_depth=int(정수): 사용자가 직접 트리의 깊이 지정
 -> 과적합 제어 역할 : 값이 클 수록 과대적합, 적을 수록 과소적합 
4. min_samples_split=2 : 내부 노드를 분할하는 데 필요한 최소 샘플 수(기본 2개)
 -> int or float, default=2    
 -> 과적합 제어 역할 : 값이 클 수록 과소적합, 적을 수록 과대적합 
# max_depth, min_samples_split를 이용하여 과소적합 문제 해결
# 두 파라미터를 역관계
# 만일 max_depth=None이면 min_samples_split에 의해 tree 깊이 결정
'''
# sample size: 평가에서 사용되는 관측치의 수
# 따라서 min_samples_split=2는 관측치의 수가 2 또는 그 이하가 될때까지 트리의 깊이를 만들어 줌

## 1. model : default parameter
tree = DecisionTreeClassifier(criterion='gini',
                               random_state=123, 
                               max_depth=None,
                               min_samples_split=2)

model = tree.fit(X=X_train, y=y_train)
dir(model)
'''
- score(): 분류 정확도
- get_depth(): 트리 깊이
- predict(): 예측치 계산
- min_samples_leaf: 내부 노드 분할 최소 샘플 수
- feature_importances_: X변수 중요도 점수화하여 출력
'''
# 트리 깊이
model.get_depth() # 5
# 내부 노드 분할 최소 샘플 수
model.min_samples_leaf # 1
# 기준: 1 혹은 2 출력 가능
# X변수의 중요도
idx=model.feature_importances_.argmax() # 20 (위치20, 21번째 칼럼 중요)
labels[idx] # 칼럼 이름 반환

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
# 중요변수: petal length > petal width

# 과적합(overfitting) 유무 확인  
model.score(X=X_train, y=y_train) # 1.0
model.score(X=X_test, y=y_test) # 0.9555555555555556
1.0 - 0.9555555555555556 # 0.0444444444444444

## 2. model2 : 과적합 해결 -> max_depth 혹은 min_samples_split 조정
# max_depth=3 -> max_depth: root 노드를 제외한 자손 노드의 세로 개수(깊이)
tree2 = DecisionTreeClassifier(criterion='gini',
                               random_state=123, 
                               max_depth=3,
                               min_samples_split=2)
# min_samples_split=20
tree2 = DecisionTreeClassifier(criterion='gini',
                               random_state=123, 
                               max_depth=None,
                               min_samples_split=20)
# 모델 생성
model2 = tree2.fit(X=X_train, y=y_train)
# 과적합(overfitting) 유무 확인  
model2.score(X=X_train, y=y_train) # 0.9809523809523809
model2.score(X=X_test, y=y_test) # 0.9333333333333333
# 분류 정확도가 조금 떨어진 것을 알 수 있음 -> 과적합 해결
0.9809523809523809 - 0.9333333333333333 # 0.04761904761904756
# tree 시각화 
graph = export_graphviz(model2,
                out_file="tree_graph.dot2",
                feature_names=x_names,
                class_names=labels,
                rounded=True,
                impurity=True,
                filled=True)
# dot file load 
file = open("tree_graph.dot2") 
dot_graph = file.read()
# tree 시각화 : Console 출력  
Source(dot_graph)

## 3. model3 : criterion='entropy' 지정 -> 차이 확인 (기본: gini)
tree3 = DecisionTreeClassifier(criterion='entropy',
                               random_state=123, 
                               max_depth=3,
                               min_samples_split=2)

model3 = tree3.fit(X=X_train, y=y_train)
# 깊이 확인
model3.get_depth() # 3
# 과적합(overfitting) 유무 확인  
model3.score(X=X_train, y=y_train) # 0.9809523809523809
model3.score(X=X_test, y=y_test) # 0.9333333333333333
# tree 시각화 
graph = export_graphviz(model3,
                out_file="tree_graph.dot3",
                feature_names=x_names,
                class_names=labels,
                rounded=True,
                impurity=True,
                filled=True)
# dot file load 
file = open("tree_graph.dot3") 
dot_graph = file.read()
'''
entropy: 정보이득
'''
# tree 시각화 : Console 출력  
Source(dot_graph) 
# 중요변수: petal length > petal width

# tree 시각화 2
# plot_tree: 노드가 많으면 가독성이 떨어짐 (sklearn 제공) -> 잘 사용하지 않음
from sklearn.tree import plot_tree
plot_tree(model)
help(plot_tree)
'''
plot_tree(decision_tree, *, max_depth=None, feature_names=None,
          class_names=None, label='all', filled=False, impurity=True,
          node_ids=False, proportion=False, rotate='deprecated',
          rounded=False, precision=3, ax=None, fontsize=None)
'''