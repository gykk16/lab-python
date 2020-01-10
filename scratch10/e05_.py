import numpy as np
import pandas as pd


def squares(x):
    return x ** 2


def doubles(x):
    return x * 2


if __name__ == '__main__':
    result1, result2 = squares(3), doubles(3)
    print(result1, result2)

    array = np.array([1, 2, 3])
    result1, result2 = squares(array), doubles(array)
    print(f'squares = {result1}, doubles = {result2}')

    df = pd.DataFrame({
        'a': [1, 2, 3],
        'b': [4, 5, 6]
    })
    print(df)
    print(squares(df))

    result = df.apply(squares, axis = 1)
    print(result)

    print(np.sum([1, 2, 3]))
    result = df.apply(np.sum, axis = 0)
    print(result)

    result = df.apply(np.sum, axis = 1)
    print(result)
    # DataFrame.apply(function, axis)
    # axis = 0(기본값) , DataFrame 의 각 컬럼을 함수의 파라미터에 전달
    # axis = 1 , DataFrame 의 각 행(row)을 함수의 파라미터에 전달
    # 함수의 리턴 값을 돌려받음
    # agg(aggregate) 함수는 GroupBy 객체에서만 사용 가능
    # apply는 DataFrame과 GroupBy 객체 모두에서 사용 가능


