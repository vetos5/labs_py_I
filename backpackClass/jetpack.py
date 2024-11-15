from base_backpack import Backpack


class Jetpack(Backpack):
    """A Jetpack class inheriting from Backpack."""

    def __init__(self, name, color, max_size=2, fuel=10):
        super().__init__(name, color, max_size)
        self.fuel = fuel

    def fly(self, amount):
        if amount > self.fuel:
            print("Not enough fuel!")
        else:
            self.fuel -= amount

    def dump(self):
        super().dump()
        self.fuel = 0
