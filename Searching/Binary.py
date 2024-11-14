# binary search

# 1.data must be in ascending order
# high = 0
# lower= 7-1
# mid = (left + right)//2 #3
def BinarySearch(array,target):
    high=0
    lower=len(array)-1
    while high<=lower:
        mid=(high+lower)//2
        if mid==target:
            print(f"{target} is found :)")
            return
        elif mid<target:
            high=mid+1
        else:
            lower=mid-1
    print(f"{target} is not found :(")


array=[15,96,1,4,5,2,7,10,63,28]
BinarySearch(array,4)
BinarySearch(array,400)