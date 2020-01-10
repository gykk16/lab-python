# 1부터 n 까지의 숫자들의 합을 리턴하는 함수
# 1 + 2 + 3 + ... + n
def sum_to_n(n: int) -> int:
    x = 0
    for i in range(n + 1):
        x += i

    return x


def sum_to_n2(n: int) -> float:
    return (n * (n + 1)) / 2


print(sum_to_n(9))
print(sum_to_n2(9))
print()


# 1 부터 n 까지 숫자들의 제곱의 합을 리턴하는 함수
# 1**2 + 2**2 + 3**2 + ... n**2
def sum_to_sqr(n: int) -> int:
    x = 0
    for i in range(n + 1):
        x += i ** 2

    return x


def sum_to_sqr2(n: int) -> float:
    return n * (n + 1) * (2 * n + 1) / 6


print(sum_to_sqr(5))
print(sum_to_sqr2(5))
print()


# 숫자들의 리스트를 전달 받아서 최대값을 찾아서 리턴하는 함수
def find_max(list: list) -> int:
    x = list[0]
    for i in list:
        if x < i:
            x = i

    return x


def find_max2(list: list) -> int:
    x = sorted(list, reverse = True)

    return x[0]


print(find_max([1, 2, 3, 4, 5]))
print(find_max([-5, -10, -100]))
print(find_max2([1, 2, 3, 4, 5]))
print(find_max2([-5, -10, -100]))
print()


# 숫자들의 리스트를 전달 받아서 최대값의 인덱스를 리턴하는 함수
def find_max_index(list: list) -> int:
    x = find_max(list)

    return list.index(x)


def find_max_index2(list: list) -> int:
    max_id, max_val = 0, list[0]
    for i, v in enumerate(list):
        if v > max_val:
            max_id, max_val = i, v

    return max_id


def find_max_index3(list: list) -> int:
    _max = list[0]
    x = 0
    for i in range(len(list)):
        if list[i] > _max:
            _max = list[i]
            x = i

    return x


print(find_max_index([1, 2, 3, 4, 5]))
print(find_max_index([-5, -10, -100]))
print(find_max_index2([1, 2, 3, 4, 5]))
print(find_max_index2([-5, -10, -100]))
print(find_max_index2([1, 2, 3, 4, 5]))
print(find_max_index3([-5, -10, -100]))
print()


# 숫자들의 리스트를 전달 받아서 중앙값을 리턴하는 함수
def find_median(list: list) -> int:
    list2 = sorted(list)
    x = len(list2) / 2
    if int(x) != x:
        x = int(x)
        x = list2[x]
    elif int(x) == x:
        x = int(x)
        x = (list2[x] + list2[x - 1]) / 2

    return x


print(find_median([1, 2, 3, 4, 5]))
print(find_median([1, 2, 3, 4, 5, 6]))

print(find_median([2, 10, 8, 4, 6]))
print(find_median([2, 6, 10, 12, 8, 4]))
print()


def find_median2(list: list) -> float:
    list_sorted = sorted(list)
    length = len(list_sorted)   # 리스트의 크기
    mid = length // 2   # 리스트의 중간 위치
    if length % 2:  # 리스트의 원소 갯수가 홀수인 경우
        v = list_sorted[mid]
    else:  # 리스트의 원소 갯수가 짝수인 경우
        mid_1 = mid - 1
        v = (list_sorted[mid_1] + list_sorted[mid]) / 2

    return v


print(find_median2([2, 10, 8, 4, 6])) # 2, 4, 6, 8, 10
print(find_median2([2, 6, 10, 12, 8, 4])) # 2, 4, 6, 8, 10, 12





