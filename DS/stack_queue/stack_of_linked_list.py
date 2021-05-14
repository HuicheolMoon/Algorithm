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
        self.length -= 1
        print(result)
        return result

    def peek(self) -> int:
        if self.length == 0:
            raise IndexError("빈 스택입니다.")
        else:
            result = self.tail.value
            print(result)
            return result

    def is_empty(self) -> bool:
        whether = True if self.length == 0 else False
        print(whether)
        return whether


if __name__ == "__main__":
    x1 = Stack()
    x1.push(4)
    x1.push(2)
    x1.push(3)
    x1.push(1)
    x1.pop()
    x1.peek()
    x1.pop()
    x1.push(5)
    x1.peek()
    x1.is_empty()
