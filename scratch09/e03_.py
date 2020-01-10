'''
1) csv 파일(stock_price.csv) write

    6/20/2019,AAPL,90.91
    6/20/2019,MSFT,41.68
    6/21/2019,AAPL,90.86
    6/21/2019,MSFT,41.51

2) csv 파일을 csv.reader를 사용해서 파일의 내용을 리스트로 변환
   각 주식 종목의 주식 가격 평균을 계산해서 출력

3) csv 파일을 csv.DictReader를 사용해서 파일의 내용을 리스트로 변환
   각 주식 종목의 주식 가격 평균을 계산해서 출력

'''
import csv

from numpy import mean

row1 = ['6/20/2019', 'AAPL', 90.91]
row2 = ['6/20/2019', 'MSFT', 41.68]
row3 = ['6/21/2019', 'AAPL', 90.86]
row4 = ['6/21/2019', 'MSFT', 41.51]
result = [row1, row2, row3, row4]


# 1) ############
with open('stock_price.csv', mode = 'w', encoding = 'UTF-8', newline = '') as f:
    writer = csv.writer(f, delimiter = ',')
    [writer.writerow(i) for i in result]

# 2) ############
with open('stock_price.csv', mode = 'r', encoding = 'UTF-8') as f:
    reader = csv.reader(f)
    df = [i for i in reader]

print(df)

aapl_price = [float(i[2]) for i in df if i[1] == 'AAPL']
msft_price = [float(i[2]) for i in df if i[1] == 'MSFT']

print(aapl_price)
print(msft_price)

aapl_mean = mean(aapl_price)
msft_mean = mean(msft_price)
print(f'AAPL mean = {aapl_mean} , MSFT mean = {msft_mean}')

print()

# 3) ############
with open('stock_price.csv', mode = 'r', encoding = 'UTF-8') as f:
    reader = csv.DictReader(f, fieldnames = ['date', 'stock', 'price'])
    df_dict = [i for i in reader]

print(df_dict)

aapl_mean = mean([float(i['price']) for i in df_dict if i['stock'] == 'AAPL'])
msft_mean = mean([float(i['price']) for i in df_dict if i['stock'] == 'MSFT'])
print(f'AAPL mean = {aapl_mean} , MSFT mean = {msft_mean}')



