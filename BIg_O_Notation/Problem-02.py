# 1. Linear Time Complexity: Big O(n) Complexity ?

# Linear time complexity (O(n)) means that the time taken by an algorithm grows linearly with 
# the size of the input. In other words, if you double the size of the input, the time 
# required to complete the algorithm will roughly double as well.

# Q find specific element in list ?
# Input List from User
x=int(input("Enter the size of List:-"))
print("Enter list Element:-")
l1=[]
for i in range(0,x,1):
    l1.append(int(input(f"Enter {i} value in list:-")))

print(l1)
y=int(input("Insert value you want to find:-"))

# Method-01
# for i in l1:
#     if(i==y):
#         print(f"{y} found !!")
#         break
#     else:
#         print(f"{y} Not found !!")
#         break

# Method02
# for i in l1:
#     flage=False
#     if(i==y):
#         print(f"{y} found !!")
#         flage=True
#         break
# if(flage==False):
#  print(f"{y} Not found !!")


# Using Funcation
def findelement(l1,y):
    Flage=True
    for i in l1:
     if(i==y):
        print(f"{y} found !!")
        flage=True
        break
    if(flage==False):
        print(f"{y} Not found !!")

findelement(l1,y)