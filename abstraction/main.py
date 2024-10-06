from shape import *


def main():
    circle = Circle(5, Yellow())
    rectangle = Rectangle(4, 6, Fuchsia())
    square = Square(3, Cyan())

    shapes = [circle, rectangle, square]

    for shape in shapes:
        print(f"A {shape.fill()} {shape.name()} with area: {shape.area()} and perimeter: {shape.perimeter()}")


if __name__ == '__main__':
    main()
