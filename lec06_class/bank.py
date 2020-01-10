'''
lec06\class08_2_acc.py 파일에서 정의한 Account 클래스를 사용해서 은행 APP 작성

1) 개좌 개설
2) 입금
3) 출금
4) 이체


'''

from lec06_class.class08_2_acc import Account

print('Glory BANK')
# 여러개의 계좌들을 관리하기 위한 dict를 선언
#   key: 계좌번호, value: Account 객체
accounts = {}  # empty dict

while True:
    print('--- 메인 메뉴 ---\n')
    print('[1] 계좌 개설')
    print('[2] 계좌 조회')
    print('[3] 입금')
    print('[4] 출금')
    print('[5] 이체')

    print('[0] 종료')
    print('---------------')
    menu = input('선택 >>> ')

    if menu == '0':
        break

    elif menu == '1':  # 계좌 개설 선택
        print('--- 신규 계좌 개설 ---\n')
        account_no = int(input('계좌번호 입력 >>> '))
        money = float(input('잔액 입력 >>> '))
        accounts[account_no] = Account(account_no, money)
        print()

    elif menu == '2':
        print('\n --- 계좌 조회 화면 ---\n')
        account_no = int(input('조회할 계좌 입력 >>> '))
        print(f'{accounts[account_no]}\n')

    elif menu == '3':
        print('\n --- 입금 화면 ---\n')
        account_no = int(input('입금 계좌번호 입력 >>> '))
        money = float(input('입금 금액 입력 >>> '))
        accounts[account_no].deposit(money)

    elif menu == '4':
        print('\n --- 출금 화면 ---\n')
        account_no = int(input('출금 계좌번호 입력 >>> '))
        money = float(input('출금 금액 입력 >>> '))
        accounts[account_no].withdraw(money)

    elif menu == '5':
        print('\n --- 이체 화면 ---\n')
        from_acc = int(input('출금 계좌번호 입력 >>> '))
        to_acc = int(input('입금 계좌번로 입력 >>> '))
        money = float(input('이체 금액 입력 >>> '))
        accounts[from_acc].transfer(accounts[to_acc], money)


print('\n APP 종료')
