    
# Q4. implement stack with class ?


# concept 1
# we can make only 2 variable = myth
# class A:
#     def __init__(self,name, age,height ):
#         self.n = name
#         self.age = age

class stack:
    def __init__(self):
        self.stack=[]
    
    def push(self,item):
        self.stack.append(item)
    
    def is_empty(self):
        if len(self.stack)==0:
            return True
        else:
            return False
    
    def pop(self):
        if not self.is_empty():
            print("Element Is delete In stack:-",self.stack.pop())
        else:
            print("Stack is empty:)))")
    
    def peek(self):
        if not self.is_empty():
            print(self.stack[len(self.stack) - 1])
        else:
            print("Stack is empty:)))")
    
    def display(self):
        print(self.stack)

    def size(self):
        print("The Size of the Stack :-",len(self.stack))
        

obj=stack()
obj.push(120)
obj.push(202)
obj.push(305)
obj.push(501)
obj.push(847)
obj.push(457)
obj.pop()
# print(obj.is_empty())
# obj.size()
obj.peek()
obj.size()
obj.display()
print(obj.is_empty())