# Q5. implement stack with class using while loop ?
class Stack:
    def __init__(self):
        self.stack=[]

    def push(self,item):
        self.stack+=[None]
        self.stack[len(self.stack) - 1] = item

    def is_empty(self):
        if len(self.stack)==0:
            return True
        else:
         return False

    def pop(self):
        if not self.is_empty():
             self.stack.pop()
        else:
            print("Stack Is empty:!!!")
    
    def size(self):
        print("The Size of the Stack :-",len(self.stack))
    
    def peek(self):
        if not self.is_empty():
             print("Top Element in stack:-",self.stack[-1])
        else:
            print("Stack Is empty:!!!")        
    def display(self):
        print("The Stack :-",self.stack)
        


obj=Stack()

obj.push(52)
obj.push(43)
obj.push(29)
obj.push(81)
obj.push(49)
obj.push(410)
obj.display()
obj.pop()
obj.size()

print(obj.is_empty())
obj.peek()