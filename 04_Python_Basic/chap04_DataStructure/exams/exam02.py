'''
step02 문제

문1) message에서 'spam' 원소는 1 'ham' 원소는 0으로 dummy 변수를 생성하시오.
      <조건> list + for 형식1) 적용   
      
  <출력결과>      
[1, 0, 1, 0, 1]   


문2) message에서 'spam' 원소만 추출하여 spam_list에 추가하시오.
      <조건> list + for + if 형식2) 적용   
      
  <출력결과>      
['spam', 'spam', 'spam']   

'''

message = ['spam', 'ham', 'spam', 'ham', 'spam']
print(message) # ['spam', 'ham', 'spam', 'ham', 'spam']

# 문1)
'''
message2=[]
for i in message:
    if i=='spam':
        message2.append(1)
    else:
        message2.append(0)
'''
message2=[1 if i=='spam' else 0 for i in message]
print(message2) # [1, 0, 1, 0, 1]

# 문2)
'''
message3=[]
for i in message:
    if i=='spam':
        message3.append(i)
'''
message3=[i for i in message if i=='spam']
print(message3) # ['spam', 'spam', 'spam']