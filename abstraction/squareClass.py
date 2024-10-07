from shape import *
from rectangleClass import Rectangle


class Square(Rectangle):
    def __init__(self, side: float, color: Color):
        try:
            Rectangle.__init__(self, side, side, color)
        except TypeError:
            print(TypeError_MSG)

    def name(self):
        return "Square"
