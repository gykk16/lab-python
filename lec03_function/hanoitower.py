# 재귀 함수를 이용한 하노이 탑

def hanoi(n, start = 'A', end = 'C', aux = 'B'):
    if n == 1:
        print(f'Move {n} from {start} to {end}')
    else:
        hanoi(n - 1, start, aux, end)
        print(f'Move {n} from {start} to {end}')
        hanoi(n - 1, aux, end, start)


def hanoi_tower(n, start, target, aux):
    '''
    재귀 함수를 사용한 하노이탑 문제 해결 방법 출력

    :param n: 원반의 갯수 (n > 0 인 정수)
    :param start: 시작 기둥
    :param target: 목표 기둥
    :param aux: 보조 기둥
    :return:
    '''

    if n == 1:
        print(f'Move {n} from {start} to {target}')
        return

    # (n - 1)개의 원반을 보조 기둥(aux)으로 옮기기
    hanoi_tower(n - 1, start, aux, target)
    print(f'Move {n} from {start} to {target}')
    # aux 에 남아 있는 (n - 1)개의 원반을 target으로 옮김
    hanoi_tower(n - 1, aux, target, start)


for n in range(1, 4):
    hanoi_tower(n, 'A', 'C', 'B')
    print('====================')
