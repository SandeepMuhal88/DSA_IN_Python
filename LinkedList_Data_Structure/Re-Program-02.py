# Doubly LinkedList
class Node:
    def __init__(self,value):
        self.data=value
        self.prev=None
        self.next=None
    

class LinkedList:
    def __init__(self):
        self.head=None

    def display(self):
        print("None",end="<-->")
        temp=self.head
        while temp:
            print(f"{temp.data} <-->",end=" ")
            temp=temp.next
        print("None")

    def insert(self,element):
        new_Node=Node(element)
        if self.head is None:
            self.head=new_Node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_Node
        new_Node.prev=temp
    
    def insertAtFirst(self,element):
        new_Node=Node(element)
        new_Node.next=self.head
        if self.head:
            self.head.prev=new_Node
        self.head=new_Node

    def InsertbyIndex(self,index,element):
        new_Node=Node(element)
        if index==0:
            if self.head is None:
                self.head=new_Node
                return
            new_Node.next=self.head
            self.head.prev=new_Node
            self.head=new_Node
            return
        temp=self.head
        current_index=0
        while temp and current_index<-1:
            temp=temp.next
            current_index+=1
        if temp:
            new_Node.next=temp.next
            if temp.next:
                temp.next.prev=new_Node
            temp.next=new_Node
            new_Node.prev=temp
            return
        print("Out of the range")

    def Update(self,element,replace):
        temp=self.head
        if self.head is None:
            print("Linkeflist is Empty:)")
            return
        elif temp is not None:
            while temp:
                if temp.data==element:
                    temp.data=replace
                    break
                temp=temp.next
        else:
         print(f"{element} is Not Found:((")


    def display(self):
        print("None",end="<-->")
        temp=self.head
        while temp:
            print(f"{temp.data} <-->",end=" ")
            temp=temp.next
        print("None")

    def delete(self,element):
        if self.head is None:
            print("LinkedList is empty:((")
            return
        if self.head.data==element:
            self.head=self.head.next
            if self.head:
                self.head.prev=None
            return
        temp=self.head
        while temp and temp.data != element:
            temp = temp.next
        if temp:
            if temp.next:
                temp.next.prev = temp.prev
            if temp.prev:
                temp.prev.next = temp.next
            return
        print(f"{element} Not found")       
obj=LinkedList()
obj.insert(22)
obj.insert(63)
obj.insert(64)
obj.insert(78)
obj.insert(96)
obj.insert(44)
obj.insertAtFirst(500)
obj.insertAtFirst("Start")
obj.InsertbyIndex(4,154)
obj.InsertbyIndex(0,2000)
obj.display()