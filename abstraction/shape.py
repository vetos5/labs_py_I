from color import *

NotImplemented_MSG = "Method Not Implemented"
NoRadius_MSG = "'self' does not have a radius attribute."
NoWidthHeight_MSG = "'self' does not have a width and height attribute."
TypeError_MSG = "Type Error"
ValueError_MSG = "Value Error"


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
        try:
            Shape.__init__(self, color)
            self.radius = radius
            if self.radius <= 0:
                print(ValueError_MSG)
                quit(1)
        except TypeError:
            print(TypeError_MSG)
            quit(1)

    def area(self):
        try:
            return 3.14 * self.radius ** 2
        except AttributeError:
            print(NoRadius_MSG)
            exit(1)
        except TypeError:
            print(TypeError_MSG)
            exit(1)

    def perimeter(self):
        try:
            return 2 * 3.14 * self.radius
        except AttributeError:
            print(NoRadius_MSG)
            exit(1)
        except TypeError:
            print(TypeError_MSG)
            exit(1)

    def name(self):
        return "Circle"


class Rectangle(Shape):
    def __init__(self, width: float, height: float, color: Color):
        try:
            Shape.__init__(self, color)
            self.width = width
            self.height = height
            if self.width <= 0 or self.height <= 0:
                print(ValueError_MSG)
                exit(1)
        except TypeError:
            print(TypeError_MSG)
            exit(1)

    def area(self):
        try:
            return self.width * self.height
        except AttributeError:
            print(NoWidthHeight_MSG)
            exit(1)

    def perimeter(self):
        try:
            return 2 * (self.width + self.height)
        except AttributeError:
            print(NoWidthHeight_MSG)
            exit(1)

    def name(self):
        return "Rectangle"


class Square(Rectangle):
    def __init__(self, side: float, color: Color):
        try:
            Rectangle.__init__(self, side, side, color)
        except TypeError:
            print(TypeError_MSG)

    def name(self):
        return "Square"
