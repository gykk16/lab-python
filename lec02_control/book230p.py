
x = 'T'
# n = 'T'
# for i in range(7):
#     print(x)
#     x += n


for i in range(8):
    for j in range(i):
        print('T', end='')
    print()
print()

for i in range(8):
    print('T' * i, end='')
    print()
print()


x = 8
for i in range(8):
    for j in reversed(range(x)):
        print('*', end='')
        if j == 0:
            for k in range(i):
                print('T', end='')
            print()
    x -= 1
print()

# for i in reversed(range(7)):
#     for j in range(i):
#         print('T', end='')
#     print()
# print()