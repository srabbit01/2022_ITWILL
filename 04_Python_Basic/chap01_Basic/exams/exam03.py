
'''
문3) 화씨를 섭씨로 변환하는 프로그램을 작성하시오.
   화씨온도 변수명 : ftemp
   섭씨온도 변수명 : ctemp
   온도변환 수식 = (화씨온도 - 32.0) * (5.0/9.0)
   
   <<화면출력 결과>>
 화씨온도 : 93
 섭씨온도 = 33.888889
'''

# 1. 화씨온도 사용자 입력
ftemp=int(input('화씨온도 : '))

# 2. 섭씨온도 계산
ctemp = (ftemp - 32.0) * (5.0/9.0)

# 3. 결과 출력
print('화씨온도 :',ftemp)
print('섭씨온도 = %8.6f' %ctemp)
