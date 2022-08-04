'''
 문2) 다음과 같은 출력 결과가 나타나도록 동적 멤버 변수 생성으로 산포도(Scattering)
      클래스를 완성하시오.
      
      <수식>
      표본 분산 = sum((x변량-산술평균)**2) / n-1
      표본 표준편차 = sqrt(표본분산)

 << 출력 결과 >>
 분산 : 7.466666666666666
 표준편차 :  2.7325202042558927
'''

from statistics import mean
from math import sqrt

x = [5, 9, 1, 7, 4, 6]


class Scattering:
    data=[]

    def __init__(self, x): # 생성자
        self.data=x

    def var_func(self): # 분산 메서드
        su = sum([(i-mean(self.data))**2 for i in self.data])
        self.var = su/(len(self.data)-1)
        return self.var

    def std_func(self): # 표준편차 메서드
        self.var_func()
        std=sqrt(self.var)
        return std


scatt = Scattering(x)  # 생성자 -> 객체 생성
var = scatt.var_func()  # 분산 반환
st = scatt.std_func()  # 표준편차 반환

print('분산 = ', var)
print('표준편차 =', st)
'''
분산 =  7.466666666666666
표준편차 = 2.7325202042558927
'''


 
        
    
    



