def LineaSerach(array ,target):
    for i in array:
        if i==target:
            print(f"{target} is found :)")
            return
    print(f"{target} is not found :(")

array=[15,96,1,4,5,2,7,10,63,28]
LineaSerach(array,4)
LineaSerach(array,400)