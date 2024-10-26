# Q2. what is double linked list ?


class Node:
    def __init__(self, value):
        self.data = value
        self.prev = None
        self.next = None
    
class DoublyLinkedList:
    def __init__(self):
        self.head=None

    def insert(self,element):
        obj=Node(element)
        if self.head is None:
            self.head=obj
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=obj
        obj.prev=temp
    
    def Update(self,element,replace):
        temp=self.head
        if temp is None:
            print("LinkedList is None:((")
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
        temp=self.head
        while temp:
            print(f"{temp.data} <-->",end=" ")
            temp=temp.next
        print("None")
        # print(self.head.next.next.prev.next.prev.data)
    
    def insertAtFirst(self,element):
        obj=Node(element)
        obj.next=self.head
        if self.head:
            self.head.prev=obj
        self.head=obj

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
        while temp and temp.data!=element:
            temp=temp.next
        if temp:
            if temp.next:
                temp.next.prev=temp.prev
            if temp.prev:
                temp.prev.next = temp.next
            return                
        print(f"{element} Not found")

    def InsertbyIndex(self,element,index):
        obj=Node(element)
        if index==0:
            obj.next=self.head
            self.head=obj
            return
        temp=self.head
        current_index=0
        while temp and current_index<index-1:
            temp=temp.next
            current_index+=1
        if temp:
            obj.next=temp.next
            temp.next=obj
        print(f"Out of Range")
obj=DoublyLinkedList()
print("Use Insert Method")
obj.insert(12)
obj.insert(11)
obj.insert(18)
obj.insert(17)
obj.insert(16)
obj.insert(15)
obj.insert(14)
obj.insert(13)
print("Use insertAtFirst")
obj.insertAtFirst(500)
obj.display()
print("Use InsertbyIndex")
obj.InsertbyIndex(5,200)
obj.InsertbyIndex(2,200)
obj.InsertbyIndex(7,200)
obj.display()
print("Use Delete Method")
obj.delete(16)
obj.Update(15,100)
obj.display()