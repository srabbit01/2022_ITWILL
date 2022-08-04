# -*- coding: utf-8 -*-
"""
문1) 토큰 생성기를 이용해서 문장의 전체 단어 길이를 확인하고,
    희소행렬과 max length를 적용하여 문서단어 행렬을 만드시오. 
"""

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


sentences = [
    "Mr. Green killed Colonel Mustard in the study with the candlestick. Mr. Green is not a very nice fellow.",
    "Professor Plum has a green plant in his study.",
    "Miss Scarlett watered Professor Plum's green plant while he was away from his office last week."]

# 전체 문장 길이
print(len(sentences)) # 3


# 1. num_words 토큰 생성기 : 중요단어 50개 선정 
tokenizer = Tokenizer(num_words=51)
tokenizer.fit_on_texts(sentences)


# 2. 전체 단어 개수 확인 
words = tokenizer.word_index
len(words) # 33개


# 3. sparse matrix : count, tfidf

# 1) count
count_mat = tokenizer.texts_to_matrix(texts=sentences, mode='count')
print(count_mat)
count_mat.shape # (3, 51)

# 2) tfidf
tfidf_mat = tokenizer.texts_to_matrix(texts=sentences, mode='tfidf')
print(tfidf_mat)
tfidf_mat.shape # (3, 51)


# 4. max length 지정 문장 길이 맞춤 : 두번째 단어 길이 이용 

# 1) 정수 인덱스 생성
seq_vector = tokenizer.texts_to_sequences(sentences)

# 2) 각 문장의 단어 길이
lens=[len(sent) for sent in seq_vector]
print(lens) # [19, 9, 16]

# 3) 패딩: max_len 이요하여 전체 문서 길이 맞추기
padding = pad_sequences(seq_vector, maxlen = max(lens))
print(padding)
'''
[[ 2  1 10 11 12  3  4  5 13  4 14  2  1 15 16  6 17 18 19]  -> 짤림
 [ 0  0  0  0  0  0  0  0  0  0  7 20 21  6  1  8  3  9  5]  -> 채움(패딩)
 [ 0  0  0 22 23 24  7 25  1  8 26 27 28 29 30  9 31 32 33]] -> 기준
'''
