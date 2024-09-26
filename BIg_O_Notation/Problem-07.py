# Q7. find sum of element of list and also find time and space complexity ?
def findSum(l1):
    add = 0
    for i in l1:
        add += i
    print(f"sum of list : {add}")


findSum([1, 2, 3, 4, 5, 6])


# time complexity = o(n)
# space complexity =  o(n)