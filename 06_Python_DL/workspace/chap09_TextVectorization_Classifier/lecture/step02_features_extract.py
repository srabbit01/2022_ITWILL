# -*- coding: utf-8 -*-
"""
step02_features_extract.py

1. 텍스트 -> 특징(features) 추출 
   -> texts -> 희소행렬(sparse matrix) : 딥러닝 모델 공급 자료 
   -> 희소행렬 가중치 방법 : binary, count, freq, Tfidf
2. num_words(max features)   
  - 희소행렬의 차수 지정(단어 길이 제한)
"""

from tensorflow.keras.preprocessing.text import Tokenizer # 토큰 생성기 

# text_sample.txt 참고 
texts = ['The dog sat on the table.', 'The dog is my Poodle.']

# 토큰 생성기 
tokenizer = Tokenizer() # 전체 단어 이용
tokenizer.fit_on_texts(texts)  # 텍스트 반영 
token = tokenizer.word_index # 토큰 반환 

print(token) # {'word':고유숫자} 
'''
{'the': 1, 'dog': 2, 'sat': 3, 'on': 4, 
 'table': 5, 'is': 6, 'my': 7, 'poodle': 8}
'''

print('전체 단어 길이 =', len(token))
# 전체 단어 길이 = 8


# 1. 희소행렬(sparse matrix) 

# 1) 단어 출현여부
binary_mat = tokenizer.texts_to_matrix(texts=texts, mode='binary') 
print(binary_mat)
'''
[[0. 1. 1. 1. 1. 1. 0. 0. 0.]  - 문장1
 [0. 1. 1. 0. 0. 0. 1. 1. 1.]] - 문장2
'''
binary_mat.shape # (2, 9) -> (문장개수, 전체 단어 개수 + 1)
# 전체 단어 개수 + 1: (1: padding 여부 출력)

# 2) 단어 출현빈도 
count_mat = tokenizer.texts_to_matrix(texts=texts, mode='count')
print(count_mat)
'''
[[0. 2. 1. 1. 1. 1. 0. 0. 0.]  - 문장1('the': 2회 출현)
 [0. 1. 1. 0. 0. 0. 1. 1. 1.]] - 문장2
'''

# 3) 단어 출현빈도 : 현재 문장 대상 
freq_mat = tokenizer.texts_to_matrix(texts=texts, mode='freq')
print(freq_mat)
'''
[[0.         0.33333333 0.16666667 0.16666667 0.16666667 0.16666667
  0.         0.         0.        ]
 [0.         0.2        0.2        0.         0.         0.
  0.2        0.2        0.2       ]]
'''
# the = 0.3333 = 출현빈도 / 전체 = 2 / 6
# -> 6개 단어 중 출현빈율
# the = 0.2 = 1 / 5 = 전체 5개 중 'the'(1)가 출현한 비율

# 4) 단어 출현비율 = tf * idf(전체문서수/단어포함된문서수)
tfidf_mat = tokenizer.texts_to_matrix(texts=texts, mode='tfidf')
print(tfidf_mat) 
'''
[[0.         0.86490296 0.51082562 0.69314718 0.69314718 0.69314718
  0.         0.         0.        ]
 [0.         0.51082562 0.51082562 0.         0.         0.
  0.69314718 0.69314718 0.69314718]]
'''
# 가장 많이 사용
0.3333 * (2/1) # 0.6666 -> 두 문서 중 한 문서에만 출현
0.3333 * (2/2) # 0.3333 -> 두 문서 모두 출현
# 문서 출현 비율이 높을 수록 가중치 값이 감소


# 2. num_words: 희소행렬 단어 길이 제한

tokenizer = Tokenizer(num_words=6) # 5개 단어 선정(단어길이+1) 
tokenizer.fit_on_texts(texts) # 텍스트 반영 
tokenizer.word_index

binary_mat = tokenizer.texts_to_matrix(texts=texts, mode='binary') 
print(binary_mat)
'''
[[0. 1. 1. 1. 1. 1.]
 [0. 1. 1. 0. 0. 0.]]
'''
binary_mat.shape # (2, 6) -> (문서개수, 전체단어+1)

