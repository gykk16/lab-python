'''
반복문 연습
'''

# 1 + 2 + 3 + ... + 100 = ?
x = 0
for i in range(1, 101):
    x += i
print(x)
print()

x, n = 0, 1
while n <= 100:
    x += n
    n += 1
print(x)
print()

numbers = [x for x in range(1, 101)]
print(sum(numbers))
print()

# 1 + 2 + 3 + ... + x <= 100
x = 0
for i in range(1, 101):
    if x + i <= 100:
        x += i
print(x)

x, n = 0, 1
while x <= 100:
    x += n
    n += 1
    if x + n >= 100:
        break
print(n)
