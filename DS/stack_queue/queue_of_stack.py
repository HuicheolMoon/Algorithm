class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next = None


class Stack:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def push(self, value: int) -> None:
        node = Node(value)
        if self.length == 0:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.length += 1

    def pop(self) -> int:
        if self.length == 0:
            raise IndexError("빈 스택입니다.")
        elif self.length == 1:
            result = self.tail.value
            self.head = None
            self.tail = None
        else:
            new_tail = self.head
            for _ in range(self.length - 2):
                new_tail = new_tail.next
            result = self.tail.value
            new_tail.next = None
            self.tail = new_tail
        self.length -= 1
        return result

    def peek(self) -> int:
        if self.length == 0:
            raise IndexError("빈 스택입니다.")
        else:
            result = self.tail.value
            return result

    def is_empty(self) -> bool:
        whether = True if self.length == 0 else False
        return whether


class Queue:
    def __init__(self) -> None:
        self.s1 = Stack()
        self.s2 = Stack()
        self.length = 0

    def enqueue(self, value: int) -> None:
        self.s1.push(value)
        self.length += 1

    def dequeue(self) -> int:
        if self.s1.is_empty() and self.s2.is_empty():
            raise IndexError("빈 큐입니다.")
        elif self.s2.is_empty():
            for _ in range(self.s1.length):
                self.s2.push(self.s1.pop())
        self.length -= 1
        return self.s2.pop()

    def peek(self) -> int:
        if self.s1.is_empty() and self.s2.is_empty():
            raise IndexError("빈 큐입니다.")
        elif self.s2.is_empty():
            for _ in range(self.s1.length):
                self.s2.push(self.s1.pop())
        return self.s2.peek()

    def is_empty(self) -> bool:
        return self.s1.is_empty() and self.s2.is_empty()


if __name__ == "__main__":
    x1 = Queue()
    x1.enqueue(4)
    x1.enqueue(2)
    x1.enqueue(3)
    x1.enqueue(1)
    print(x1.dequeue())
    print(x1.peek())
    print(x1.dequeue())
    x1.enqueue(5)
    print(x1.peek())
    print(x1.is_empty())
