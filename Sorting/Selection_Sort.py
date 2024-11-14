# Selection Sort

def SelectionSort(arr):
    for i in range(len(arr)):
        min=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]
    return arr

arr=[20,63,10,30,50,90]
print(SelectionSort(arr))
array=[15,96,1,4,5,2,7,10,63,28]
print(SelectionSort(array))