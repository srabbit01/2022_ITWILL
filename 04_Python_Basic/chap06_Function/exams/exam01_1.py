'''
문1-1) start ~ end 사이의 합계 구하기   

<출력 예시>
start : 1
end : 10

합계 = 55
'''

# 함수 정의
def get_sum(start, end):
    sum_value  = 0 
    if end >= start:
        for i in range(start,end+1):
            sum_value+=i
    else:
        for i in range(start,end-1,-1):
            sum_value+=i
    return sum_value

# 키보드 입력 
start = int(input('start : '))
end = int(input('end : '))
print()

# 함수 호출
sum_value = get_sum(start, end) 
print('합계 =',sum_value)
