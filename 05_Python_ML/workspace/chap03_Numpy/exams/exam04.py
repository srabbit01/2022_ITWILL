'''
문4) 다음 같은 가중치(weight)와 입력(X)를 이용하여 히든 노드(hidden node)를 구하시오.  
    <조건1> weight(3,3) * X(3,1) = hidden(3,1)  
    <조건2> weight 행렬 자료 : 표준정규분포 난수  
    <조건3> X 행렬 자료 : 1,2,3     
'''

import numpy as np

print('weight 행렬 자료')
weight=np.random.randn(3,3) # (3,3)
print(weight)
print()
print(' X 행렬 자료')
X=np.random.normal(0,1,3)
X=np.array([[1],[2],[3]])
print(X) # (3,1)
print()
print('hidden 노드')
hidden=np.dot(weight,X)
print(hidden)
# [-0.6344628  -1.07611907 -0.36521941]





