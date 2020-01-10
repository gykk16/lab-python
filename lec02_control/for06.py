'''
dictionary comprehension

dict:
{k : v}
'''

numbers = [1, 2, 3, 4, 5]
names = ['a', 'b', 'c', 'd', 'e']

students = {}  # empty dict
for i in range(len(numbers)):
    students[numbers[i]] = names[i]
print(students)

# dictionary comprehension
students2 = {numbers[i]: names[i] for i in range(len(numbers))}
print(students2)

# zip
num_name = zip(numbers, names)
print(num_name)
for i in num_name:
    print(i)
print()

for i in zip(numbers, names):
    print(i)
print()

#
students3 = {}
for key, value in zip(numbers, names):
    students3[key] = value
print(students3)

#
students4 = {k: v for k, v in zip(numbers, names)}
print(students4)

# key 가 홀수인 dict 출력
students5 = {k: v for k, v in zip(numbers, names) if k % 2}
print(students5)