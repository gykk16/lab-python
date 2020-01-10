'''

'''


# 함수 정의
def test(x: object, y: object) -> object:
    print(f'x = {x}, y = {y}')
    return x + y, x - y


# 함수 호출
# test()
# TypeError: test() missing 2 required positional arguments: 'x' and 'y'
# positional arguments: 함수를 호출할 때 전달하는 값(argument)들이 함수 정의에 선언된 파라미터 순서대로 전달되는 방식
plus, minus = test(1, 2)
plus, minus = test(2, 1)

# keyword arguments: 함수를 호출할 때, argument를 파라미터 = 값 형식으로 전달하는 방식
plus, minus = test(x = 10, y = 20)
print(minus)
plus, minus = test(y = 10, x = 20)
print(minus)

# default arguments: 함수를 정의할 때 파라미터의 기본값을 설정하는 것
def show_msg(msg: str = 'hello', times: int = 1) -> None:
    print(msg * times)

show_msg('졸리세요(?)', 5)
show_msg(',,,네 많이 졸려요')
show_msg()


# default argument를 갖는 파라미터는 반드시 default argument 를 갖지 않는 파라민터들이 선언된 뒤에 선언해야 함
def test2(x = 1, y):
    return x + y
test2(1)