'''
Python 반복문 - for 구문

for 변수 in Iterable:
    반복할 문장들

Iterable(반복 가능한 타입): 리스트, 튜플, 집합, 딕셔너리, 문자열, ...
'''


# range(to): 0부터 (to - 1) 까지 범위의 숫자들
# range(from, to): from 부터 (to - 1) 까지 범위의 숫자들
# range(from, to, step): from 부터 (to - 1) 까지 step 만큼씩 증가

for i in range(5):
    print(i, end = ' ')

print()

for i in range(1, 5):   # (1, 2, 3, 4)
    print(i, end = ' ')
print()

for i in range(1, 5, 2):    # (1, 3)
    print(i, end = ' ')
print()

for s in "Hello, Python":
    print(s, end = ' ')
print()

langs = ['PL/SQL', 'R', 'Python', 'Java']
for lang in langs:
    print(lang, end = ' ')
print()

for i in range(len(langs)):
    print(i, langs[i])
print()

alphabets = {1: 'a', 2: 'b', 3: 'c'}
print(alphabets.keys())

for key in alphabets.keys():
    print(key, alphabets[key])
print()

# in dict는 딕셔너리의 key들을 반복한다
for key in alphabets:
    print(key)
print()

for item in alphabets.items():
    print(item)
print()

# key, value = (1, 'a')
for key, value in alphabets.items():
    print(key, value)