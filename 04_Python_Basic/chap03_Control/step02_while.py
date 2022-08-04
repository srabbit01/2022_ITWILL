'''
반복문(while)

형식)
while 조건식 :
    실행문
    실행문 
'''

# 1. 카운터와 누적 변수 
cnt = tot = 0 # 초기화
print(cnt,tot)

while cnt < 5 : 
    cnt += 1  # 카운터 변수
    tot += cnt #  누적 변수
    print(cnt,tot)
print() # line skip
print('cnt=',cnt,'tot=',tot) 


# 2. 1 ~ n까지 수열 누적합
cnt = tot = tot2 = 0

while cnt < 100 : # 100회 반복
    cnt += 1 # 카운터
    tot += cnt # 누적 합 (1~100)
    if cnt % 5 == 0:
        tot2 += cnt # 누적 합(1~100 중 5배수)
                
print('1 ~ 100까지 합 = %d' %tot) # 1 ~ 100까지 합 = 5050
print('1 ~ 100까지 5배수 합 = %d' %tot2) 

# 문제) 1~100 사이에서 3의 배수이면서(and) 5의 배수가 아닌 합 구하기
cnt = tot = 0
while cnt < 100:
    cnt+=1 # 카운터
    if cnt % 3 == 0 and cnt % 5 != 0:
        print(cnt,end=' ')
        tot += cnt # 누적 합
print()
print('tot=',tot) # tot = 1368
        
# 3. 무한 루프 -> exit 조건 지정 
while True :
    num = int(input('숫자 입력 : '))
    
    if num % 10 == 0 : # exit(탈출) 조건 
        print('프로그램 종료')
        break # loop exit
        print('입력 값 -> ', num)


print('>>숫자 맞추기 게임<< ')
'''
 myInput == computer : '성공'(exit)
 myInput > computer : '더 작은 수 입력'
 myInput < computer : '더 큰수 입력'
'''

import random # 난수 생성 함수 제공
com = random.randint(a=1,b=10) # 1~10 정수 난수 생성
while True:
    my = int(input('예상 숫자 입력 : ')) # 사용자 숫자 입력
    
    if my == com: # 탈출 조건
        print('성공!')
        break # loop exit
    elif my > com:
        print('더 작은 수 입력')
    else:
        print('더 큰 수 입력')
        
# 4. continue, break
'''
반복문에서 사용되는 키워드
continue: 계속 반복, 다음 문장 skip
break: 반복 탈출 (exit)
'''

i = 0
while i < 10 :
    i += 1 # 카운터
    if i == 3 : 
        continue #  다음 문장 skip
    if i == 4:
        pass
    if i == 6 : # 2차 작성  
        break #  루프 탈출(loop exit)
    print(i, end = ' ') 



