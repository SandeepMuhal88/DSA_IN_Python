# Q6. store every element of list in another list using for loop and find time and space complexity ?
def anotherList(l1):
    newList = []
    for i in l1:
        newList.append(i)
    print(newList)


l1 = [10, 20, 30]
anotherList(l1)



# time complexity = o(n)
# space complexity = 0(n)