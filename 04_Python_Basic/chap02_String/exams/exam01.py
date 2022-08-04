'''
문1) 3개의 단어를 키보드로 입력 받아서 각 단어의 첫자를 추출하여 단어의 약자를 출력하시오.
  조건1) 각 단어 저장 변수 : word1, word2, word3 
  조건2) 입력과 출력 구분선 : * 연산자 이용 
  조건3) 약자 저장 변수 : abbr
  조건4) 원래 단어 저장 변수 : tot_words  
   
   <<화면출력 결과>>  
 첫번째 단어 : Korea 
 두번째 단어 : Baseball
 세번째 단어 : Orag
 =================
 약자 : KBO
 원래 단어 : Korea Baseball Orag
'''

# 1. 사용자 입력 변수 생성
tot_words=input('단어 입력 : ')

# 2. 단어 분리
sep_word=tot_words.split()
sep_word # ['Korea', 'Baseball', 'Orag']
word1=sep_word[0]
word2=sep_word[1]
word3=sep_word[2]

# 3. 단어 약자 추출
abbr=[word1[0],word2[0],word3[0]]
abbr=''.join(abbr)
abbr

# 4. 결과 출력
line='='*20
print('''
      첫번째 단어 : {}
      첫번째 단어 : {}
      첫번째 단어 : {}
      {}
      약자 : {}
      원래 단어 : {}
      '''.format(word1,word2,word3,line,abbr,tot_words))