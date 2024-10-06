INDEX_ERROR_MSG = "Index out of range"


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self, values=None):
        self.array = list(values) if values is not None else []
        self.head = None
        self.tail = None
        self.size = 0

        for value in self.array:
            self.add(value)

    def add(self, element):
        new_node = Node(element)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def remove(self, index):
        if index < 0 or index >= self.size:
            print(INDEX_ERROR_MSG)
            exit(1)

        current = self.head
        for _ in range(index):
            current = current.next

        if current.prev:
            current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev

        if current == self.head:
            self.head = current.next
        if current == self.tail:
            self.tail = current.prev

        self.size -= 1

    def insert(self, index, element):
        if index < 0 or index > self.size:
            print(INDEX_ERROR_MSG)
            exit(1)

        new_node = Node(element)

        if index == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            if self.size == 0:
                self.tail = new_node
        elif index == self.size:
            self.add(element)
            return
        else:
            current = self.head
            for _ in range(index):
                current = current.next
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

    def __len__(self):
        return self.size

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def get(self, index):
        if index < 0 or index >= self.size:
            print(INDEX_ERROR_MSG)
            return None

        current = self.head
        for _ in range(index):
            current = current.next

        return current.value if current else None


if __name__ == '__main__':
    array = [1, 2, 3]
    llist = LinkedList(array)
    for value in llist:
        print(value, end=' ')
    print()

    llist.remove(0)
    for value in llist:
        print(value, end=' ')
    print('\n')
    print(len(llist))

    print(llist.get(7))

    llist.clear()

    for value in llist:
        print(value, end=' ')
    print()

