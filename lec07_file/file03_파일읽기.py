
# open
f = open('test.txt', mode = 'r', encoding = 'utf-8')

# read: read(), readline()
# content = f.read()
content = f.read(3)
print(content)

content = f.read(3)
print(content)

# close
f.close()


f = open('test2.txt', 'r', encoding = 'utf-8')
line = f.readline()
line = line.strip()
print(f'line: {line}, length: {len(line)}')
line = f.readline().strip()
print(f'line: {line}, length: {len(line)}')
line = f.readline().strip()
print(f'line: {line}, length: {len(line)}')


f.close()

# .strip 문자열 중간에 있는 공백을 제외한 공백 제거
print('              hello   python   \n       '.strip())


# 무한 루프와 readline()을 사용해서 문서 끝까지 읽기

f = open('test.txt', mode = 'r', encoding = 'utf-8')
while True:
    line = f.readline()
    if line == '': # 파일 끝(EOF: End of File)에 도달
        break   # 무한 루프 종료
    print(line.strip())

f.close()

print()

f = open('test.txt', mode = 'r', encoding = 'utf-8')
line = f.readline()
while line:
    # line이 빈 문자열('')이면 False, 그렇지 않으면 True
    print(line.strip())
    line = f.readline()

f.close()

print()

with open('test2.txt', mode = 'r', encoding = 'utf-8') as f:
    line = f.readline()
    while line:
        print(line.strip())
        line = f.readline()


