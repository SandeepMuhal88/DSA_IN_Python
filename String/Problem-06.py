# Q6. how to update single element in list ?


# string = "my name is jai"

# print(string.split())
# a = list(string)
# print(a)
# a[3] = "p"
# sting = "".join(a)
# print(sting)


# Update("my name is jai", 1, "p")


def updateElement(string, element, update):
    l1 = list(string)
    if element in l1:
        index = l1.index(element)
        print(f"{element} found at {index+1} Postion")
        print("updated string :")
        l1[index] = update
        string = "".join(l1)
        print(string)
    else:
        print("Element not found ")


string = "this is your python class"
element = "t"
update = "T"
updateElement(string, element, update)