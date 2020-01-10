'''
 함수에서 return의 의미
 1) 함수를 종료
 2) 함수를 호출한 곳에 값을 반환(리턴)

 yield: 반복문 안에서만 함수의 결과를 반환할 때

'''



def test():
    x = 0
    while x < 4:
        return x
    x += 1 # 위에서 이미 리턴이 되었기 때문에 절대로 실행될 수 없는 코드

for i in range(4):
    print(test())


def four():
    x = 0
    while x < 4:
        yield x
        x += 1


print(four())
for x in four():
    print(x)