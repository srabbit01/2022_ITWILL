"""
chap03_Control: 제어문 = 조건문+반복문

1. 조건문(if)
- 블럭: 콜론과 들여쓰기(tab키) <-> 내여쓰기: 원래 상태로 돌아오기 shift+tab
- 블럭 단위 실행 필요
"""

'''
형식1)
if 조건식 :
    실행문
'''

var = 10 # 초기화 
if var >= 5 :
    print('var=', var)
    print('var는 5보다 크다.')
    print('조건과 상관 있음')
print('조건과 무관') # 들여쓰기가 되어있지 않기 때문에 조건과 무관

'''
형식2) if~else 
if 조건식 :
    실행문1 : True
else :
    실행문2 : False 
'''

var = int(input('var 변수에 값 입력 : ')) # 키보드 입력 

if var >= 5 :
    print('var는 5이상')
else :
    print('var는 5미만')


'''
형식3) 연속적 if~else 
if 조건식1 :
    실행문1 -> 조건식1 True
elif 조건식2 :
    실행문2 -> 조건식2 True
else :
    실행문3 -> 모든 조건 False
'''


# 점수 : 100~85 : '우수', 84~70 : '보통', 69이하 (79미만): '저조'

score = int(input('점수 입력: ')) # 점수 

# 중첩 if ~ else 
if score < 0 or score > 100 :
      print('점수 잘못 입력')
else :
    if score >= 85 :
        print('우수')
        grade='우수' # 파생변수에 결과 저장
    elif score >= 70 :
        print('보통')
        grade='보통'
    else :
        print('저조')
        grade='저조'
# 블록이 끝나도 점수에 대한 결과가 파생변수에 저장되어 있음
print('당신의 점수는 %d점이고, 등급은 \'%s\'이다.' %(score,grade))

# 블록 if vs 한줄 if

# 1) 블록 if
num=9

if num>=5:
    result=num+5
else:
    result=num*5

print('result=',result) # result = 14

# 2) 한줄 if: 간혹 생산성을 위해 좋음
# 형식) 변수 = 참 if 조건식 else 거짓

result=num+5 if num>=5 else num*5
print('result=',result) # result = 14

# if 값 in 데이터셋:
names=['홍길동','이순신','유관순'] # c('홍길동','이순신','유관순')
print(names) # ['홍길동', '이순신', '유관순']

if '홍길동' in names:
    print('찾는 이름 있음')
else:
    print('찾는 이름 없음')
