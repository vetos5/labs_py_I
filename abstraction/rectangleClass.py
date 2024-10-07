from shape import *


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
