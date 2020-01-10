

class Rectangle:
    '''
    직사각형 클래스
    '''

    def __init__(self, width = 0, height = 0):
        self.width = width
        self.height = height


    def info(self):
        print(f'Rectangle(x = {self.width}, h = {self.height})')


    def __eq__(self, other):
        return self.width == other.width and self.height == other.height


    def __str__(self):
        return f'<{__name__}.직사각형 객체 주소: >'


if __name__ == '__main__':
    rect1 = Rectangle(3, 2)
    print(type(rect1))
    print(id(rect1))
    rect1.info()
    print()

    rect2 = Rectangle(1)
    rect2.info()

    rect4 = Rectangle(2, 2)
    rect5 = Rectangle(2, 2)
    print()

    print(rect4 == rect5)
    # obj1 == obj2 비교하는 방법(== 연산자의 동작 방식)
    # == 연산자는 클래스의 __eq__ 함수를 호출
    # obj1.__eq__(obj2)

    # 개발자가 클래스를 정의할 때 __eq__ 메소드를 정의하지 않아도 모든 클래스는 __eq__ 메소드를 가지고 있음
    # 기본 __eq__ 메소드는 개체들의 주소값(id)를 비교함
    # 개발자가 __eq__ 메소드를 다른 방식으로 작성하면 == 연산자는 개발자의 의도대로 True/False를 리턴

    print(rect4 is rect5)
    print(rect5)