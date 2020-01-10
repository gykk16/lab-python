'''
함수 정의:
(1)
def 함수이름(파라미터 선언, ...):
    함수 기능 작성
    [return 값]

(2)
def 함수이름(파라미터: 타입, 파라미터2: 타입, ...) -> 리턴타입:
    함수 기능 작성
    [return 값]
'''


def substract(x: int, y: int) -> int:
    return x - y

result = substract(1, 2)
print(result)

result = substract(1.1, 0.9)
print(result)



def my_sum(numbers: list) -> float:
    '''
    숫자(int, float)들이 저장된 리스트를 전달받아서, 모든 원소들의 합을 리턴하는 함수

    :param numbers: 숫자들이 저장되 리스트
    :return: 리스트의 모든 원소들의 합
    '''

    x = 0
    for i in numbers:
        x += i

    return x

result = my_sum([1, 2, 3, 4, 6])
print(result)
result = my_sum([1.0, 10.0, 100.0])
print(result)

print()
def my_mean(numbers: list) -> float:
    '''
    숫자들을 저장하는 리스트를 전달 받아서, 모든 원소들의 평균을 계산해서 리턴

    :param numbers: 숫자들을 저장한 리스트
    :return: 리스트의 모든 원소들의 평균
    '''

    x = 0
    for i in numbers:
        x += i
    x /= len(numbers)

    # return x
    return my_sum(numbers) / len(numbers)

result = my_mean([1, 2, 3, 4, 5])
print(result)
result = my_mean([1.0, 10.0, 100.0])
print(result)