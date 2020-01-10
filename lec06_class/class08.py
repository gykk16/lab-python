class Account:
    '''
    은행 계좌 클래스

    field(데이터): 계좌번호(acc_no), 잔액(balance),
    method(기능): 입금(deposit), 출금(withdraw), 이체(transfer)

    '''

    def __init__(self, acc_no, pw, balance ):
        self.acc_no = acc_no
        self.balance = balance
        self.pw = pw

    def deposit(self):
        while True:
            try:
                print()
                input_acc_no = int(input('>>> 계좌번호를 입력하세요 : '))
                if type(input_acc_no) == int:
                    break
            except ValueError:
                print('계좌가 잘못되었습니다.')

        input_pw = str(input('>>> 비밀번호 4자리를 입력하세요 : '))
        input_x = int(input('>>> 입금할 금액을 입력하세요 : '))

        if self.acc_no == input_acc_no and self.pw == input_pw:
            self.balance += input_x
            print(f'입금 전 : {self.balance - input_x} , 입금 후 : {self.balance} \n'
                  f'입금이 완료되었습니다.')
        else:
            print('계좌번호 또는 비밀번호가 잘못되었습니다.')


    def withdraw(self):
        input_acc_no = int(input('>>> 계좌번호를 입력하세요 : '))
        input_pw = str(input('>>> 비밀번호 4자리를 입력하세요 : '))
        input_x = int(input('>>> 출금할 금액을 입력하세요 : '))

        if self.acc_no == input_acc_no and self.pw == input_pw:
            if self.balance < input_x:
                print('잔액이 부족합니다.')
            else:
                self.balance -= input_x
                print(f'출금 전 : {self.balance + input_x} , 출금 후 : {self.balance}\n'
                  f'출금이 완료되었습니다.')
        else:
            print('계좌번호 또는 비밀번호가 잘못되었습니다.')

    # def transfer(self):
    #     input_acc_no = int(input('>>> 출금 계좌번호를 입력하세요 : '))
    #     input_pw = str(input('>>> 비밀번호 4자리를 입력하세요 : '))
    #     input_acc_2 = input('>>> 이체 계좌번호를 입력하세요 : ')
    #     input_x = int(input('>>> 이체 할 금액을 입력하세요 : '))
    #
    #     if self.acc_no == input_acc_no and self.pw == input_pw:
    #         if self.balance < input_x:
    #             print('잔액이 부족합니다.')
    #         else:
    #             self.balance -= input_x
    #             input_acc_2.balance += input_x
    #         print(f'이체 전 : {self.balance + input_x} , 이체 후 : {self.balance} \n'
    #               f'이체 완료.')
    #      else:
    #         print('계좌번호 또는 비밀번호가 잘못되었습니다.')

    def transfer2(self, other):
        input_acc_no = int(input('>>> 출금 계좌번호를 입력하세요 : '))
        input_pw = str(input('>>> 비밀번호 4자리를 입력하세요 : '))
        input_x = int(input('>>> 이체 할 금액을 입력하세요 : '))

        if self.acc_no == input_acc_no and self.pw == input_pw:
            if self.balance < input_x:
                print('잔액이 부족합니다.')
            else:
                self.balance -= input_x
                other.balance += input_x
            print(f'이체 전 : {self.balance + input_x} , 이체 후 : {self.balance} \n'
                  f'이체 완료.')
        else:
            print('계좌번호 또는 비밀번호가 잘못되었습니다.')

ac1 = Account(1001, '0000', 1000)
ac2 = Account(1002, '1234', 2000)

print(ac1.balance)
print(ac2.balance)

ac1.deposit()
print(ac1.balance)
print()
#
# ac1.withdraw()
# print(ac1.balance)
# print()

# ac1.transfer2(ac2)
# print(f'ac1 balcance: {ac1.balance})
# print(f'ac2 balcance: {ac2.balance})
# print()