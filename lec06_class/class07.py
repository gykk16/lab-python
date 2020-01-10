import math


class Circle:
    '''
    field: 반지름(radius)
    method:
        __init__()
        area(): 원의 넓이를 return
        perimeter(): 원의 둘레 길이를 return
        __str__(): circle(r = 123) 형식
        __eq__(): 반지름 같으면 equal(True)

    '''

    def __init__(self, radius):
        self.radius = radius
        if self.radius < 0:
            raise ValueError('반지름이 0 보다  작습니다.')

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f'Circle(r = {self.radius})'

    def __repr__(self): # representation
        return f'원({self.radius})'

    def __eq__(self, other):    # equal
        return self.radius == other.radius

    def __ne__(self, other):    # not equal
        return self.radius != other.radius

    def __gt__(self, other):    # greater than
        print('__gt__ 호출')
        return self.radius > other.radius

    def __ge__(self, other):    # greater than or equal
        return self.radius >= other.radius
        print('__ge__ 호출')

    # __lt__ : less than (<)
    # __le__ : less than or equal to (<=)

if __name__ == '__main__':
    c1 = Circle(6)
    area1 = c1.area()
    perimeter1 = c1.perimeter()
    print(area1)
    print(perimeter1)
    print(c1)
    print()

    c2 = Circle(6)
    print(c1 == c2)
    print(c1 != c2)
    print(c1 > c2)
    print(c1 < c2)

    circles = [
        Circle(10),
        Circle(7),
        Circle(100),
        Circle(50),
        Circle(0),
        Circle(50)
    ]
    print(circles)

    print(sorted(circles))
    print(sorted(circles, reverse = True))