# def BubbleSort(array):
#     n=len(array)
#     for i in range(n):
#         for j in range(0,n-i-1):
#             if array[j]>array[j+1]:
#                 array[j],array[j+1]=array[j+1],array[j]
#     print(f"Sorted array:-{array}")

def BubbleSort(array):
    for i in range(len(array)):
        for j in range(0,len(array)-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
    print(f"Sorted Array:-{array}")


array=[15,96,1,4,5,2,7,10,63,28]
print(len(array))
BubbleSort(array)
