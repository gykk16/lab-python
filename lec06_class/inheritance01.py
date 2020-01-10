'''
상속(inheritance)

    부모 class로부터 데이터(field)와 기능(method)를 물려받아서 자식 클래스에서 사용할 수 있도록 하는 개념
    - parent(부모), super(상위), base(기본) class
    - child(자식), sub(하위), derived(유도) class

'''


class Shape:
    def __init__(self, x = 0, y = 0):
        print('\n Shape.__init__ 호출 \n')
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Shape(x = {self.x}, y = {self.y})'

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def area(self):
        '''
        Shape 객체는 넓비를 계산 할 수 없고,
        Shape 의 sub 타입들인 Rectangle, Circle 객체가 각자의 방식으로 넓이를 계산해야 됨

        :return:
        '''

        raise NotImplementedError('area 메소드를 반드시 override')

    def draw(self):
        '''
        넓이를 계산하는 area 메소드를 사용해서 도형 내부를 그려주는 메소드

        :return:
        '''

        print(f'Drawing area {self.area()} ...')

# 상속:
# class Child(Parent):
#   body
class Rectangle(Shape):
    def __init__(self, w = 0, h = 0, x = 0, y = 0):
        print('\n Rectangle.__init__ 호출 \n')
        super().__init__(x, y)  # 부모 클래스의 __init__ 호출 (부모 클래스의 주소를 가지고 있음)
        # Shape.__init__(self, x, y)    # self 생략 불가 (클래스의 이름은 주소까지 불러오지 않는다)
        self.w = w
        self.h = h

    # override: 부모 클래스로부터 상속 박은 메소드를 자식 클래스에서 재정의 하는 것.
    def __repr__(self):
        return f'사각형 (w = {self.w}, h = {self.h}, x = {self.x}, y = {self.y})'

    def area(self):
        return self.w * self.h


class Circle(Shape):
    def __init__(self, r = 0, x = 0, y = 0):
        print('\n Circle.__init__ 호출 \n')
        super().__init__(x, y)
        self.r = r

    def __repr__(self):
        return f'원 (반지름 = {r}, x = {self.x}, y = {self.y})'

    def area(self):
        return 3.14159 * self.r ** 2


if __name__ == '__main__':
    shape1 = Shape()
    print(shape1)
    shape1.move(1, 2)
    print(shape1)

    rect1 = Rectangle(3, 4, 0, 0)
    print(type(rect1))
    print(rect1)
    rect1.move(-1, -2)
    print(rect1)

    circle1 = Circle(r = 10, x = 0, y = 0)
    print(type(circle1))
    print(rect1)

    rect1.draw()
    circle1.draw()