'''
재귀 합수(recursive function)
'''

# factorial
# 0! = 1
# n! = 1 * 2 * 3 * ... * (n - 1) * n

def factorial1(n: int) -> int:
    x = 1
    for i in range(1, n + 1):
        x *= i

    return x


for i in range(6):
    print(f'{i}! = {factorial1(i)}')
print()


# 0! = 1
# n! = 1 * 2 * 3 * ... * (n - 1) * n = (n - 1)! * n
def factorial2(n: int) -> int:
    if n == 0:
        return 1
    elif n > 0:
        return factorial2(n - 1) * n


for i in range(6):
    print(f'{i}! = {factorial2(i)}')
print()


def sum_to_n(n: int) -> int:
    if n == 1:
        return 1
    elif n > 0:
        return sum_to_n(n - 1) + n


for i in range(6):
    print(f'sum to {i} = {sum_to_n(i)}')
print()
