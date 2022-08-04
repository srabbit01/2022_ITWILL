'''
step02_operator.py
1. 할당 연산자(=): 변수에 값 할당
2. 패킹(packing) 할당: 여러 개의 값을 묶어 변수에 할당
3. 연산자: 산술, 관계, 논리 연산자
'''

# 1. 할당연산자(=)
# i = 10
# tot = 10
# 한 줄로 서로 다른 변수에 동일한 값 할당 가능
i = tot = 10 # 변수 초기화 
print(i, tot) # 10 10
i += 1 # i = i + 1 -> 카운터 변수: 변수에 1씩 증가
tot += i # tot = tot + i  -> 누적 변수: 변수에 n씩 증가
print(i, tot) 

# 서로 다른값 할당 
v1, v2 = 100, 200
print(v1, v2)

# 변수 값 교체
v2, v1 = v1, v2
print(v1, v2)
'''
C언어의 경우, 임시변수를 생성하여 변수 값 교체
tmp = v1
v1 = v2
v2 = tmp
파이썬의 경우, 임시변수 없이 변수 값 교체
'''

# 2. 패킹(packing) 할당 
lst = [1,2,3,4,5] # 벡터형 자료구조
# R의 C() 함수와 유사
print(lst) # [1, 2, 3, 4, 5]

# *변수: 패킹 할당 대상
v1, *v2 = lst # 첫번째 값 첫번째 변수, 이외 값 두번째 변수에 할당
print(v1, v2) # 1 [2, 3, 4, 5]

*v1, v2 = lst # 이외 값 첫번째 변수, 마지막 값 두번째 변수에 할당
print(v1, v2) # [1, 2, 3, 4] 5

# 3. 연산자 : 산술,관계,논리 연산자 
num1 = 100 
num2 = 6

# 1) 산술연산자 
add = num1 + num2
print('add=', add) # add= 110

sub = num1 - num2
print('sub =', sub) # sub = 90

div = num1 / num2 
print('div =', div) # div = 16.666666

div = num1 // num2 
print('div =', div) # div = 16

div2 = num1 % num2
print('div2=', div2) # div2= 0

mul = num1 * num2
print('mul=', mul) # mul= 1000

square = num1 ** 2
print('square=', square) # square= 10000


# 2) 관계 연산자 
# (1) 동등비교 
result = num1 == num2
print(result) # False

result = num1 != num2
print(result) # True

# (2) 크기비교 
result = num1 > num2
print(result)

result = num1 >= num2
print(result)

result = num1 < num2
print(result)

result = num1 <= num2
print(result)

# 3) 논리 연산자
result = num1 >= 50 and num2 <= 20
print(result) # True

result = num1 < 50 or num2 <= 20
print(result) # True

result = not(num1 < 50)
print(result) # True








