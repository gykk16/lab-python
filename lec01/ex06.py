'''
문자열 타입
'''

s = '''    def my_function(x: int) -> int:
        return x + 1
'''
print(s)


s = '''\
    def my_function(x: int) -> int:
        return x + 1
'''
print(s)


s = '''
    def my_function(x: int) -> int:
        return x + 1
'''
print(s)


s = '\thello\n\tpython'
print(s)

#   문자열 인덱스, 자르기(slicing)
s = 'hello'
print(s[0])
print(s[1])
print(s[4])
# print(s[5])   # IndexError 발생
# 인덱스 시작은 0부터
print(s[0:2])
# x:y - from x(포함, include) to y(미포함, exclude)
print(s[1:5])
print(s[1: ]) # 배열의 끝까지 출력
print(s[ :3]) # 처음(0)부터 3번 까지 (3번 미포함)