'''
file.readline() 사용해서 csv 파일 읽기

'''
import os

def my_csv_reader(fn: str, header = True) -> list:
    '''
    csv 파일의 데이터를 2차원 행렬 형태로 리턴

    :param fn: 읽을 csv 파일 이름(예: data\\exam.csv)
    :param header: csv 파일의 헤더 존재 여부
    :return: csv 파일에서 헤더는 제외한 데이터들로 이루어진 2차원 리스트
   '''

    data = []

    with open(fn, mode = 'r', encoding = 'utf-8') as f:
        if header == False:
            f.readline()

        for line in f:
            # print(line.strip())
            text = line.strip()
            data.append(text.split(','))

    return data


def print_data(data: list) -> None:
    '''
    2차원 리스트의 내용을 출력

    :param data: 2차원 행렬 형태의 리스트
    :return: None
    '''

    for row in data:
        for i in row:
            print(i, end = ' ')
        print()


def get_sum_min(data: list, col: int) -> tuple:
    '''
    주어진 2차원 리스트(data)에서 해당 컬럼(col)의 데이터들의 총합(sum)과 평균(mean)을 계산해서 리턴

    :param data: 2차원 행렬 형태의 리스트
    :param col: 컬럼 인덱스(0, 1, 2, ... )
    :return:
    '''


if __name__ == '__main__':
    # 작성한 함수 테스트
    csv = my_csv_reader('data\exam.csv', header = True)
    print(type(csv))
    print(csv)
    print()
    print_data(csv)
    print()





