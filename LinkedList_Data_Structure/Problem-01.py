# Q1. what is single linked list ?

# steps :
# 1. node = (data + Reference to the next node)

# Data->next

# MAke Node class
# class Node:
#     def __init__(self,value):
#         self.data=value
#         self.next=None


# class LinkedList:
#     def __init__(self):
#         self.head=None

#     def insert(self,data):
#         new_node=Node()

# Q1. what is single linked list ?

# steps :
# 1. node = (data + Reference to the next node)


class Node:

    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        # 30 -> none
        if self.head is None:  # 10 -> (20 -> none)
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print(self):
        info = self.head
        print(self.head.data)
        print(f"peek value : {info.data}")
        while info:
            print(f"{info.data} ->", end=" ")
            info = info.next
        print("None")

    def insert_at_start(self, data):
        # 10 -> 20 -> 30 -> None
        # 40 -> 10 -> 20 -> 30 -> None
        new_node = Node(data)
        # 40 -> None
        new_node.next = self.head
        # 40 -> 10 -> 20 -> 30 -> None

        self.head = new_node


obj = LinkedList()
obj.insert(10)
obj.insert(20)
obj.print()

# new_node is a local variable


# concept 1
# Q1. practice question

# name = "jp"


# class A:
#     name = "jai"

#     def __init__(self):
#         self.name = "jai prakash"

#     def info(self):
#         print(name)
#         # name = "jd"


# obj = A()
# obj.info()

# jai , jai


# def func():
#     print(value)
#     value = 2


# func()


# concept 2


# 1. falsy value = flase,None,empty,0
# 2. truly value = "string",numebr,true,
# l1 = ""
# print(bool(None))  # error


# def function():
#     print("radha")


# print(function)


# class A:
#     pass


# obj = A()
# obj.print()
# print(obj)
# print(A)