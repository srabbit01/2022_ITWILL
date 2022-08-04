# -*- coding: utf-8 -*-
"""
문제3) obama.txt(오바바 연설문) 파일을 읽어와서 텍스트를 전처리한 후 다음과 같이 출력하시오.
  
  <출력 예시>  
전체 단어수 = 4,907개
최고 출현 단어 :  the
top10 word = ['the', 'and', 'of', 'to', 'our', 'that', 'a', 'you', 'we', 'applause']

단어 빈도수
the : 205
and : 195
of : 152
to : 140
our : 109
that : 91
a : 83
you : 82
we : 81
applause : 75
"""

# 텍스트 전처리 함수
def clean_text(texts) :
    from re import sub
    
    # 1. 소문자 변경     
    texts_re = texts.lower()  # string.lower()
    
    # 2. 숫자 제거 : list 내포
    texts_re2 = sub('[0-9]', '', texts_re) 
    
    # 3. 문장부호 제거 : sub('p', 'r', string)
    punc_str = '[,.?!:;]'    
    texts_re3 = sub(punc_str, '', texts_re2) 
    
    # 4. 특수문자 제거 : sub('p', 'r', string)
    spec_str = '[!@#$%^&*()\[\]]'    
    texts_re4 = sub(spec_str, '', texts_re3) 
        
    # 5. 공백(white space) 제거 
    texts_re5 = ' '.join(texts_re4.split()) 
    
    return texts_re5


import os 

try :
    # 1.파일 읽기 : obama.txt
    os.chdir('C:\\work\\Crystal\\DataAnalysis\\[ITWILL]BigDataAnalysis_ExpertTraining\\04. Python Basic\\workspace\\chap08_FileIO\\data')
    rfile = open('obama.txt', mode = 'r') 
    
    # 2. 줄단위 전체 읽기 
    all_=rfile.readlines()
    
    # 3.줄 단위 텍스트 전처리  
    li=[]
    for a in all_:
        a_=clean_text(a)
        if a_ != '':
            li.append(a_)
    
    # 4. 단어 카운트 : 전체 단어수 & 최고 단어 
    word=[]
    for l in li:
        sp=l.split()
        word.extend(sp)
    
    # 5. Top10 단어 & 단어 빈도수 
    get_word={}
    for gw in word:
        get_word[gw]=get_word.get(gw,0)+1
    
    # 최고 출현 빈도수 높은 것 선정
    # 내림차순 정렬
    sorted_word=sorted(get_word,key=get_word.get,reverse=True)
    top10=sorted_word[:10]
    
    # 6. 결과 출력
    print('전체 단어수 : {}개'.format(len(word)))
    print('최고 출현 단어 :  {}'.format(top10[0]))
    print(f'top10 word = {top10}')
    for i in top10:
        print(f'{i} : {get_word[i]}')
    
except Exception as e:
    print('Error 발생 : ', e)
finally:
    rfile.close()
    
    