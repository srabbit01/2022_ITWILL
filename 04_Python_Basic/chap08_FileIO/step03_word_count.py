# -*- coding: utf-8 -*-
"""
step03_word_count.py

<순서 작업>
1. text file read
2. text file 전처리
3. text file saved
4. 단어 카운트
5. TopN 단어 선정
"""

# 텍스트 전처리 함수: chap06 > step03_func_app.py 
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
    spec_str = '[!@#$%^&*()]'    
    texts_re4 = sub(spec_str, '', texts_re3) 
        
    # 5. 공백(white space) 제거 
    texts_re5 = ' '.join(texts_re4.split()) 
    
    return texts_re5

# 1. text file read
path = 'C:\\work\\Crystal\\DataAnalysis\\[ITWILL]BigDataAnalysis_ExpertTraining\\04. Python Basic\\workspace\\chap08_FileIO\\data'

file=open(path+'\\texts.txt',mode='r',encoding='utf-8') # mode='r'
texts=file.readlines() # 줄 단위 전체 문서 읽기
print('texts 전처리 전')
print(texts)
file.close()
'''
['우리나라    대한민국, 우리나라%$ 만세\n', '비아그&라 500GRAM 정력 최고!\n', '나는 대한민국 사람\n', '보험료 15000원에 평생 보장 마감 임박\n', '나는 홍길동']
'''
# 2. text file 전처리
texts_re=[clean_text(t) for t in texts] # 함수 호출
texts_re=clean_text(texts)
print('texts 전처리 후')
print(texts_re)

# 3. text file saved
file2=open(path+'/clean_texts.txt',mode='w',encoding='utf-8')
for t in texts_re:
    file2.write(t+'\n') # 줄바꿈 삽입
print('text sile is saved...')
file2.close()

# 4. 단어 카운트
file3=open(path+'/clean_texts.txt',mode='r',encoding='utf-8')
new_texts=file3.readlines()
words=[] # 단어 저장
# 1) 단어 추출
for t in new_texts: # 문장
    for word in t.split():
        words.append(word)
print('words :\n',words)
# 2) 단어 카운트
wc={} # 빈 dict
for word in words:
    wc[word]=wc.get(word,0)+1
print('word count: \n', wc)
'''
word count:
 {'우리나라': 2, '대한민국': 2, '만세': 1, '비아그라': 1, 'gram': 1, '정력': 1, '최고': 1, '나는': 2, '사람': 1, '보험료': 1, '원에': 1, '평생': 1, '보장': 1, '마감': 1, '임박': 1, '홍길동': 1}
'''

# 5. TopN 단어 선정
# 최고 출현 단어
print('최고 출현 단어 :',max(wc,key=wc.get)) # 키값 생략 가능
# 최고 출현 단어 : 우리나라
# key=dict.get : 모든 key 값 지정

# 출현빈도수에 대한 단어 내림차순 정렬
# dict
wc_sorted=sorted(wc,key=wc.get,reverse=True) # 정렬 기준 (dict -> list)
print(wc_sorted)
# ['우리나라', '대한민국', '나는', '만세', '비아그라', 'gram', '정력', '최고', '사람', '보험료', '원에', '평생', '보장', '마감', '임박', '홍길동']

topN=5
top5_word=wc_sorted[:topN]
print('top5 word :',top5_word)
# top5 word : ['우리나라', '대한민국', '나는', '만세', '비아그라']
print('단어 -> 빈도수')
for i in top5_word:
    print(i,wc[i],sep=' -> ')





