'''
람다 표현식(lambda expression)
    함수의 이름 없이, 함수의 매개변수 선언과 리턴 값으로만 표현하는 방법

lambda [p1, p2, ...]: 식(expression)

'''


multiplication = lambda x, y: x * y
result = multiplication(11, 11)
print(result)


division = lambda x, y: x / y
result = division(1, 2)
print(result)


# 람다 표현식은 함수의 매개변수로 함수를 전달할 때 많이 사용함
def calc(x, y, op):
    return op(x, y)

result = calc(1, 2, lambda x, y: x + y)
print(result)


# 람다 표현식을 사용한 함수 예
def my_filter(values, func):
    '''

    :param values: 리스트
    :param func: True/ False를 리턴하는 함수
    :return: 필터링 된 새로운 리스트
    '''

    result = [] # 빈 리스트 생성
    for item in values: # 리스트의 모든 원소들에 대해서 반복
        if func(item):  # 필터링 조건 함수 func의 리턴 값을 검사
            result.append(item)

    return result


numbers = [1, -2, 3, -4, -5, 6, -7, 8]
positives = my_filter(numbers, lambda x: x > 0)
print(positives)
evens = my_filter(numbers, lambda x: x % 2 == 0)
print(evens)


languages = ['python', 'r', 'pl/sql', 'java', 'c/c++']
more_than_5 = my_filter(languages, lambda x: len(x) > 5)
print(more_than_5)


def my_filter2(values, func):
    return [x for x in values if func(x)]

print(my_filter2(numbers, lambda x : x > 0))


#########################################

def my_mapper(values, func):
    '''

    :param values: 리스트
    :param func: 파라미터 1개인 함수
    :return: dict
    '''

    result = {} # 비어 있는 dict 생성
    for item in values:
        # dict의 키는 item, dict의 값(value)는 함수 func의 리턴 값
        result[item] = func(item)

    return result


result = my_mapper(languages, lambda x: len(x))
print(result)

def my_mapper2(values, func):
    return {k: func(k) for k in values}

print(my_mapper2(languages, lambda x: len(x)))