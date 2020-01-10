'''
선택 정렬 알고리즘

'''
import numpy as np


def find_min(numbers: list):
    '''
    주어진 리스트에서 최소값과 최소값의 인덱스를 리턴하는 함수

    :param numbers: 숫자들의 리스트
    :return: 최소값의 인덱스, 최소값
    '''
    min_id, min_value = 0, numbers[0]
    for i, v in enumerate(numbers):
        if v < min_value:
            min_id, min_value = i, v

    return min_id, min_value


def find_max(numbers: list):
    '''
    주어진 리스트에서 최소값과 최소값의 인덱스를 리턴하는 함수

    :param numbers: 숫자들의 리스트
    :return: 최소값의 인덱스, 최소값
    '''
    max_id, max_value = 0, numbers[0]
    for i, v in enumerate(numbers):
        if v > max_value:
            max_id, max_value = i, v

    return max_id, max_value


def sel_sort(numbers):
    '''
    주어진 리스트의 원소들이 정렬된 새로운 리스트를 생성해서 리턴
    주어진 리스트(파라미터에 전달된 리스트)의 순서는 바뀌지 않음

    :param numbers:
    :return:
    '''
    num_copy = numbers.copy()
    result = []  # 빈 리스트 생성
    while num_copy:  # numbers의 원소가 있는 동안에
        # print('numbers =', numbers)
        # print('result =', result)
        _, min_value = find_min(num_copy)  # 최소값을 찾음
        result.append(min_value)  # 결과 리스트 추가
        num_copy.remove(min_value)  # 원본에서 최소값 삭제

    return result


numbers = [np.random.randint(0, 101) for i in range(5)]
print(numbers)
print(sel_sort(numbers))
print()


def sel_sort2(numbers: list):
    '''
    주어진 리스트를 정렬하는 함수
    새로운 리스트를 생성하지 않고, 원본 리스트의 순서를 바꿈

    :param numbers:
    :return:
    '''
    length = len(numbers)
    for i in range(0, length - 1):
        # i: 최소값을 옮길 위치
        for j in range(i + 1, length):
            # j: 최소값을 찾기 위해서 비교할 원소들의 인덱스
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
                # print(numbers)

    return numbers


numbers = [np.random.randint(0, 101) for i in range(5)]
print(numbers)
print(sel_sort2(numbers))
print()

####################################################################
####################################################################
####################################################################

def sel_sort3(numbers: list, reverse: bool = False) -> list:
    '''
    주어진 리스트의 원소들이 정렬된 새로운 리스를 생성해서 리턴
    주어진 리스트(차라미터에 전달된 리스트)의 순서는 바뀌지 않음

    :param numbers:
    :param reverse: False이면 오름차순, True이면 내림차순 정렬. 기본값은 False.
    :return:
    '''
    num_copy = numbers.copy()
    result = []

    while num_copy:
        if reverse:
            _, find = find_max(num_copy)
        else:
            _, find = find_min(num_copy)

        result.append(find)
        num_copy.remove(find)

    return result


print('sel_sort3')
numbers = [np.random.randint(0, 101) for i in range(5)]
print(f'원본 : {numbers}')
print(f'오름 : {sel_sort3(numbers)}')
print(f'내림 : {sel_sort3(numbers, reverse = True)}')
print()

def sel_sort4(numbers: list, reverse: bool = False):
    '''
    주어진 리스트를 정렬하는 함수
    새로운 리스트를 생성하지 않고, 원본 리스트의 순서를 바꿈

    :param numbers:
    :param reverse: False이면 오름차순, True이면 내림차순 정렬. 기본값은 False.
    :return:
    '''
    length = len(numbers)

    for i in range(0, length - 1):
        for j in range(i + 1, length):
            if reverse:
                if numbers[i] < numbers[j]:
                    numbers[i], numbers[j] = numbers[j], numbers[i]
            else:
                if numbers[i] > numbers[j]:
                    numbers[i], numbers[j] = numbers[j], numbers[i]

    return numbers


print('sel_sort4')
numbers = [np.random.randint(0, 101) for i in range(5)]
print(f'원본 : {numbers}')
print(f'오름 : {sel_sort4(numbers)}')
print(f'내림 : {sel_sort4(numbers, reverse = True)}')
print()