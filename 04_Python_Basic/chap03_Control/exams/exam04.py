# -*- coding: utf-8 -*-
"""
문4) 키보드로 입력받은 문자열 중에서 자음과 모음의 개수를 집계하는 프로그램을 작성하여 보자.
     모음(홀소리) : aeiou, 자음(닿소리) : 나머지 21개 영문자
"""


original = input('문자열을 입력하시오: ')
word = original.lower() # 소문자 변경 

vowels = 0  # 모음 문자 카운트
consonants = 0  # 자음 문자 카운트

vow=['a','e','i','o','u']

# 문자열이 1개 이상이면서 알파벳인 경우 
if len(original) > 0 and original.isalpha():
    pass    
    for i in word:
        if i in vow:
            vowels+=1
        else:
            consonants+=1
    print('모음수: %d, 자음수: %d' %(vowels,consonants))
else :
    print('다시 입력하세요.')         		


