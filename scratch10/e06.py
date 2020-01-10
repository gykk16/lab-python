import numpy as np
import pandas as pd


def squared_mean(data):
    ''' 데이터의 제곱의 평균을 리턴 '''
    squared_sum = 0
    for i in data:
        squared_sum += i ** 2
    return squared_sum /len(data)


def my_func(x):
    return x.min(), x.max(), x.mean(), squared_mean(x)


if __name__ == '__main__':
    df = pd.DataFrame({
        'pop': np.random.randint(1, 10, 4),
        'income': np.random.randint(1, 10, 4)
    }, index = ['a', 'b', 'c', 'd'])

    print(df)

    # agg(aggregate): DataFrame의 축(axis)을 기준으로 통계량을 집계(aggregate)하기 위한 함수
        # 통계량(statistics): 합계(sum), 평균(mean), 분산(var), 표준편차(std), 최소값(min), 최대값(max), 중앙값(median), ...
        # agg 함수는 집계가 목적이기 때문에 데이터 타입이 숫자 타입인 행/열에만 함수를 적용해 계산
        # agg 함수는 pandas나 numpy에서 제공하는 집계 함수들 이외에도 사용 사용자 정의 함수를 사용할 수 있음.
        # 단, 함수는 Series를 파라미터에 전달하면 숫자(Scalar)를 리턴하는 함수여야 한다

    print('=== agg by column ===')
    print(df.agg('mean'))   # 파라미터 axis 의 기본 값은 0(컬럼 방향)

    print('=== agg by row ===')
    print(df.agg('mean', axis = 1))

    print(df.agg(squared_mean))

    # apply: DataFrame에 축(axis)을 기준으로 함수를 적용(apply)하기 위한 함수
    #   적용하려는 함수는 pandas 객체(DataFrame, Series, Scalar)를 리턴하면 됨
    #   agg 함수는 숫자 타입 스칼라만 리턴하는 함수를 적용하는 apply의 특수한 경우

    print('=== apply by column ===')
    print(df.apply('mean'))   # 파라미터 axis 의 기본 값은 0(컬럼 방향)

    print('=== apply by row ===')
    print(df.apply('mean', axis = 1))


    print(df.agg(my_func))
    print(df.apply(my_func))
