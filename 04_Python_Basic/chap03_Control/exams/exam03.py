
'''
문3) word count
   - 여러 줄의 문자열에서 공백을 기준으로 단어를 분류하고, 단어 수 출력하기
'''

multiline="""안녕 Python 세계로 오신걸
환영 합니다.
파이션은 비단뱀 처럼 매력적인 언어 입니다."""


# <<출력 결과>> 
'''
안녕
Python
세계로
오신걸
환영
합니다.
파이션은
비단뱀
처럼
매력적인
언어
입니다.
단어수 : 12
'''

# 1. 문단 > 문장 > 단어
words=[]
for sents in multiline.split('\n'):
    for word in sents.split():
        print(word)
        words.append(word)

# 2. 결과 출력 
print('단어수: %d' %len(words))