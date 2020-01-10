import pandas as pd


if __name__ == '__main__':

    tips = pd.read_csv('tips.csv')
    print(tips.head())

    # DataFrame에 tip_pct 컬럼 추가: 팁금액 / 총금액
    print('\n === DataFrame에 tip_pct 컬럼 추가: 팁금액 / 총금액 ===')
    tips['tip_pct'] = tips['tip'] / tips['total_bill']
    print(tips)

    # day, smoker별 그룹을 지어서,
    # tip_pct의 평균을 출력
    print('\n === day, smoker별 그룹을 지어서, tip_pct의 평균을 출력 ===')
    tips_pct = tips.groupby(['day', 'smoker'])['tip_pct']
    print(tips_pct.mean())

    # day, smoker별 그룹의 tip_pct의 평균, 표준편차, 최대/최소 차이를 출력
    print('\n === day, smoker별 그룹의 tip_pct의 평균, 표준편차, 최대/최소 차이를 출력 ===')
    df = tips_pct.agg(MEAN = 'mean',
                      STD = 'std',
                      MaxMinRANGE = lambda x: x.max() - x.min())
    print(df)

    # day, smoker별 그룹의 tip_pct, total_bill 컬럼의 평균, 표준편차, 최대/최소 차이
    print('\n === day, smoker별 그룹의 tip_pct, total_bill 컬럼의 평균, 표준편차, 최대/최소 차이 ===')
    grouped = tips.groupby(['day', 'smoker'])
    tips_pct_total = grouped[['tip_pct', 'total_bill']]
    df = tips_pct_total.agg([('MEAN', 'mean'),
                             ('STD', 'std'),
                             ('MaxMinRANGE', lambda x: x.max() - x.min())])
    print(df)

    # GroupBy 객체의 컬럼들마다 다른 함수를 agg 로 적용할 때
    # agg({'col_name': [functions], ...})
    # 그룹핑된 데이터 프레임의 tip 컬럼에는 max() 함수를 aggregate 하고,
    # size 컬럼에는 sum() 함수를 aggregate 함.
    result = grouped.agg({'tip': 'max', 'size': 'sum'})
    print(result)

    functions = [('MEAN', 'mean'), ('STD', 'std'), ('MaxMinRANGE', lambda x: x.max() - x.min())]
    df = grouped.agg({
        'tip_pct': functions,
        'total_bill': functions
    })
    print(df)

    # grouping 컬럼들이 aggregate 결과에서 인덱스로 사용하지 않고자 할 때,
    grouped = tips.groupby(['day', 'smoker'], as_index = False)
    print(grouped['tip'].mean())

    df = grouped.agg({
        'tip_pct': functions,
        'total_bill': functions
    })
    print(df)