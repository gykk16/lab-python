'''
통계

중심 경향성: 평균, 중앙값, 분위수(4분위, 100분위 = 퍼센트), 최빈값,

산포도: 분산(variance), 표준 편차(standard deviation), 범위(range)

상관관계: 공분산(covariance), 상관계수(correlation)

'''
from collections import Counter
import math
from scratch04 import dot

def mean(x):
    '''
    리스트 x의 모든 아이템들의 평균을 계산해서 리턴

    :param x: 원소 n개 인 (1차원) 리스트
    :return: 평균
    '''

    r = 0
    for i in x:
        r += i
    return r / len(x)


def median(x):
    '''
    리스트 x 를 정렬 했을때 중앙에 있는 값을 찾아서 리턴
    n 이 홀수이면, 중앙값을 찾아서 리턴,
    n 이 짝수이면, 중앙에 있는 두개 값의 평균을 리턴

    :param x: 원소 n개 인 (1차원) 리스트
    :return: 중앙값
    '''

    x1 = sorted(x)
    n = len(x1)
    mid = n // 2   # 리스트의 가운데 위치 인덱스
    if n % 2:
        r = x1[mid]
    else:
        r = (x1[mid - 1] + x1[mid]) / 2

    return r


def quantile(x, p):
    '''
    리스트 x의 p분위에 속하는 값을 찾아서 리턴

    :param x: 원소가 n개 인 (1차원) 리스트
    :param p: 0 ~ 1.0 사이의 값
    :return: 해당 분위수(퍼센트)의 값
    '''

    n = len(x)
    p_index = int(n * p) # 행당 퍼센트의 인덱스 - 소수점 버리기
    x1 = sorted(x)
    return x[p_index]


def mode(x):
    '''
    리스트에서 가장 자주 나타나는 값(최빈값)을 리턴
    최빈갑시 여러개인 경우, 최빈값들의 리스트를 리턴

    :param x: 원소가 n개인 (1차원) 리스트
    :return: 최빈값들의 리스트
    '''

    count = Counter(x)
    # print(count)
    # print(count.keys(), count.values()) # .keys(): 데이터(아이템), .values(): 빈도수
    # print(count.items())  # 값, 빈도수
    max_count = max(count.values()) # 빈도수의 최대값
    # r = []  # 최빈 값을 저장할 리스트
    # for val, cnt in count.items():
    #     if cnt == max_count:
    #         r.append(val)
    #
    # return r

    return [val for val, cnt in count.items() if cnt == max_count]


def data_range(x):
    '''


    :param x: 원소 n 인 (1차원) 리스트
    :return: 리슽의 최대값 - 리스트의 최소값
    '''

    return max(x) - min(x)


def variance(x):
    '''
    ((x1 - mean)**2 + (x2 - mean)**2 + ... + (xn - mean)**2) / (n - 1)

    :param x: 원소가 n 개인 (1차원) 리스트
    :return: 분산
    '''

    r = 0
    m = mean(x)
    # for i in x:
    #     r += (i - m)**2
    #
    # return r / len(x) - 1

    return sum([(i - m) ** 2 for i in x]) / (len(x) - 1)

def standard_deviation(x):
    '''
    sqrt(variance)

    :param x: 원소가 n 개인 (1차원) 리스트
    :return: 표준편차
    '''

    return math.sqrt(variance(x))


def covariance(x, y):
    '''
    공분산(covariance)
    Cov = sum((xi - x_bar)(yi - y_bar)) / (n - 1)

    :param x: 원소 n개 인 (1차원) 리스트
    :param y: 원소 n개 인 (1차원) 리스트
    :return: 공분산
    '''

    mean_x = mean(x)
    mean_y = mean(y)
    # r = 0
    # for i, j in zip(x, y):
    #     r += (i - m_x) * (j - m_y)
    #
    # return r / (len(x) - 1)

    return sum([(i - mean_x) * (j - mean_y) for i, j in zip(x, y)]) / (len(x) - 1)


def correlation(x, y):
    '''
    상관 계수(correlation)
    Corr = Cov(x, y) / (SD(x) * SD(y))

    :param x: 원소 n개 인 (1차원) 리스트
    :param y: 원소 n개 인 (1차원) 리스트
    :return:
    '''

    return covariance(x, y) / (standard_deviation(x) * standard_deviation(y))


if __name__ == '__main__':
    A = [1, 2, 2, 3, 3, 4, 4, 4, 5, 6, 6, 6, 100]
    B = [1, 2, 2, 3, 3, 4, 4, 4, 5, 6, 6, 100]
    print(A)
    print(mean(A))
    print(median(A))
    print(quantile(A, 0.75))


    print()

    print(B)
    print(mean(B))
    print(median(B))
    print(quantile(B, 0.25))

    print()
    print(mode(A))
    print(mode(B))

    print()
    print(variance(A))
    print(standard_deviation(A))

    print()
    A = [1, 2, 2, 3, 3, 4, 4, 4, 5, 6, 6, 99]
    B = [1, 2, 2, 3, 3, 4, 4, 4, 5, 6, 6, 100]
    print(covariance(A, B))
    print(correlation(A, B))

    print()
    x = [-3, -2, -1, 0, 1, 2, 3]
    y = [3, 2, 1, 0, 1, 2, 3]
    # y = |x|
    print(correlation(x, y))



