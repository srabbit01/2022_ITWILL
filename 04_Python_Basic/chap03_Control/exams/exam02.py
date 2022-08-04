'''
문2) 다음과 같이 아메리카노 3잔만 제공하는 커피 자판기를 구현하시오.
     (커피 한 잔은 2500원이라고 가정한다.)
     조건1> 2500원 미만, 금액이 부족합니다. 반복 수행
     조건2> 2500원 이상, 맛있게 드세요. 잔돈 표시, 커피 잔 빼기
     조건3> 2500원 이면, 맛있게 드세오. 커피 잔 빼기
     조건4> 커피 3잔을 모두 판매하면 프로그램 종료
'''

print("==" * 15)   
print('아메리카노 커피 자판기 동작')
print('가격은 2,500원')
print('커피는 3잔만 판매 가능')
print("==" * 15)

coffee = 3 # 커피 3잔

while True: # 무한 반복
    money = int(input('투입 금액을 입력하시오. '))
    if coffee == 0: # 종료 조건
        print('~~ 장사 끝 ~~')
        break
    else:
        if money < 2500:
            print('금액이 부족합니다.')
        elif money == 2500:
            coffee -= 1 # 커피잔 빼기: coffee=coffee-1
            print('맛있게 드세요.')
            print('남은 커피는 %d잔입니다.' %coffee)
        else:
            coffee -= 1
            print('맛있게 드세요.')
            print('잔돈: {0:3,d}원'.format(money-2500))
            print('남은 커피는 %d잔입니다.' %coffee)
# My case

coffee = 3 # 커피 3잔

while coffee != 0: # 무한 반복
    money = int(input('투입 금액을 입력하시오. '))
    if money < 2500:
        print('금액이 부족합니다.')
    elif money == 2500:
        coffee -= 1
        print('맛있게 드세요.')
        print('남은 커피는 %d잔입니다.' %coffee)
    else:
        coffee -= 1
        print('맛있게 드세요.')
        print('잔돈: {0:3,d}원'.format(money-2500))
        print('남은 커피는 %d잔입니다.' %coffee)
              
    if coffee == 0: # 종료 조건
        print('~~ 장사 끝 ~~')
