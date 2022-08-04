# -*- coding: utf-8 -*-
"""
step02_konlpy.py

konlpy : 한글 형태소 분석을 제공하는 패키지 
pip install konlpy
"""

import konlpy

from konlpy.tag import Kkma # class 
from konlpy.tag import Okt # class
'''
Kkma vs Okt
- 공통점: 형태소 분석기(문장을 품사 단위로 쪼개는 과정)
- 차이점
  - Kkma: 상세한 품사 정보 제공 (동일 단어 내 파생 단어 추출)
  - Okt: 일반 품사 정보 제공(명사,조사,형용사) + 영문 단어 포함
'''

##########################
### Kkma
##########################
kkma = Kkma() # 객체 생성 
'''
OSError: [WinError 126] JVM DLL not found: C:\Program Files\Java\jre1.8.0_151\bin\server\jvm.dll
- JDK 프로그램 손상 가능성 존재
- 1) Spyder 재시작
- 2) JDK 제거 -> JDK 재다운로드
'''

dir(Kkma)
'''
 'morphs',: 형태소만 추출
 'nouns',: 문장 -> 명사(단어) 추출
 'pos',: (형태소,품사) 한쌍으로 추출
 'sentences': 문단 -> 문장 추출
 '''
# 문단 -> 문장 or 문장 -> 형태소 : 토큰화

# 문단(단락) : 3개의 문장 집합
para = "나는 홍길동 입니다. age는 23세 입니다. 대한민국을 사람 만세 입니다."

# 문단(단락) -> 문장
ex_sent = kkma.sentences(para) # list 반환 
print(ex_sent)
# ['나는 홍길동 입니다.', 'age는 23세 입니다.', '대한민국을 사람 만세 입니다.']

# 문단 -> 명사(단어)
ex_nouns = kkma.nouns(para)
print(ex_nouns) # 10개
# ['나', '홍길동', '23', '23세', '세', '대한', '대한민국', '민국', '사람', '만세']
'''
# 명사형 품사 지정하여 원하는 품사의 명사만 추출 가능
'''
# NNG 일반 명사 NNP 고유 명사 NNB 의존 명사 NR 수사 NP 대명사
# 위 중 NNG 일반 명사, NNP 고유 명사, NP 대명사
nouns=[] # 명사 저장
for word, wclass in ex_pos: # (형태소,품사)
    if wclass=='NNG' or wclass=='NNP' or wclass=='NP':
        nouns.append(word)
print(nouns)
# ['나', '홍길동', '대한민국', '사람', '만세']

# 문단 -> 품사(형태소)
ex_pos = kkma.pos(para)
print(ex_pos) # 상세한 품사 제공 
'''
[('형태소', '품사')]
[('나', 'NP'), ('는', 'JX'), ('홍길동', 'NNG'), ('이', 'VCP'), 
 ('ㅂ니다', 'EFN'), ('.', 'SF'), ('age', 'OL'), ('는', 'JX'), 
 ('23', 'NR'), ('세', 'NNM'), ('이', 'VCP'), ('ㅂ니다', 'EFN'), 
 ('.', 'SF'), ('대한민국', 'NNG'), ('을', 'JKO'), ('사람', 'NNG'),
 ('만세', 'NNG'), ('이', 'VCP'), ('ㅂ니다', 'EFN'), ('.', 'SF')]
'''

# 문단 -> 형태소
ex_morphs=kkma.morphs(para) # list 반환
print(ex_morphs)
# ['나', '는', '홍길동', '이', 'ㅂ니다', '.', 'age', '는', '23', '세', '이', 'ㅂ니다', '.', '대한민국', '을', '사람', '만세', '이', 'ㅂ니다', '.']

##############################
### Okt
##############################
okt = Okt() # 객체 생성 
dir(Okt)
'''
 'morphs',: 형태소만 추출
 'normalize',: 문단 -> 문장 추출
 'nouns',: 문장 -> 명사(단어) 추출
 'phrases',: 구 추출 (구: 2개 이상의 단어) -> 절: 공백을 기준으로 잘리는 것
 'pos': (형태소,품사) 한쌍으로 추출
'''
# 형태소 추출 
okt.morphs(para) # list
'''
['나', '는', '홍길동', '입니다', '.', 'age', '는', '23', '세', '입니다',
 '.', '대한민국','을', '사람', '만세', '입니다', '.']
'''

# 문단 -> 문장 
ex_sent = okt.normalize(para) # 문자열 반환 
dir(ex_sent)
ex_sent.split('. ')
print(ex_sent)
type(ex_sent) # str
'''
'나는 홍길동 입니다. age는 23세 입니다. 대한민국을 사람 만세 입니다.'
'''

# 명사 추출 : 중복 단어 추출 X
okt.nouns(para) 
# ['나', '홍길동', '세', '대한민국', '사람', '만세']

# 품사 부착(단어, 품사) 
okt.pos(para) 
'''
# 품사 종류가 세분화되지 X
[('나', 'Noun'), -> 모든 명사
 ('는', 'Josa'), -> 조사
 ('홍길동', 'Noun'),
 ('입니다', 'Adjective'), -> 형용사
 ('.', 'Punctuation'), -> 문장부호
 ('age', 'Alpha'), -> 영문자
 ('는', 'Verb'), -> 동사
 ('23', 'Number'), -> 숫자
 ('세', 'Noun'),
 ('입니다', 'Adjective'),
 ('.', 'Punctuation'),
 ('대한민국', 'Noun'),
 ('을', 'Josa'),
 ('사람', 'Noun'),
 ('만세', 'Noun'),
 ('입니다', 'Adjective'),
 ('.', 'Punctuation')]
'''
# 필요한 품사 단어 추출: 명사 및 영문자
words=[]
for word, wclass in okt.pos(para):
    if wclass=='Noun' or wclass=='Alpha':
        words.append(word)
print(words)
# ['나', '홍길동', 'age', '세', '대한민국', '사람', '만세']
 
# 구 단위 추출
okt.phrases(para)
# ['홍길동', 'age', 'age는 23세', '대한민국', '사람', '사람 만세', '23', '만세']