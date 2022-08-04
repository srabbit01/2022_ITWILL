'''
Best Cluster 찾는 방법 
'''

from sklearn.cluster import KMeans # model 
from sklearn.datasets import load_iris # dataset 
import matplotlib.pyplot as plt # 시각화 

# 1. dataset load 
X, y = load_iris(return_X_y=True)
print(X.shape) # (150, 4)
print(X)

# 2. Best Cluster 
size = range(1, 11) # k값 범위
inertia = [] # 응집도 

for k in size : 
    obj = KMeans(n_clusters = k) 
    model = obj.fit(X)
    inertia.append(model.inertia_) # inertia_: 응집도
# 응집도 한 줄 출력
inertia=[KMeans(n_clusters=k).fit(X).inertia_ for k in range(1, 11)]

print(inertia)
# 응집도가 작을 수록 좋음
'''
이너샷 value
- 응집도를 나타내는 척도
- 중심점과 각 포인트 간의 거리제곱의 합
- 작을 수록 응집도 좋음
'''

# 3. best cluster 찾기 
plt.plot(size, inertia, '-o')
plt.xticks(size)
plt.show()
# [해설] elbow point: 꺾인 부분의 값이 가장 적절 (좋음)
