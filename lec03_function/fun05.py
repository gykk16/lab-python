'''
가변 길이 인수(variable-length argument
함수를 호출할 때 전달하는 argument의 갯수가 다양하게 면하는 것
'''

print('a')
print('a', 'b', 'c', 'd', sep = ':')


def fn_vararg(*varargs):
    print(varargs)
    print(*varargs)
    # 가변 길이 인수들은 tuple처럼 취급하면 됨
    for arg in varargs:
        print(arg)


fn_vararg(1, 2, 3)
print()


def summation(*args):
    '''
    임의의 갯수의 숫자들을 전달 받아서 그 숫자들의 총합을 return하는 함수

    :param args: 합계를 계산할 숫자들(갯수 제한 없음)
    :return: 숫자들의 합
    '''

    x = 0
    for i in args:
        x += i

    return x


print(summation())
print(summation(1))
print(summation(1, 2, 3, 4, 5))

print()


def fn_vararg2(a, *b):
    print(f'a = {a}')
    print(f'b = {b}')


fn_vararg2(1)

print()


def fn_vararg3(*a, b):
    print(f'a = {a}')
    print(f'b = {b}')


# fn_vararg3()
# fn_vararg3(1)
# fn_vararg3(1, 2)
fn_vararg3(1, 2, b = 3)

print()


def calculator(*values, operator):
    '''
    operator 가 '+' 인 경우에는 values 들의 합계를 리턴하고,
    operator 가 '*' 인 경우에는 values 들의 곱을 리턴하는 함수

    :param values:
    :param operator:
    :return:
    '''
    x = 0
    if operator is '+':
        x = 0
        for i in values:
            x += i
    elif operator is '*':
        x = 1
        for i in values:
            x *= i

    return x


print(calculator(2, 10, operator = '+'))
print(calculator(2, 10, operator = '*'))
print(calculator(2, 10, operator = '/'))
