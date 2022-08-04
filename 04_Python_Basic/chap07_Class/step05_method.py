'''
method 유형: 클래스 내 정의한 함수
 1. instance method : 객체.method() 호출, (self) 기본 인수
    -> 객체 생성 시점에서 만들어진 매서드: 일반/수정 메서드
    -> 반드시, 객체가 생성되어야 사용 가능
 2. class method : 클래스.method() 호출, (cls) 기본 인수 
    -> 객체를 만들지 않아도 클래스 이름 자체로도 호출 가능한 매서드
'''

class datePro :
    
    # 생성자 
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    # instance method: object.method
    def display(self):
        print(f"생년월일 : {self.year}년 {self.month}월 {self.day}일")
    
    # class method:class.method()
    @classmethod # 함수 장식자: 하단의 매서드 꾸밈 -> 클래스 매서드가 되 수 있도록 꾸밈
    # 클래스 매서드 선언: 함수 장식자에 의해 클래스 매서드 임을 선언
    def date_string(cls, dateStr):  # 함수 호출 방식
        year = dateStr[:4]
        month = dateStr[4:6]
        day = dateStr[6:]
        print(f'생년월일 : {year}년 {month}월 {day}일') # 1995 10 25
        
# object 생성
dateObj = datePro(1995, 10, 25)

# object.method()(
dateObj.display() # 생년월일 : 1995년 10월 25일

dateObj.date_string('19951025') # 생년월일 : 1995년 10월 25일
# 클래스 매서드도 객체 이용하여 호출 가능

# class.method() # 객체 생성하지 않아도 즉시 호출 가능
datePro.date_string('19951225') # 생년월일 : 1995년 12월 25일


# date 모듈
from datetime import date
# class.classmethod()
print(date.today()) # 2022-04-15

