# def access(string,index):
#     l1=string.split()
#     if len(l1)<index:
#         print("Out of range!!")
#     else:
#         print(l1[index])

# access("M name is sandeep muhal",3)

def access(string,index):
    l1=string.split()
    if len(l1)<index:
        print("Out of range!!")
    else:
        print(l1[index-1])

access("M name is sandeep muhal",3)
# Time complexicty:- o(n)