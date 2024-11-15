from base_backpack import Backpack
from jetpack import Jetpack
from complex_number import ComplexNumber


def test_backpack():
    pack = Backpack("Alice", "red", max_size=4)
    pack.put("book")
    pack.put("pencil")
    pack.put("notebook")
    pack.put("eraser")
    pack.put("extra")
    print(pack)
    pack.dump()
    print("After dump:", pack.contents)


def test_jetpack():
    jet = Jetpack("Charlie", "green")
    jet.fly(5)
    jet.fly(6)
    print("Remaining fuel:", jet.fuel)
    jet.dump()
    print("After dump:", jet.contents, jet.fuel)


def test_complex_number():
    c1 = ComplexNumber(3, 4)
    c2 = ComplexNumber(1, -2)
    print("c1:", c1)
    print("c2:", c2)
    print("c1 + c2:", c1 + c2)
    print("c1 - c2:", c1 - c2)
    print("c1 * c2:", c1 * c2)
    print("c1 / c2:", c1 / c2)
    print("|c1|:", abs(c1))
    print("c1 conjugate:", c1.conjugate())
    print("Equality test:", c1 == c2)


if __name__ == "__main__":
    test_backpack()
    test_jetpack()
    test_complex_number()
