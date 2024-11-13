from utils import *

if __name__ == '__main__':
    values = [1, 2, 3]
    llist = LinkedList(values)
    print(llist)

    llist.remove(1)
    print(llist)

    llist.insert(1, 5)
    print(llist)

    deque = Deque(values)
    deque.appendleft(0)
    print(deque)

    deque.pop()
    print(deque)

    deque.popleft()
    print(deque)

    reverse_file_lines("input.txt", "output.txt")
