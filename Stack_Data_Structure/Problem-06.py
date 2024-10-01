# Q6. find time and space complexity of stack when implement wihtin class ?
# overall time complexity = o(1)
# space complexity = o(n)
# l1 = [10]
# l1[len(l1)-1] = 50
# print()

# def push(self, element):
#     self.stack = self.stack + [None]
#     self.stack[len(self.stack) - 1] = element

class St:
    def __init__(self):
        self.stack=[]

    def push(self,item):
        self.stack+=[None]
        self.stack[len(self.stack)-1]=item


    def is_empty(self):
        if len(self.stack)==0:
            return True
        else:
            return False
        

    def pop(self):
        if not self.is_empty():
            print("Last element is delete:-",self.stack.pop())
        else:
            print("Stack is empty:)))!!")
    
    def peek(self):
        if not self.is_empty():
            print("Top most element in stack:-",self.stack[-1])
        else:
            print("Stack is empty:)))!!")
    
    
    def size(self):
        print("The Size of the Stack :-",len(self.stack))
    
    def display(self):
        print("The Stack :-",self.stack)
        

        

obj=St()
print(obj.is_empty())
obj.push(12)
obj.push(26)
obj.push(45)
obj.push(77)
obj.push(84)
obj.push(78)
obj.size()
obj.peek()
obj.pop()