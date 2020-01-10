class Account:
    '''
    은행 계좌 클래스

    field(데이터): 계좌번호(acc_no), 잔액(balance),
    method(기능): 입금(deposit), 출금(withdraw), 이체(transfer)

    '''

    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance
        try:
            temp = balance + 1
        except Exception:
            raise TypeError()

    def __repr__(self): # 객체 표현식
        return f'Account no.: {self.acc_no}, Balance: {self.balance}'


    def deposit(self, x):
        if x < 0:
            raise ValueError('입금 금액이 잘못 되었습니다.')
        self.balance += x
        print(f'입금 전 : {self.balance - x} \n'
              f'입금 후 : {self.balance} \n'
              f'입금이 완료되었습니다.')


    def withdraw(self, x):
        if x < 0:
            raise ValueError()
        elif self.balance < x:
            raise ValueError()
        self.balance -= x
        print(f'출금 전 : {self.balance + x} \n'
              f'출금 후 : {self.balance} \n'
              f'출금이 완료되었습니다.')


    def transfer(self, to, x):
        self.withdraw(x)
        to.deposit(x)


if __name__ == '__main__':

    ac1 = Account(1002, '0000', 1000)
    ac2 = Account(1002, '1234', 2000)

    print(ac1)
    print(ac2)

    ac1.deposit(2000)
    print(ac1.balance)
    print()

    ac1.withdraw(1000)
    print(ac1.balance)
    print()

    ac1.transfer(ac2, 300)
    print()
    print(ac1)
    print(ac2)

