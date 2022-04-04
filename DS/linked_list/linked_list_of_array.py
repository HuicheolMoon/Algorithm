class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self) -> None
        self.head = None
        self.length = 0

    def append_node(self, node: Node) -> None:
        if self.length == 0:
            self.head = node
        else:
            tail = self.head
            while tail.next:
                tail = tail.next
            tail.next = node
        self.length += 1

    def delete_node(self, idx: int) -> None:
        if idx >= self.length:
            raise IndexError("인덱스가 리스트 범위 밖입니다.")
        elif idx == 0:
            self.head = self.head.next
        else:
            count = 1
            front = self.head
            ghost = self.head.next
            while count < idx:
                front = ghost
                ghost = front.next
                count += 1
            front.next = ghost.next
        self.length -= 1

    def insert_node(self, node: Node, idx: int) -> None:
        if idx > self.length:
            raise IndexError("인덱스가 리스트 범위 밖입니다.")
        elif idx == 0:
            node.next = self.head
            self.head = node
        else:
            count = 1
            front = self.head
            while count < idx:
                front = front.next
                count += 1
            node.next = front.next
            front.next = node
        self.length += 1

    def get_index(self, value: int) -> int:
        if self.length > 0:
            tail = self.head
            idx = 0
            while tail:
                if tail.value == value:
                    return idx
                tail = tail.next
                idx += 1
        raise IndexError("해당하는 값이 없습니다.")


x1 = LinkedList()
x1.append_node(Node(4))
x1.append_node(Node(2))
x1.append_node(Node(3))
x1.append_node(Node(1))
x1.insert_node(Node(5), 2)
print(x1.get_index(2))
print(x1.get_index(3))
x1.insert_node(Node(6), 2)
x1.delete_node(3)
print(x1.get_index(2))
