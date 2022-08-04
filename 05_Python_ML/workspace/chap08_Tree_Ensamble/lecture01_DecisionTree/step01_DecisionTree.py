'''
step01_DecisionTree.py

Decision Tree 모델 
중요변수 선택 기준 : GINI, Entropy
    
 <변수 선택>   
 x변수 : iq수치, 나이, 수입, 사업가유무, 학위유무
 y변수 : 흡연유무
"""

'''
import pandas as pd # csv file download
from sklearn.tree import DecisionTreeClassifier # 분류기: 모델 생성
from sklearn.metrics import accuracy_score # model 평가
# tree 시각화 
from sklearn.tree import export_graphviz
from graphviz import Source # 외부 라이브러리기 때문에 다운로드 필요
'''
graphviz import 과정
1. graphviz 애플리케이션 다운로드 및 설치: ppt 참고
2. 아나콘다 프롬프트 설치: pip install graphviz
3. 메모리상 로딩: import graphviz
'''

# 1. dataset load 
path=r'C:\work\Crystal\DataAnalysis\[ITWILL]BigDataAnalysis_ExpertTraining\05. Python ML'
dataset = pd.read_csv(path+"/data/tree_data.csv")
print(dataset.info())
'''
iq         6 non-null int64 - iq수치
age        6 non-null int64 - 나이
income     6 non-null int64 - 수입
owner      6 non-null int64 - 사업가 유무
unidegree  6 non-null int64 - 학위 유무
smoking    6 non-null int64 - 흡연 유무 - y변수 
'''

# 2. 변수 선택 
cols = list(dataset.columns)
X = dataset[cols[:-1]]
y = dataset[cols[-1]]

# 3. model & 평가 
model = DecisionTreeClassifier(random_state=123).fit(X, y) # 분류기

y_pred = model.predict(X)
print(y_pred) 

acc = accuracy_score(y, y_pred)
print(acc) # 1.0: 100% 예측 -> 모델의 개수 적으며 복잡도가 낮기 때문 


# 4. tree 시각화 
feature_names = cols[:-1]  # x변수 이름
class_names = ['no', 'yes'] # y변수 class (0: no, 1: yes)

# 그래프 설정
graph = export_graphviz(model,
                out_file="tree_graph.dot",
                feature_names = feature_names,
                class_names = class_names,
                rounded=True,
                impurity=True,
                filled=True)
'''
- out_file: 시각화 한것을 특정 dot file에 저장 (dot: 그래픽 출력 가능한 외부 파일)
            = 결과 저장하는 dot file
- feature_names: X 칼럼명
- class_names: y칼럼 내 범주명
- rounded: True면 둥근형, False면 사각형
- impurity: True면 지니 불순도 표시, False면 표시하지 않음
- filled: True면 색상 채움, False면 색상 채우지 X
# 지니 불순도 낮을 수록 좋음
# gini(지니계수) = 1-지니불순도 (클 수록 좋음)
'''

# dot file load 
file = open("tree_graph.dot", mode = 'r') # 파일 객체 읽기
dot_graph = file.read()

# tree 시각화 : Console 출력  (Plots 내 X)
Source(dot_graph) # 주의 : Spyder restart -> 오류 뜨면 spyder 재실행 
# 외부 어플리케이션을 이용하여 출려되기 때문에, plot이 아닌 console에 출력
'''
[해석]
gini: 지니계수
samples: 노드 내 행(샘플) 수
value: 각 범주 별 분류된 개수
class: 가장 많이 존재하는 범주 이름
# 중요변수: income > iq
'''

