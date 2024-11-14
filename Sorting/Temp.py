# def Dice():
#     for i in range(1, 7):
#         for j in range(1, 7):
#             print(i, j)


# Dice()

# bubble sort


# def BubbleSort(array):
#     for i in range(len(array)):
#         for j in range(len(array) - i - 1):
#             if array[j] > array[j + 1]:
#                 array[j], array[j + 1] = array[j + 1], array[j]
#     return array


# print(BubbleSort([20, 10, 50, 40, 30]))


# selection sort


# def SelectionSort(array):
#     for i in range(len(array)):
#         min = i
#         for j in range(i+1, len(array)):
#             if array[j] < array[min]:
#                 min = j
#         array[i], array[min] = array[min], array[i]
#     return array


# print(SelectionSort([20, 10, 50, 40, 30]))


# insertion sort


# def InsertionSort(array):
#     for i in range(1, len(array)):
#         key = array[i]
#         previous = i - 1

#         while previous >= 0 and key < array[previous]:
#             array[previous + 1] = array[previous]
#             previous -= 1
#         # previous = -1
#         array[previous + 1] = key

#     return array


# print(InsertionSort([20, 10, 50, 40, 30]))


# merge Sort


# 1. concept
# array = [10, 20, 30, 40, 50, 60, 70]
# print(array[3:])
# print(array[:3])

# 2.concept : extend
# array1 = [1, 2, 3]
# array.extend(array1)
# print(array)


def MergeSort(array):
    # case 1: if length of array is 1
    if len(array) <= 1:
        return array

    # case2 : divide
    mid = len(array) // 2
    # 20, 10, 50, 40, 30

    left_half = MergeSort(array[:mid])
    right_half = MergeSort(array[mid:])

    return Merge(left_half, right_half)


def Merge(left, right):
    sorted_array = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])

    return sorted_array


print(MergeSort([20, 10, 50, 40, 30]))