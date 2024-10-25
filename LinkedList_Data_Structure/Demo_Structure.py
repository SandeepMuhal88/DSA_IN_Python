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

# Create a data structure name:- Linked list

class Node:
    def __init__(self,Value):
        self.data=Value
        self.next= None

class LinkedList:
    def __init__(self):
        self.head=None
    
    # We assign self.head to new_Node the it will object
    def insert(self,data):

        new_Node=Node(data)
        if self.head is None:
            self.head=new_Node
            return
        last=self.head
        while last.next:
            last=last.next
        last.next=new_Node
    
    def display(self):
        dis=self.head
        while dis:
            print(f"{dis.data} -> ",end=" ")
            dis=dis.next
        print("None")
    
    def insertATstart(self,element):
        new_Node=Node(element)
        new_Node.next=self.head
        new_Node.next=self.head
    
    def delete(self,element):
        if self.head and self.head.data:
            self.head=self.head.next
            temp=self.head
            prev=None
        
        while temp and temp.data!=element:
            prev=temp
            temp=temp.next
def insertAtIndex(self, index, element):
        newNode = Node(element)
        if index == 0:
            newNode.next = self.head
            self.head = newNode
            return
        temp = self.head 
        current_index = 0

        while temp and current_index < index - 1:
            temp = temp.next
            current_index += 1

        if temp is None:
            print(f"Index {index} is out of range.")
            return
        newNode.next = temp.next
        temp = self.head 
        temp.next = newNode    
        
                
def insertByIndex(self, index, element):
        newNode = Node(element)
        if index == 0:
            newNode.next = self.head
            self.head = newNode
            return
        temp = self.head
        current_index = 0
        while temp and current_index < index - 1:
            temp = temp.next
            current_index += 1
        if temp:
            newNode.next = temp.next
            temp.next = newNode
        else:
            print(f"{element} Not found")
obj=LinkedList()
obj.insert(12)
obj.insert(13)
obj.insert(40)
obj.insert(100)
obj.display()


# new_node is a local variable
# concept 1
# Q1.practice question

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