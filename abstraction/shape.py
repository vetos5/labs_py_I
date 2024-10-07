from color import *
from errorMSG import *


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




