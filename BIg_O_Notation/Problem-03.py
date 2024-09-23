# Q3. find element in list using binary search ?
def BinarySearch(l1,traget):
    start=0
    end=len(l1)-1
    while start<=end: 
         # floor division
         mid = (start + end) // 2

         if l1[mid]==traget:
              return f"{traget} is found"
         elif l1[mid]<traget:
              start=mid+1
         else:
              end=mid-1
    return f"{traget} is not found"





# time complexity = o(log n)
# print(BinarySearch([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 80))


# Input List from User
x=int(input("Enter the size of List:-"))
print("Enter list Element:-")
l1=[]
for i in range(0,x,1):
    l1.append(int(input(f"Enter {i} value in list:-")))

print(l1)
l1.sort()
print("Sorted List",l1)
traget=int(input("Insert value you want to find:-"))
print(BinarySearch(l1,traget))
