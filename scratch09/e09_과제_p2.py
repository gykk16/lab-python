'''
emp.csv 파일을 읽어서, DataFrame을 생성
    - 급여(sal)가 2000 이상인 직원들의 모든 정보를 출력
    - 부서 번호(deptno)가 10인 직원들의 모든 정보를 출력
    - 급여가 전체 직원의 급여의 평균보다 많은 직원의 사번, 이름, 급여를 출력
    - 30번 부서에서 일하는, 직책이 SALESMAN인 직원들의 사번, 이름, 급여, 부서번호를 출력
    - 20, 30번 부서에 근무하는 직원들 중 급여가 2000을 초과하는 직원들의 사번, 이름,
    급여, 부서번호를 출력
    - 수당이 없는 직원들 중에서, 매니저가 있고, 직책이 'MANAGER' 또는 'CLERK'인
    직원들의 모든 정보를 검색

    - 사원 이름에 'E'가 포함된 직원들의 이름만 출력 (str.contains() 이용)

'''

import pandas as pd
import numpy as np


col_names = ['empno', 'ename', 'job', 'mgr', 'hiredate', 'sal', 'comm', 'deptno']
col_names = [i.upper() for i in col_names]

# emp.csv 파일을 읽어서, DataFrame을 생성
emp = pd.read_csv('emp.csv', encoding = 'UTF-8', names = col_names)
print(emp)
print(type(emp))
# emp.columns = ['empno', 'ename', 'job', 'mgr', 'hiredate', 'sal', 'comm', 'deptno']

print('\n================\n '
      '3) 급여(sal)가 2000 이상인 직원들의 모든 정보를 출력')

print(emp[emp['SAL'] >= 2000])

print('\n================\n '
      '4) 부서 번호(deptno)가 10인 직원들의 모든 정보를 출력')

print(emp[emp['DEPTNO'] == 10])

print('\n================\n '
      '5) 급여가 전체 직원의 급여의 평균보다 많은 직원의 사번, 이름, 급여를 출력')

sal_mean = emp['SAL'].mean()
print('SAL mean :', sal_mean)

subset = emp[emp['SAL'] > emp['SAL'].mean()]
print(subset[['EMPNO', 'ENAME', 'SAL']])

print('\n================\n '
      '6) 30번 부서에서 일하는, 직책이 SALESMAN인 직원들의 사번, 이름, 급여, 부서번호를 출력')

dept_30 = emp[emp['DEPTNO'] == 30]
dept_30_salesman = dept_30[dept_30['JOB'] == 'SALESMAN']
print(dept_30_salesman[['EMPNO', 'ENAME', 'JOB', 'SAL', 'DEPTNO']])
##
print()
c1 = emp['DEPTNO'] == 30
c2 = emp['JOB'] == 'SALESMAN'
subset = emp[c1 & c2]
print(subset[['EMPNO', 'ENAME', 'JOB', 'SAL', 'DEPTNO']])

print('\n================\n '
      '7) 20, 30번 부서에 근무하는 직원들 중 급여가 2000을 초과하는 직원들의 사번, 이름, 급여, 부서번호를 출력')

# c1 = emp['DEPTNO'] == 20
# c2 = emp['DEPTNO'] == 30
c1 = emp['DEPTNO'].isin([20, 30])
c3 = emp['SAL'] > 2000

# subset = emp[(c1 | c2) & c3]
subset = emp[c1 & c3]
print(subset[['EMPNO', 'ENAME', 'SAL', 'DEPTNO']])

print('\n================\n '
      '8) 수당이 없는 직원들 중에서, 매니저가 있고, 직책이 MANAGER 또는 CLERK인 직원들의 모든 정보를 검색')
# -
c1 = emp['COMM'].isnull()
# c2 = ~emp['MGR'].isnull()
c2 = emp['MGR'].notnull()
c3 = emp['JOB'].isin(['MANAGER', 'CLERK'])
subset = emp[c1 & c2 & c3]
print(subset)

print('\n================\n '
      '9) 사원 이름에 "E"가 포함된 직원들의 이름만 출력 (str.contains() 이용)')
# -
# subset = emp[emp['ENAME'].str.contains('E')]
subset = emp[emp['ENAME'].str.contains('E')]
# print(subset)
print(subset['ENAME'])  # Series
print(subset[['ENAME']])    # DataFrame


# DataFrame.to_csv(file_path)
# to_csv() 함수는 행 이름(row index)를 파일에 쓴다
# row index 를 쓰지 않으려면 index = False 파라미터 추가
emp.to_csv('emp2.csv', index = False)



