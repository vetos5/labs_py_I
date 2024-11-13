from linkedList import *


class Deque(LinkedList):

    def pop(self):
        if not self.tail:
            raise ValueError("Deque is empty.")
        value = self.tail.value
        if self.tail.prev:
            self.tail.prev.next = None
            self.tail = self.tail.prev
        else:
            self.head = self.tail = None
        self.size -= 1
        return value

    def popleft(self):
        if not self.head:
            raise ValueError("Deque is empty.")
        value = self.head.value
        if self.head.next:
            self.head.next.prev = None
            self.head = self.head.next
        else:
            self.head = self.tail = None
        self.size -= 1
        return value

    def appendleft(self, element):
        new_node = Node(element)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def remove(*args, **kwargs):
        raise NotImplementedError("Use pop() or popleft() for removal.")

    def insert(*args, **kwargs):
        raise NotImplementedError("Middle insertion is disabled for Deque.")
