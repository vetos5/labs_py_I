from color import *

NotImplemented_MSG = "Method Not Implemented"


class Shape(ABC):
    def __init__(self, color: Color):
        self.color = color

    def area(self):
        print(NotImplemented_MSG)
        quit(1)

    def perimeter(self):
        print(NotImplemented_MSG)
        quit(1)

    def name(self):
        print(NotImplemented_MSG)
        quit(1)

    def fill(self):
        return self.color.fill()


class Circle(Shape):
    def __init__(self, radius: float, color: Color):
        Shape.__init__(self, color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

    def name(self):
        return "Circle"


class Rectangle(Shape):
    def __init__(self, width: float, height: float, color: Color):
        Shape.__init__(self, color)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def name(self):
        return "Rectangle"


class Square(Rectangle):
    def __init__(self, side: float, color: Color):
        Rectangle.__init__(self, side, side, color)

    def name(self):
        return "Square"
