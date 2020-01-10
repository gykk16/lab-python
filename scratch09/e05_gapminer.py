'''
gapminer.tsv 파일을 pandas 패키지의 read_csv() 함수를 사용해서 DataFrame 으로 변환

    행과 열의 갯수 확인
    앞쪽 데이터 5건 출력
    뒷쪽 데이터 5건 출력
    컬럼 이름들을 출력
    데이터 타입 출력
    'country', lifeExp', 'gdpPercap' 컬럼 출력
    행 인덱스가 0, 99, 999 인 행들을 출력
    행 레이블이 840 ~ 851인 행들의 나라이름, 기대수면, 1인당 gdp 출력
    ============
    연도별(year)별 기대 수명의 평균을 출력
    연도별(year)별, 대륙(continent)별 기대 수명의 평균을 출력

'''
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file_path = os.path.join('gapminder.tsv')

df = pd.read_csv(file_path, delimiter = '\t')
print(df)
print('================\n')
#     행과 열의 갯수 확인
print(df.shape)
print('================\n')
#     앞쪽 데이터 5건 출력, 뒷쪽 데이터 5건 출력
print(df.head())
print()
print(df.tail())
print('================\n')
#     컬럼 이름들을 출력
print(df.columns)
print('================\n')
#     데이터 타입 출력
print(df.dtypes)
print('================\n')
#     'country', lifeExp', 'gdpPercap' 컬럼 출력
print(df[['country', 'lifeExp', 'gdpPercap']])
print('================\n')
#     행 인덱스가 0, 99, 999 인 행들을 출력
print(df.iloc[[0, 99, 999]])
print('================\n')
#     행 레이블이 840 ~ 851인 행들의 나라이름, 기대수면, 1인당 gdp 출력
print(df.loc[840:851, ['country', 'lifeExp', 'gdpPercap']])
# print(df.iloc[840:852, [0, 3, 5]])
print('================\n')
print('================\n')
print('================\n')
#     ============
#     연도별(year)별 기대 수명의 평균을 출력
print(df.groupby('year').agg({'lifeExp': np.mean}))
print()
print(df.groupby('year')['lifeExp'].mean())
print('================\n')
#     연도별(year)별, 대륙(continent)별 기대 수명의 평균을 출력
print(df.groupby(['year', 'continent']).agg({'lifeExp': np.mean}))
print()
print(df.groupby(['year', 'continent'])['lifeExp'].mean())


#############################
# 연도별 기대수명 그래프
year_lifeExp = df.groupby('year')['lifeExp'].mean()
print(year_lifeExp)
plt.plot(year_lifeExp)
plt.show()

############################
# 연도별 전세계 인구수(pop) 그래프
year_pop = df.groupby('year')['pop'].sum()
print(year_pop)
plt.plot(year_pop)
plt.title('pop by year')
plt.show()

