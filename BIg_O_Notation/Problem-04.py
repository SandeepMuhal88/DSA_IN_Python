# Q4. compare element of list with another list ?

def compare(l1, l2):
    for i in l1:
        for j in l2:
            print(i, j)

# Question :- Which is gretest


def Gretestcompare(l1, l2):
    for i in l1:
        for j in l2:
           if i >j:
               print(i)
           else:
               print(j)

# time complexity = 0(n^2)


l1 = [10, 20, 30]
l2 = [5, 15, 25]

compare(l1, l2)
Gretestcompare(l1, l2)