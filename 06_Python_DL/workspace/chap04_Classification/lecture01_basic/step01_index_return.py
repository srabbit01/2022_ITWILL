'''
index 리턴 
  1. argmin/argmax
   - 최소/최대 값의 index 반환 
  2. argsort
   - 정렬 후 index 반환
'''
import tensorflow as tf # ver2.3

a = tf.constant([5,2,1,4,3], dtype=tf.int32) # 1차원 
b = tf.constant([4,5,1,3,2]) # 1차원 
c = tf.constant([[5,4,2], [3,2,4]]) # 2차원 
print(c)
'''
[[5 4 2]
 [3 2 4]]
'''

# 1. argmin/argmax : 최솟값/최댓값 색인반환 
# 형식) argmin/argmax(input, axis=0)
print(tf.argmin(a).numpy()) # 2
print(tf.argmax(b).numpy()) # 1

# 2차원 : 행축(열 단위) : axis=0, 열축(행 단위) : axis=1
print(tf.argmin(c, axis=0).numpy()) # 행축: 열단위 = [1 1 0]
print(tf.argmin(c, axis=1).numpy()) # 열축: 행단위 = [2 1]

print(tf.argmax(c, axis=0).numpy()) # [0 0 1]
print(tf.argmax(c, axis=1).numpy()) # [0 2]


# 2. argsort : 오름차순정렬 후 색인반환
# 행렬 없이 전체: axis = -1 -> 행렬 따로 못함
# 형식) tf.argsort(values, axis = -1, direction='ASCENDING')
print(tf.argsort(a)) 
# [5,2,1,4,3] -> [2 1 4 3 0]
print(tf.argsort(b)) 
# [4,5,1,3,2] -> [2 4 3 0 1]

# 내림차순 정렬 -> 색인 반환
print(tf.argsort(a,direction='DESCENDING')) 
# [0 3 4 1 2]
print(tf.argsort(b,direction='DESCENDING')) 
# [1 0 3 4 2]

# 행렬자료 -> 색인 반환
print(tf.argsort(c))
'''
[[5 4 2]
 [3 2 4]]
---------------------
[[2 1 0]  -> 1행 색인
 [1 0 2]] -> 2행 색인
'''