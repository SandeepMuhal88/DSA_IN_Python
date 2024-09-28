# Q3. implement stack with function using while loop ?

stack=[]
def push(item):
    stack.append(item)
    menu()

def is_empty():
    if len(stack)==0:
        return True
    else:
        return False
    # return len(stack)==0

def POP():
    if not is_empty():
        stack.pop()
    else:
        print("Stack is Empty:))!!")

# [12,52,63,48]
def Peek():
    if not is_empty():
        print(stack[-1])
    else:
        print("Stack is Empty:))!!")
def size():
    return len(stack)



def menu():
    while True:

        print("1. Push element!             2.Pop Element!")
        print("3.Peek element!              4.Size od stack")
        print("5.Check is empty.             6.Exit. ")

        choice=int(input("Enter your choice:="))
        match choice:
            case 1:
                item=input("Enter item:-")
                push(item)
            case 2:
                POP()
               
            case 3:
                Peek()
               
            case 4:
                print("The size of the Stack:-",size())
            case 5:
                print(is_empty())
            case 6:
                break
            case _:
                print("Invalid day entered.")
                
print("====================================================================================================================================")
print("====================================================================================================================================")
print("=========================***********Perform Oeration In stack Data Structur***************==========================================")
print("====================================================================================================================================")
print("====================================================================================================================================")
menu()