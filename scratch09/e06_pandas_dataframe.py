'''
gapminder.tsv 파일을 읽어서 데이터 프레임 생성

'''
import os

import pandas as pd

df = pd.read_csv('gapminder.tsv', sep = '\t', encoding = 'UTF-8')
print(df.iloc[0:5])

# boolean indexing:
# 컬럼의 값을 이용해서 특정 레코드(행, row)들을 선택하는 방법
# DataFrame[컬럼의 값을 이용한 조건식]
df_afg = df[df['country'] == 'Afghanistan']
print(df_afg)

df_korea = df[df['country'] == 'Korea, Rep.']
print(df_korea)


# 대한민국(Korea, Rep.)의 인구(pop)과 1인당 GDP(gdpPercap)을 출력

print(df[df['country'] == 'Korea, Rep.'][['pop', 'gdpPercap']])
print(df_korea[['pop', 'gdpPercap']])


print('================ \n\n')

# mpg.csv 파일을 읽어서 DataFrame을 생성
# cty 컬럼의 값이 cty 평균보다 큰 자동차들의 model, cty, hwy를 출력

file_path = os.path.join('..', 'scratch08', 'mpg.csv')
mpg = pd.read_csv(file_path, encoding = 'UTF-8')
print(mpg.head())

# cty 평균 계산
cty_mean = mpg['cty'].mean()
print(cty_mean)
print('\n\n')
# cty 값이 평균보다 큰 레코드들을 출력
print(mpg[mpg['cty'] > cty_mean])
print('\n\n')
# cty 가 평균 이상인 자동차들의 model, cty, hwy 컬럼을 출력
df_1 = mpg[['model', 'cty', 'hwy']]
print(df_1[df_1['cty'] > cty_mean])

print('////////////')
print(mpg[['cty']])
print(type(mpg[['cty']]))


print(mpg['cty'])
print(type(mpg['cty']))


