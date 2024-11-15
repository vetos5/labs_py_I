class Backpack:
    """A Backpack object class. Holds items and has attributes for the owner, color, and maximum size."""

    def __init__(self, name, color, max_size=5):
        self.name = name
        self.color = color
        self.max_size = max_size
        self.contents = []

    def put(self, item):
        if len(self.contents) >= self.max_size:
            print("No Room!")
        else:
            self.contents.append(item)

    def take(self, item):
        if item in self.contents:
            self.contents.remove(item)

    def dump(self):
        self.contents = []

    def __str__(self):
        return (
            f"Owner: {self.name}\n"
            f"Color: {self.color}\n"
            f"Size: {len(self.contents)}\n"
            f"Max Size: {self.max_size}\n"
            f"Contents: {self.contents}"
        )

    def __eq__(self, other):
        return (
                self.name == other.name and
                self.color == other.color and
                len(self.contents) == len(other.contents)
        )
