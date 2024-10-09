# Q2. what is double linked list ?


class Node:
    def __init__(self, value):
        self.data = value
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        last = self.head

        while last.next:
            last = last.next
        last.next = new_node

    def print(self):
        info = self.head
        while info:
            print(f"{info.data} ->", end=" ")
            info = info.next
        print("None")


obj = LinkedList()
obj.insert(10)
obj.insert(20)
obj.insert(30)
obj.print()