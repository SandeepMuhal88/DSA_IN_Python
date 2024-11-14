# Merge Sort
def MergeSort(array):
    # case 1: if length of array is 1
    if len(array) <= 1:
        return array

    # case2 : divide
    mid = len(array) // 2
   

    left_half = MergeSort(array[:mid])
    right_half = MergeSort(array[mid:])

    return Merge(left_half, right_half)


def Merge(left, right):
    sorted_array = []
    v1 = v2 = 0

    while v1 < len(left) and v2 < len(right):
        if left[v1] < right[v2]:
            sorted_array.append(left[v1])
            v1 += 1
        else:
            sorted_array.append(right[v2])
            v2 += 1
    sorted_array.extend(left[v1:])
    sorted_array.extend(right[v2:])

    return sorted_array

array=[15,96,1,4,5,2,7,10,63,28]
print(MergeSort(array))