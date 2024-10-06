from abc import ABC, abstractmethod


class Color(ABC):
    @abstractmethod
    def fill(self):
        pass


class Fuchsia(Color):
    def fill(self):
        return "Fuchsia"


class Cyan(Color):
    def fill(self):
        return "Cyan"


class Yellow(Color):
    def fill(self):
        return "Yellow"
