'''
1. Tensor 모양변경  
 - tf.transpose : 전치행렬 
 - tf.reshape : 모양 변경 
'''

import tensorflow as tf

print("\ntensorflow")
# 정규분포 따르는 난수 생성
x = tf.random.normal([2, 3]) # 2행 3열
print(x)

# 전치행렬
xt = tf.transpose(x) # 3행 2열
print(xt) 

# 모양 재수정
x_r = tf.reshape(tensor=x, shape=[1, 6]) # (tensor, shape)
print(x_r) # 1행 6열

x3d = tf.reshape(tensor=x, shape=[2, 1, 3])
print(x3d)

'''
2. squeeze
 - 차원의 size가 1인 경우 제거
'''

# 영행렬 생성
t = tf.zeros( (1,2,1,3) )
t.shape # [1, 2, 1, 3]

# 4d -> 2d
print(tf.squeeze(t)) # shape=(2, 3)

print(tf.squeeze(t).shape) # (2, 3)

print(tf.squeeze(t).get_shape()) # (2, 3)


'''
3. expand_dims
 - tensor에 축 단위로 차원을 추가하는 함수 
'''

const = tf.constant([1,2,3,4,5]) # 1차원 

print(const)
print(const.shape) # (5,)

d0 = tf.expand_dims(const, axis=0) # 행축 2차원 
print(d0) # 차원 증가
d0 = tf.expand_dims(d0, axis=0)

d1 = tf.expand_dims(const, axis=1) # 열축 2차원 
print(d1)
d1 = tf.expand_dims(d1, axis=1)

'''
4. slice
- tensorflow 자료 자르기
'''

t = tf.constant([[[1, 1, 1], [2, 2, 2]],
                 [[3, 3, 3], [4, 4, 4]],
                 [[5, 5, 5], [6, 6, 6]]])

# 원본 t에서 시작위치 [1, 0, 0]은 [3, 3, 3] 리스트의 맨 앞 [3] 이다.
# 시작 위치에서 [1, 1, 3] shape으로 내용물을 꺼내오면,
# 총 1*1*3 개의 원소가 차례대로 선택되고 
# 그 결과는 [[[3, 3, 3]]] 이 된다.
tf.slice(t, [1, 0, 0], [1, 1, 3]).numpy()


# 같은 위치에서 1*2*3 개의 원소를 [1, 2, 3] shape으로 꺼내오면,
# [[[3, 3, 3],
#   [4, 4, 4]]]
tf.slice(t, [1, 0, 0], [1, 2, 3]).numpy()


# 같은 원리로 아래의 결과를 생각해보자
tf.slice(t, [1, 0, 0], [2, 1, 3]).numpy()
# [[[3, 3, 3]],
#  [[5, 5, 5]]]