# [1,2,5,10,20,50] = 48[20,20,5,2,1]
# [1,2,5,10,20,50,100,200,500] = 67[50,10,5,2]


# greedy
# [1,5,2,10,20,50]
def Greedy(coins, amount):
    coins.sort(reverse=True)
    count = 0
    array = []

    for i in coins:
        count = count + amount // i
        if amount // i > 0:
            que = amount // i
            for j in range(que):
                array.append(i)
        amount = amount % i
        if amount == 0:
            break
    if amount == 0:
        print("Number of coins required :", count)
        print("coins :", array)
    else:
        print("this amount can not be maked")

Greedy([1,3,4],6)