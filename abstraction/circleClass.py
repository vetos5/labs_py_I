from shape import *
from math import pi


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
            return pi * self.radius ** 2
        except AttributeError:
            print(NoRadius_MSG)
            exit(1)
        except TypeError:
            print(TypeError_MSG)
            exit(1)

    def perimeter(self):
        try:
            return 2 * pi * self.radius
        except AttributeError:
            print(NoRadius_MSG)
            exit(1)
        except TypeError:
            print(TypeError_MSG)
            exit(1)

    def name(self):
        return "Circle"
