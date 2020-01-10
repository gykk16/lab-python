'''
2차원 리스트(list)를 이용한 행렬
'''


def shape(matrix):
    '''
    행렬의 행과 열의 개수를 tuple 형태로 리턴

    :param matrix: 행렬
    (행의 개수가 n 개이고 , 열의 개수가 m 개인 2차원 리스트
    :return: tuple (n, m)
    '''

    return len(matrix), len(matrix[0])


def get_row(matrix, index):
    '''
    주어진 행렬(matrix)에서 index에 해당하는 row를 리턴하는 함수

    :param matrix: n * m 행렬
    :param index: 행 번호
    :return: 벡터 (원소가 m개인 리스트)
    '''

    return matrix[index]

def get_col(matrix, index):
    '''
    주어진 행렬(matrix)에서 index에 해당하는 column을 리턴하는 함수

    :param matrix: n * m 행렬
    :param index: 열(column) 번호
    :return: 벡터 (원소가 n개인 리스트)
    '''

    list = []
    # for i in matrix:
    #     list.append(i[index])
    # return list
    return [i[index] for i in matrix]


def make_matix(nrows, ncols, fn):
    '''
    함수의 fn의 리턴 값들로 이루어진 nrows * ncols 행렬을 생성

    :param nrows: 행의 개수
    :param nclos: 열의 개수
    :param fn: 함수(fn(nrows, ncols) = 숫자)
    :return: nrows * ncols 행렬렬
   '''

    # m = []
    # for i in range(nrows):
    #     row = []
    #     for j in range(ncols):
    #         row.append(fn(i, j))
    #     m.append(row)
    # return m
    return [[fn(i, j) for j in range(ncols)] for i in range(nrows)]


def transpose(matrix):
    '''
    주어진 행렬에서 행과 열을 귀바꾼 행렬(전치행렬)

    :param matrix: n * m 행렬
    :return: m * n 행렬
    '''

    # m = []
    # for i in range(len(matrix[0])):
    #     new_row = get_col(matrix, i)
    #     m.append(new_row)
    #
    # return m

    # return [get_col(matrix, i) for i in range(len(matrix[0]))]

    nrows, ncols = shape(matrix)
    t = make_matix(ncols, nrows, lambda x, y: matrix[y][x])
    return t



def transpose(matrix):
    print('unpacking 연산자 * 를 사용한 transpose')
    # m = []
    # for col in zip(*matrix):
    #     m.append(list(col))
    # return m
    return [list(i) for i in zip(*matrix)]

if __name__ == '__main__':
    # 2 * 3 행렬 (row = 2, col = 3)
    A = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    # 3 * 2 행렬 (row = 3, col = 2)
    B = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]

    print(A)
    print('shape of A =', shape(A))
    print()
    print(B)
    print('shape of B =', shape(B))

    print()
    print('get_row of A =', get_row(A, 1))
    print('get_row of B =', get_row(B, 1))
    print('get_col of A =', get_col(A, 1))
    print('get_col of B =', get_col(B, 1))

    print()
    def plus(x, y):
        return x + y

    m = make_matix(2, 2, lambda x, y: x + y)
    print(m)

    def identity(x, y):
        # result = 0
        # if x == y:
        #     result = 1
        # else:
        #     result = 0

        # result = 1 if x == y else 0 # 3항 연산자
        # return result

        return 1 if x == y else 0

    identity_matrix = make_matix(3, 3, identity)
    print(identity_matrix)

    identity_matrix = make_matix(3, 3, lambda x, y: 1 if x == y else 0)
    print(identity_matrix)

    print()
    print()
    A = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    B = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]

    print('matrix A =', A)
    print('shape of A =', shape(A))

    transpose_A = transpose(A)
    print('transposed matrix A =', transpose_A)
    print('shape of transposed A =', shape(transpose_A))

    print()

    print('matrix B =', B)
    print('shape of B =', shape(B))

    transpose_B = transpose(B)
    print('transposed matrix B =', transpose_B)
    print('shape of transposed B =', shape(transpose_B))


    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [7, 8, 9]

    for x, y, z in zip(a, b, c):
        print(x, y, z)

    print()
    # unpacking 연산자: *
    print('A =', A)
    print('*A = ', *A)
    print('B =', B)
    print('*B = ', *B)