'''
클래스 작성, 객체 생성, 메소드 사용 연습
'''

class Employee:
    '''
    사원 정보와 급여 인상 메소드를 가지고 있는 클래스

    field: empno, ename, salary, deptno
    method: raise_salary(self, pct)
    '''

    def __init__(self, empno, ename, salary, deptno):
        self.empno = empno
        self.ename = ename
        self.salary = salary
        self.deptno = deptno


    def raise_salary(self, pct):
        '''
        인상된 급여를 return

        :param pct: 급여 인상율(0.1 = 10%, 0.5 = 50%, ...)
        :return:
        '''
        self.salary *= (1 + pct)
        return self.salary

    def __repr__(self):
        return f'(사번: {self.empno}, 이름: {self.ename}, 급여: {self.salary}, 부서번호: {self.deptno})'


scott = Employee(7777, 'Scott', 1000, 10)
print(scott.__repr__())
scott.raise_salary(.1)
print(scott.__repr__())

print()

smith = Employee(9999, 'Smith', 10000, 10)
print(smith.__repr__())
smith.raise_salary(-.1)
print(smith.__repr__())

print()

adams = Employee(8888, 'Adams', 500, 30)

employees = [scott, smith, adams]
print(employees)


print(sorted(employees, key = lambda x: x.empno))
print(sorted(employees, key = lambda x: x.salary))