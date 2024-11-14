# Singly LinkedList Re Program
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
        while temp.next:
            temp=temp.next
        temp.next=new_Node
    
    def display(self):
        temp=self.head
        while temp.next:
            print(f"{temp.data}->",end=" ")
            temp=temp.next
        print("None")

    def insertAtFirst(self,element):
        new_Node=Node(element)
        new_Node.next=self.head
        self.head=new_Node
    
    def Update(self,element,replace):
        if self.head is None:
            print("Error!! Linked List is Empty:!!")
            return
        temp =self.head
        while temp:
            if temp.data==element:
                temp.data=replace
                return
            temp=temp.next
        print("Element is Not Found!!:)")
    
    def Delete(self,element):
        if self.head is None:
            print("Error!! Linked List is Empty:!!")
            return
        if self.head.data==element:
            self.head=self.head.next
            return
        temp =self.head
        prev=None
        while temp and temp.data!=element:
            prev=temp
            temp=temp.next
        if temp:
            prev.next=temp.next
            return
        print("Element is Not Found!!:)")     

    def insertByIndex(self,index,element):
        new_Node=Node(element)
        if index==0:
            new_Node.next=self.head
            self.head=new_Node
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
        print("Out of range:))")



obj=LinkedList()
obj.insert(12)
obj.insert(32)
obj.insert(52)
obj.insert(72)
obj.insert(62)
obj.insert(52)
obj.insert(22)
obj.insertAtFirst(200)
obj.Update(52,"Bhavesh")
obj.display()
obj.Update("Bhavesh","Sandeep")
# obj.Delete(200)
# obj.Delete(22)
obj.insertByIndex(5,500)
obj.display()