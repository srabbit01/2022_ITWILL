# -*- coding: utf-8 -*-
"""
step06_Account.py

은행 계좌 클래스
멤버변수: 예금주, 계좌번호, 잔액 = 상태 (명사)
매서드: 잔액 확인하기, 입금하기, 출금하기 = 동작 (동사)
"""
class Account:
    
    def __init__(self,name,no,bal):
        self.__name=name # 예금주
        self.__no=no # 계좌번호
        self.__balance=bal # 잔액
    
    # getter: 획득자(은닉변수를 넣어주는 것)
    # 잔액 확인
    def getBalance(self):
        
        return self.__balance
    # 계좌번호 확인
    def getNo(self):
        return self.__no
    # 예금주 확인
    def getName(self):
        return self.__name
    
    # setter: 지정자
    # 입금하기
    def deposit(self,money):
        if money>0:
            self.__balance+=money
        else:
            print('~입금 금액 확인~') # 예외처리
    # 출금하기    
    def withdraw(self,money):
        if 0 < money <= self.__balance:
            self.__balance-=money
        elif money <= 0:
            print('~출금 금액 확인~')
        else:
            print('~잔액 부족~')
    
# 사용자 입력
'''
name=input("예금주 : ")
no=input('계좌번호 : ')
bal=int(input('잔액(원) : '))
'''
name='홍길동'; no='123-1234-12345'; bal=1000
# 계좌1 생성
acc1=Account(name,no,bal)

# 예금주 확인
# acc1.__name # AttributeError # 직접 접근 불가능 -> 정보보안 목적

# 은닉 변수는 자신의 객체를 이용하여 확인 불가능
print('예금주 :',acc1.getName())
print('계좌번호 :',acc1.getNo())
print('현재 잔액 : {0:3,d}원'.format(acc1.getBalance()))

# 입/출금
'''
in_money=int(input('입금액(원) : '))
out_money=int(input('출금액(원) : '))
'''
# 입금
acc1.deposit(-1000) # ~입금 금액 확인~
acc1.deposit(5000) # 현재 잔액 : 6,000원
print('현재 잔액 : {0:3,d}원'.format(acc1.getBalance()))
# 출금
acc1.withdraw(-1000) # ~출금 금액 확인~
acc1.withdraw(7000) # ~잔액 부족~
acc1.withdraw(2000) # 현재 잔액 : 4,000원
print('현재 잔액 : {0:3,d}원'.format(acc1.getBalance()))

# 계좌2 생성
acc2=Account('유관순','123-4567-56789',0)
print('현재 잔액 : {0:3,d}원'.format(acc2.getBalance()))
# 현재 잔액 :   0원