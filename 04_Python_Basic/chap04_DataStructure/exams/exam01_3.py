'''
step01 문제 

문3) 리스트(list)에 추가할 원소의 개수를 키보드로 입력 받은 후, 입력 받은 수 만큼
     임의 숫자를 리스트에 추가한다. 
     이후 리스트에서 찾을 값을 키보드로 입력한 후 리스트에 해당 값이 있으면 "YES",  
     없으면 "NO"를 출력하시오. 
          
<출력 예시1>
list 개수 : 5
1
2
3
4
5
3  <- 찾을 값 
YES

<출력 예시2>
list 개수 : 3
1
2
4
3 <- 찾을 값 
NO
'''

lst=[]
size = int(input('list 개수 : ')) # list 크기 입력
for i in range(size): # size만큼 반복
    lst.append(int(input("숫자를 입력하시오 "))) # size만큼 숫자 입력

# 숫자 찾기
get=int(input("찾을 값을 입력하시오. "))
if get in lst:
    print("Yes")
else:
    print("No")















