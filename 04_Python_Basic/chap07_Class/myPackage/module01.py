# -*- coding: utf-8 -*-
"""
myPackage > module01.py > 함수 or 클래스
"""

# module: 함수 + 클래스 + 변수(명령문)
def Adder(x,y):
    add = x+y
    return add

class Mul:
    # 생성자
    def __init__(self,x,y):
        self.x=x
        self.y=y
    #메서드
    def mul(self):
        return self.x*self.y

# 변수(명령문): 다른 모듈에서 import 순간에 나타남
print(__name__) # __main__:약속된 명령어 -> 현재 모듈에서 실행 시 출력
# __name__: 현재 모듈의 이름 = 패키지명.모듈명
print('출력 외')

# print('add=',Adder(10,20)) # add= 30

# 모듈 시작점
# __name__ : 예약어
# __main__: 현재 실행 모듈의 이름
if __name__=='__main__': # 불필요한 내용 출력 방지
    print('add=',Adder(10,20))
    print('출력 내')
