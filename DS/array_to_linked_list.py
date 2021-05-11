from random import randint

array = [randint(1, 100) for _ in range(10)]


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def append_node(self, node):
        if not self.head:
            self.head = node
        else:
            tail = self.head
            while tail.next:
                tail = tail.next
            tail.next = node
        self.length += 1

    def get_index(self, value):
        if not self.head:
            raise IndexError("해당하는 값이 없습니다.")
        tail = self.head
        idx = 0
        while tail:
            if tail.value == value:
                print(idx)
                return idx
            tail = tail.next
            idx += 1
        raise IndexError("해당하는 값이 없습니다.")

    def insert_node(self, node, idx):
        if idx == 0:
            node.next = self.head
            self.head = node
        elif idx > self.length:
            raise IndexError("인덱스가 리스트 범위 밖입니다.")
        else:
            count = 1
            front = self.head
            while count < idx:
                front = front.next
                count += 1
            node.next = front.next
            front.next = node

    def delete_node(self, idx):
        if idx == 0:
            front = self.head
            self.head = front.next
        elif idx >= self.length:
            raise IndexError("인덱스가 리스트 범위 밖입니다.")
        else:
            count = 1
            front = self.head
            end = front.next
            while count < idx:
                front = end
                end = front.next
                count += 1
            front.next = end.next

    def clear_list(self):
        self.head = None

    def print_list(self):
        elements = []
        node = self.head
        while node:
            elements.append(node.value)
            node = node.next
        concate_elem = ", ".join(list(map(str, elements)))
        result = f"[{concate_elem}]"
        print(result)


if __name__ == "__main__":
    lnkl = LinkedList()
    lnkl.append_node(Node(4))
    lnkl.append_node(Node(2))
    lnkl.append_node(Node(3))
    lnkl.append_node(Node(1))
    lnkl.insert_node(Node(5), 2)
    lnkl.print_list()
    lnkl.get_index(2)
    lnkl.get_index(3)
    lnkl.insert_node(Node(6), 2)
    lnkl.print_list()
