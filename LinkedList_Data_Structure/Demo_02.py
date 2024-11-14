# double Linked List


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, element):
        newNode = Node(element)
        if self.head is None:
            self.head = newNode
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newNode
        newNode.prev = temp

    def insertAtStart(self, element):
        newNode = Node(element)
        # data = element, next = None , prev = None
        newNode.next = self.head
        if self.head:
            self.head.prev = newNode
        self.head = newNode

    def display(self):
        temp = self.head
        while temp:
            print(f"{temp.data} <-->", end=" ")
            temp = temp.next
        print("None")

    def Update(self, element, replace):
        temp = self.head
        if self.head is None:
            print("Linked List is Empty !")
        elif self.head is not None:
            while temp:
                if temp.data == element:
                    temp.data = replace
                    break
                temp = temp.next
            else:
                print(f"{element} Not found")

    def delete(self, element):
        if self.head is None:
            print("linked list is empty")
            return

        if self.head.data == element:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            return

        temp = self.head

        while temp and temp.data != element:
            temp = temp.next
        if temp:
            if temp.next:
                temp.next.prev = temp.prev
            if temp.prev:
                temp.prev.next = temp.next
            return
        print(f"{element} Not found")

    def insertByIndex(self, index, element):
        newNode = Node(element)
        if index == 0:

            if self.head is None:
                self.head = newNode
                return
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            return
        current_index = 0
        temp = self.head
        while temp and current_index < index - 1:
            temp = temp.next
            current_index += 1

        if temp:
            newNode.next = temp.next
            if temp.next:
                temp.next.prev = newNode
            temp.next = newNode
            newNode.prev = temp

            return
        print("Index not found")

    def info(self):
        print(self.head.next.next.next.next.data)
        print(self.head.next.next.next.next.prev.data)
        print(self.head.next.next.next.prev.data)


obj = LinkedList()
obj.insert(10)
obj.insertAtStart("Radha")
obj.insertAtStart("Krishna")
obj.insert(20)
obj.delete("Krishna")
obj.Update("Radha", "Radha Rani")
obj.insertByIndex(0, "sandeep")
obj.insertByIndex(3, "jd")
obj.display()
obj.info()

# single linked list
# double linked list
# circuler linked list (single linked list)
# circuler linked list (double linked list)