'''
선형 대수(Linear Algebra)

'''

import math


def add(v, w):
    '''
    주어진 두개의 n 차원 벡터에서 성분별로 더하기를 해서, 새로운 n 차원 벡터를 리턴

    :param v: n 타원 벡터(성분이 n개인 벡터)
    :param w: n 타원 벡터(성분이 n개인 벡터)
    :return: 각 성분별로 더하기 결과를 갖는 벡터터
   '''

    x = []
    # for i, j in zip(v, w):
    #     x.append(i + j)
    # return x

    # for i in range(len(v)):
    #     x.append(v[i] + w[i])
    # return x

    if len(v) != len(w):
        raise ValueError('v 와 w 는 길이가 같아야 합니다.')

    return [v_i + w_i for v_i, w_i in zip(v, w)]


def substract(v, w):
    '''
    주어진 두개의 n 차원 벡터에서 성분별로 더하기를 해서, 새로운 n 차원 벡터를 리턴

    :param v: n 타원 벡터(성분이 n개인 벡터)
    :param w: n 타원 벡터(성분이 n개인 벡터)
    :return: 각 성분별로 더하기 결과를 갖는 벡터터
   '''

    # x = []
    # for i, j in zip(v, w):
    #     x.append(i - j)
    # return x

    if len(v) != len(w):
        raise ValueError('v 와 w 는 길이가 같아야 합니다.')

    return [v_i - w_i for v_i, w_i in zip(v, w)]


def vector_sum(vectors):
    '''
    모든 벡터들에서 각 성분별 더하기를 수행
    vector_sum([[1, 2], [3, 4], [5, 6]]) = [9, 12]

    :param vectors: n 차원 벡터들의 리스트(2차원 리스트)
    :return: n 차원 벡터
    '''

    num_of_elements = len(vectors[0])
    for vector in vectors[1:]:
        if num_of_elements != len(vector):
            raise ValueError('길이가 같아야 합니다.')

    # result = [0 for _ in range(num_of_elements)]
    # for i in range(num_of_elements):
    #     for vector in vectors:
    #         result[i] += vector[i]
    #
    # return result

    result = vectors[0]
    for i in vectors[1:]:
        result = add(result, i)
    return result


def scalar_multiply(c, vector):
    '''
    c * [x1, x2, x3 ... ] = [c * x1, c * x2, x * x3, ... ]

    :param c: 숫자(스칼라, scalar)
    :param vector: n 차원 벡터
    :return: n 차원 벡터
    '''

    return [c * v_i for v_i in vector]


def dot(v, w):
    '''
    [v1, v2, v3 ... ] · [w1, w2, w3, ... ] = v1*w1 + v2*w2 + v3*w3 + ...

    :param v: n 차원 벡터
    :param w: n 차원 벡터
    :return:
    '''

    if len(v) != len(w):
        raise ValueError('두 벡터의 길이가 같아야 합니다.')

    # x = [v_i * w_i for v_i, w_i in zip(v, w)]
    # r = 0
    # for i in x:
    #     r += i
    # return r

    r = 0
    for v_i, w_i in zip(v, w):
        r += v_i * w_i

    return r


def vector_mean(vectors):
    '''
    주어진 벡터들의 리스트에서 각 항목별 평균으로 이루어진 벡터

    :param vectors: n 차원 벡터들의 리스트
    (길이가 n 인 1차원 리스트를 아이테으로 갖는 2차원 리스트
    :return: n 차원 벡터(길이가 n 인 1치원 리스트)
    '''

    num_of_elements = len(vectors[0])
    for i in vectors[1:]:
        if num_of_elements != len(i):
            raise ValueError('길이가 같아야 합니다.')

    length = len(vectors)
    r = vector_sum(vectors)
    return scalar_multiply(1 / length, r)


def sum_of_squares(vector):
    '''
    vector = [x1, x2, ... xn] 일때,
    x1**2 + x2**2 + ... + xn**2을 리턴

    :param vector: n 차원 벡터(길이가 n 인 1차원 리스트)
    :return: 숫자
    '''

    # r = 0
    # for x_i in vector:
    #     r += x_i ** 2   # x_i * x_i
    # return r

    return dot(vector, vector)


def magnitude(vector):
    '''
        벡터의 크기를 리턴

    :param vector:
    :return:
    '''

    return math.sqrt(sum_of_squares(vector))


def squared_distance(v, w):
    '''
    (v1 - w1)**2 + (v2 - w2)**2 + ... + (vn - wn)**2 리턴

    :param v: n 차원 벡터(길이가 n 인 1차원 리스트)
    :param w: n 차원 벡터(길이가 n 인 1차원 리스트)
    :return: 숫자
    '''
    # r = [v_i - w_i for v_i, w_i in zip(v, w)]
    # return sum_of_squares(r)

    return sum_of_squares(substract(v, w))


def distance(v, w):
    '''
    두 벡터 v 와 w 사이의 거리를 리턴
    sqrt(squared_distance)

    :param v: n 차원 벡터(길이가 n 인 1차원 리스트)
    :param w: n 차원 벡터(길이가 n 인 1차원 리스트)
    :return:
    '''

    return math.sqrt(squared_distance(v, w))


if __name__ == '__main__':
    v = [1, 2]
    w = [3, 4]

    r = add(v, w)
    print(r)

    v = [10, 9, 8]
    w = [1, 2, 3]
    r = substract(v, w)
    print(r)

    print()
    vectors = [[1, 2], [3, 4], [5, 6]]
    r = vector_sum(vectors)
    print(r)

    print()
    v = [1, 3, 5]
    r = scalar_multiply(2, v)
    print(r)

    print()
    v = [2, 3]
    unit_x = [1, 0]  # x 축 단위 벡터
    unit_y = [0, 1]  # y 축 단위 벡터
    dot_x = dot(v, unit_x)
    print('dot1 =', dot_x)
    dot_y = dot(v, unit_y)
    print('dot2 =', dot_y)

    print()
    vectors = [[1, 2, 3],
               [3, 4, 5],
               [5, 6, 7],
               [7, 8, 9]]
    r = vector_mean(vectors)
    print(r)

    print()
    v = [3, 4]
    ss = sum_of_squares(v)
    print('sum of squares =', ss)

    norm = magnitude(v)
    print('magnitude =', norm)

    print()
    v = [1, 2]
    w = [3, 4]
    r = squared_distance(v, w)
    print(r)
    r = distance(v, w)
    print(r)


