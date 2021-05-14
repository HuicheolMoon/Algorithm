class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next = None


class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def enqueue(self, value: int) -> None:
        node = Node(value)
        if self.length == 0:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.length += 1

    def dequeue(self) -> int:
        if self.length == 0:
            raise IndexError("빈 큐입니다.")
        elif self.length == 1:
            result = self.head.value
            self.head = None
            self.tail = None
        else:
            result = self.head.value
            self.head = self.head.next
        self.length -= 1
        return result

    def peek(self) -> int:
        if self.length == 0:
            raise IndexError("빈 큐입니다.")
        else:
            result = self.head.value
            return result

    def is_empty(self) -> bool:
        whether = True if self.length == 0 else False
        return whether


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
