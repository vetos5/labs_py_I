INDEX_ERROR_MSG = "Index out of range"


class Node:
    def __init__(self, value):
        if not isinstance(value, (int, float, str)):
            raise TypeError("Node value must be an int, float, or str.")
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        self.size = 0

        if values is not None:
            for value in values:
                self.append(value)

    def append(self, element):
        new_node = Node(element)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def find(self, data):
        current = self.head
        while current:
            if current.value == data:
                return current
            current = current.next
        raise ValueError("Data not found in the list.")

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError(INDEX_ERROR_MSG)
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def remove(self, data):
        target = self.find(data)

        if target.prev:
            target.prev.next = target.next
        else:
            self.head = target.next

        if target.next:
            target.next.prev = target.prev
        else:
            self.tail = target.prev

        self.size -= 1

    def insert(self, index, element):
        if index < 0 or index > self.size:
            raise IndexError(INDEX_ERROR_MSG)

        new_node = Node(element)

        if index == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            self.tail = new_node
        elif index == self.size:
            self.append(element)
            return
        else:
            current = self.get(index)
            new_node.prev = current.prev
            new_node.next = current
            if current.prev:
                current.prev.next = new_node
            current.prev = new_node

        self.size += 1

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def count(self, value):
        count = 0
        current = self.head
        while current:
            if current.value == value:
                count += 1
            current = current.next
        return count

    def reverse(self):
        current = self.head
        self.tail = current
        prev_node = None
        while current:
            next_node = current.next
            current.next = prev_node
            current.prev = next_node
            prev_node = current
            current = next_node
        self.head = prev_node

    def roll(self, steps):
        if self.size == 0 or steps % self.size == 0:
            return
        steps = steps % self.size
        if steps < 0:
            steps = self.size + steps
        for _ in range(steps):
            self.tail.next = self.head
            self.head.prev = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            self.head = self.head.prev
            self.head.prev = None

    def sort(self):
        if self.size < 2:
            return
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next:
                if current.value > current.next.value:
                    current.value, current.next.value = current.next.value, current.value
                    swapped = True
                current = current.next

    def __len__(self):
        return self.size

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(repr(current.value))
            current = current.next
        return "[" + ", ".join(values) + "]"

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __add__(self, other):
        if not isinstance(other, LinkedList):
            raise TypeError("Can only concatenate LinkedList with LinkedList")
        result = LinkedList()
        for value in self:
            result.append(value)
        for value in other:
            result.append(value)
        return result

    def __getitem__(self, index):
        if index < 0:
            index += self.size
        if index < 0 or index >= self.size:
            raise IndexError(INDEX_ERROR_MSG)
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value

    def __setitem__(self, index, value):
        if index < 0:
            index += self.size
        if index < 0 or index >= self.size:
            raise IndexError(INDEX_ERROR_MSG)
        current = self.head
        for _ in range(index):
            current = current.next
        current.value = value
