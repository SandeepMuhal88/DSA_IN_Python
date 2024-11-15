# Dynamic programing
def dynamic(coins, amount):
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for j in coins:
            if i - j >= 0:  # or i >= j
                dp[i] = min(dp[i], dp[i - j] + 1)
    if dp[amount] != amount + 1:
        print("minimum coins required :", dp[amount])
        print(dp)
    else:
        print("can not make this amount")


dynamic([1, 3, 4], 6)
# dynamic = time consuming but correct
# array = [6] * 5
# print(array)
