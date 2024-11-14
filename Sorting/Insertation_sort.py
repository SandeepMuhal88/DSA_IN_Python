# Insertation_Sort Algorithm
def InsertationSort(array):
    for i in range(1,len(array)):
        key=array[i]
        previous=i-1
        while previous>=0 and array[previous]>key:
            array[previous+1]=array[previous]
            previous -= 1
        array[previous+1]=key
    return array


def insertation(arr):
    for i in range(1,len(arr)):
        j=arr[i]
        pre=i-1
        while j<arr[pre] and pre>=0:
            arr[pre+1]=arr[pre]
            pre-=1
        arr[pre+1]=j
    return arr

arr=[20,63,10,30,50,90]
print(insertation(arr))
array=[15,96,1,4,5,2,7,10,63,28]
print(InsertationSort(array))