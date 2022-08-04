# 문5) 다음과 같이 단 수를 인수로 넘겨서 해당 구구단을 장식하여 함수 장식자를 정의하시오.
'''
<출력 예시>
*** 2단 ***
2 * 1 = 2
2 * 2 = 4
   :
2 * 9 = 18
***********
'''

def gugu_deco(gugu_dan) :
    def inner(dan):
        print('*** %s단 ***' %dan)
        gugu_dan(dan)
        print('***********')
    return inner
        

@gugu_deco 
def gugu_dan(dan):
    for i in range(1, 10) :
        print('%d * %d = %d'%(dan, i, dan*i))

gugu_dan(2)
'''
*** 2단 ***
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
2 * 6 = 12
2 * 7 = 14
2 * 8 = 16
2 * 9 = 18
***********
'''