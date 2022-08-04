# -*- coding: utf-8 -*-
"""
step01_cosine_similarity.py

코사인 유사도 이용 -> 유사 문서 찾기  

<작업절차>
 1. 자연어 -> 문서단어행렬 변경 
 2. 코사인 유사도 적용     
 
 # Encoding: 단어 -> 숫자
"""

# 희소행렬(sparse matrix)
from sklearn.feature_extraction.text import TfidfVectorizer # 단어생성기 
# 코사인 유사도 
from sklearn.metrics.pairwise import cosine_similarity # 1(대상문서) vs N(타문서)


# 문장(자연어)
sentences = [
    "Mr. Green killed Colonel Mustard in the study with the candlestick. Mr. Green is not a very nice fellow.",
    "Professor Plum has a green plant in his study.",
    "Miss Scarlett watered Professor Plum's green plant while he was away from his office last week."
] # list

print(sentences)
len(sentences) # 3


# 1. 대상 문서(자연어) -> DTM(문서단어행렬:희소행렬) 변경
# 단어 생성 및 희소행렬 생성 -> 7장. sparse matrix
obj = TfidfVectorizer() # 1) 단어생성기 

# 단어 보기 
fit = obj.fit(sentences)
voca = fit.vocabulary_ # 단어들 
print(voca)

# 2) 희소행렬(DTM) 
sp_mat = obj.fit_transform(sentences)
print(sp_mat)
'''
  (문서번호,딘어번호) 가중치
  (0, 3)	0.2205828828763741
  (0, 16)	0.2205828828763741
  (0, 25)	0.2205828828763741
# 1에 가까울 수록 중요, 0에 가까울 수록 중요하지 않음
  '''

# scipy -> numpy
sp_mat_arr = sp_mat.toarray()
print(sp_mat_arr)
type(sp_mat_arr) # numpy.ndarray

# 2. 코사인 유사도 적용 

# 1) 검색 쿼리(search query)
query = ['green plant in his study'] # 검색 문장 

# 2) 희소행렬(DTM)
# 이미 fitting되어 있기 때문에 fit하지 않음
query_sp_mat = obj.transform(query) # 함수 주의 
# 이미 fitting된 31개 단어 희소행렬에 해당 문서의 해당 부분만 가중치 부여

# scipy -> numpy
query_sp_mat_arr = query_sp_mat.toarray()
query_sp_mat_arr.shape # (1, 31) = (문장수,단어수)
query_sp_mat_arr


# 3) 코사인 유사도 계산 
sim = cosine_similarity(query_sp_mat_arr, sp_mat_arr) # (query,N)
# 쿼리와 N개의 문장을 각각 1:N 비교하기
sim.shape # (1, 3) = 1 : 3 문장 비교함을 볼 수 있음
print(sim) 
# 유사도 결과: [[0.25069697 0.74327606 0.24964024]]
# [해설] 두번째 문서의 코사인 유사도가 가장 큼


# 4) 2d(1, 3) -> 1d(3,)
sim = sim.reshape(3)
sim.shape # (3,) # 2차원 벡터 -> 1차원 벡터


# 5) 내림차순 정렬 -> index 반환
sim.argsort() # 오름차순: [2, 0, 1]
idx=sim.argsort()[::-1] # 내림차순: [1, 0, 2]
type(idx)


# 6) query와 가장 유사도가 높은 순으로 문장 출력
for i in idx:
    print(f'similarity : {sim[i]}, sentences : {sentences[i]}')
'''
similarity : 0.7432760626367734, sentences : Professor Plum has a green plant in his study.
similarity : 0.25069697393300555, sentences : Mr. Green killed Colonel Mustard in the study with the candlestick. Mr. Green is not a very nice fellow.
similarity : 0.2496402361939771, sentences : Miss Scarlett watered Professor Plum's green plant while he was away from his office last week.
'''