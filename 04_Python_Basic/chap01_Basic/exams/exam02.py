'''
문2) 다음 밑변, 윗변, 높이를 이용하여 사다리꼴의 넓이를 구하시오.

    조건1) 밑변(base), 윗변(upper), 높이(height)
              base = 12, upper = 7, height = 9
    조건2) 사다리꼴 넓이(area) 
             area = (base + upper) * height / 2
    조건3) 소수점 2자리 까지 출력 : format()이용 

   <<화면출력 결과>>
 밑변 입력 : 12
 윗변 입력 : 7
 높이 입력 : 9
 사다리꼴 넓이 =  85.50
'''

# 1. 변수 입력
base = 12; upper = 7; height = 9

# 2. 사다리꼴 넓이 계산
area = (base + upper) * height / 2

# 3. 결과 출력
print('밑변 입력 :',base)
print('윗변 입력 :',upper)
print('높이 입력 :',height)
print("사다리꼴 넓이 =",format(area,'.2f'))
