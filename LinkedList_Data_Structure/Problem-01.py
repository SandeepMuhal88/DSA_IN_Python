# What is Linked List
 
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None


    def insert(self,element):
        new_Node=Node(element)
        if self.head is None:
            self.head=new_Node
            return
        temp=self.head
        # while temp is not none
        while temp.next:
            temp=temp.next
        temp.next=new_Node

    def insertAtFirst(self,element):
        new_Node=Node(element)
        new_Node.next=self.head


    def display(self):
        temp=self.head
        while temp:
            print(f"{temp.data} ->",end=" ")
            temp=temp.next
        print("None")

    def Update(self,element,replace):
        if self.head is None:
            print("LinkedList is empty !!:)")
            return
        temp=self.head
        while temp:
            if temp.data==element:
                temp.data=replace
                return
            temp=temp.next
            print(f"{element} is not found")

        
    def Delete(self,element):
        if self.head is None:
            print("LinkedList is Empty")
            return
        
        if self.head.data==element:
            self.head=self.head.next
            return
        temp=self.head
        prev=None
        while temp and temp.data!=element:
            prev=temp
            temp=temp.next
        if temp:
            prev.next=temp.next
            return
        print(f"{element} Not found")
    def insertByIndex(self,index,element):
        new_Node=Node(element)
        if index == 0:
            new_Node.next = self.head
            self.head = new_Node
            return       
        temp=self.head
        current_index=0
        while temp and current_index<index-1:
            temp=temp.next
            current_index+=1
        if temp:
            new_Node.next=temp.next
            temp.next=new_Node
            return
        print("Out of range:-(")
        
# 11 -> 13 -> 16 -> 17 -> 19 -> 11 -> 52 -> None
obj=LinkedList()
obj.insert(11)
obj.insert(13)
obj.insert(16)
obj.insert(17)
obj.insert(19)
obj.insert(11)
obj.insert(52)
obj.display()
obj.Delete(17)
print("After delete value")
obj.insertByIndex(3,200)
obj.insertByIndex(5,200)
obj.insertByIndex(6,200)
obj.display()