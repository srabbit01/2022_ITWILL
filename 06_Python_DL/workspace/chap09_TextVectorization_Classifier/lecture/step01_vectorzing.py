# -*- coding: utf-8 -*-
"""
step01_vectorzing.py

1. 텍스트 벡터화  
  - 텍스트 -> 숫자형 벡터 변환 
  - 딥러닝 모델에서 텍스트 처리를 위한 전처리 
2. 작업 절차 
   단계1 : 토큰(token) 생성: 텍스트 -> 단어/문자/문장 추출
   단계2 : 정수 인텍스 생성: 단어/문자/문장 모음 -> 단어 순서화 (순서: 단어 역할)
   단계3 : 패딩(padding): 문장의 단어 길이 맞춤 (maxlen 기준)
           -> 문장마다 단어 개수 다르기 때문에 끝 선 맞추기
           -> 대부분 가장 긴 문장 기준 (길이 맞추기)
           -> 모든 문장의 단어 개수가 동일하다 가정
   단계4 : 인코딩(encoding): 딥러닝 모델에 공급할 숫자형 데이터 생성
"""

from tensorflow.keras.preprocessing.text import Tokenizer # 토큰 생성기
from tensorflow.keras.preprocessing.sequence import pad_sequences # 패딩(padding)
from tensorflow.keras.utils import to_categorical # 인코딩(encoding)

# sample text
texts = ['The dog sat on the table.', 'The dog is my Poodle.']

# 토큰 생성기 
tokenizer = Tokenizer() 

# 1. 토큰 생성 
tokenizer.fit_on_texts(texts) # 텍스트 반영

token = tokenizer.word_index  # 텍스트 -> 토큰 추출

print(token) # 단어 사전 = {'단어': 고유숫자}: 모델에 공급되는 특징
# 고유숫자: 단어 등장 순서(중복단어추출X, 유일한 단어에 고유번호 부여)
# -> 단어 대신하는 십진수
'''
{'the': 1,
 'dog': 2,
 'sat': 3,
 'on': 4,
 'table': 5,
 'is': 6,
 'my': 7,
 'poodle': 8}
# 등장 순서대로 번호 생성
'''
print('전체 단어 개수 :', len(token))
# 전체 단어 개수 : 8

# 2. 정수 인텍스 생성: 단어 -> 정수 변환
seq_vector = tokenizer.texts_to_sequences(texts)
print(seq_vector)
'''
# 단어 -> 10진수
  문장1(6개)          문장2(5개)       문장3(3개) -> 단어 수치화 
[[1, 2, 3, 4, 1, 5], [1, 2, 6, 7, 8], [2, 4, 5]]
'''

# max length : 최대 단어수 
lens=[len(sent) for sent in seq_vector]
lens # [6, 5]
maxlen = max(lens)
'''
max_length: 한 문장을 구성하는 최대 단어수
 -> max_length=10: 모든 문장의 단어 길이 10개
 -> 10개 미만의 부족한 단어의 경우, 0으로 채움
 -> 10개 초과의 넘치는 단어의 경우, 10개로 잘림
'''

# 3. 패딩(padding): 정수 인덱스 길이 맞춤 (maxlen 기준)
padding = pad_sequences(seq_vector, maxlen = maxlen)
print(padding)
'''
[[1 2 3 4 1 5]  - 문장1
 [0 1 2 6 7 8]  - 문장2
 [0 0 0 2 4 5]] - 문장3
# 자리 맞추기 위해 0 패딩 추가
'''


# 4. 인코딩 : one-hot encoding(2진수)
one_hot = to_categorical(padding)
print(one_hot)
'''
문장1
[[[0. 1. 0. 0. 0. 0. 0. 0. 0.]  the
  [0. 0. 1. 0. 0. 0. 0. 0. 0.]
  [0. 0. 0. 1. 0. 0. 0. 0. 0.]
  [0. 0. 0. 0. 1. 0. 0. 0. 0.]
  [0. 1. 0. 0. 0. 0. 0. 0. 0.]
  [0. 0. 0. 0. 0. 1. 0. 0. 0.]] table
문장2
 [[1. 0. 0. 0. 0. 0. 0. 0. 0.]  padding(0)
  [0. 1. 0. 0. 0. 0. 0. 0. 0.]  the
  [0. 0. 1. 0. 0. 0. 0. 0. 0.]
  [0. 0. 0. 0. 0. 0. 1. 0. 0.]
  [0. 0. 0. 0. 0. 0. 0. 1. 0.]
  [0. 0. 0. 0. 0. 0. 0. 0. 1.]]]Poodle
'''

one_hot.shape # (2, 6, 9) -> (문장개수, 단어개수, 전체단어개수+1)
'''
- docs: 전체 문장 개수
- words: 문서 내 포함된 단어의 개수 (maxlen)
- total_words: 전체 단어 개수 + 1 (padding 때문에 추가)
# 첫번째 열 = padding (실제 데이터 X)
'''
