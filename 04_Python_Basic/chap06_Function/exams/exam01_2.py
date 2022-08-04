'''
문1-2) Start counter 문제  


<출력 예시>
height : 3 <- 층수 키보드 입력 
*
**
***
start 개수 : 6 
'''

# 함수 정의
'''
def StarCount(height):  
    # 층 개수, 별 개수 변수 선언 
    h_cnt=s_cnt = 0
    for r in range(1+height+1):
        print('*'*r)
        s_cnt+=r
    return s_cnt
'''
def StarCount(height):  
    # 층 개수, 별 개수 변수 선언 
    h_cnt=s_cnt=0
    while h_cnt < height:
        h_cnt+=1
        print('*'*h_cnt)
        s_cnt+=h_cnt
    return s_cnt

# 키보드 입력 & 함수 호출
star_cnt = StarCount(int(input('height : '))) # 층 수 입력

# start 개수 출력
print('start 개수 : %d'%star_cnt)

