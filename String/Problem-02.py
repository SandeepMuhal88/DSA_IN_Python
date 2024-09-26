# Q2. Accessing character in Python String ?

# accessing charcter
# name = "my name is jai"
# l1 = name.split()
# print(l1)
# print(l1[1])

def Access(str,index):
    List=str.split()
    if len(List) <=index or index <0:
        print("Out Of Range:-")
    else:
        print(List[index-1])

Access("My NAme is Sandeep Muhal",10)
Access("My NAme is Sandeep Muhal",15)
Access("My NAme is Sandeep Muhal",1)
Access("My NAme is Sandeep Muhal",2)
Access("My NAme is Sandeep Muhal",3)
Access("My NAme is Sandeep Muhal",4)
Access("My NAme is Sandeep Muhal",5)


# One Mistake in this Function Last Element Is Not Print
def access(string, index):
    l1 = string.split()
    if len(l1) <= index or index < 0:
        print("out of range")
    else:
        print(l1[index - 1])


access("this is your python class",4)



# time complexity = o(1)
# space complexity = o(1)

# l1 = [10, 20, 30, 40, 50]
# print(l1[3])