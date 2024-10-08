# Q3. implememnt queue without inbuilt function ?

queue=[]

def enqueue(element):
    global queue 
    queue+=[None] 
    queue[len(queue)-1]=element
    # print(len(queue))

def is_empty():
    if len(queue)==0:
        return True
    else:
        return False
    

def dequeue():
    global queue
    if not is_empty():
        Temp_queue = []
        for i in range(1, len(queue)):
            Temp_queue.append(queue[i])
        queue = Temp_queue
    else:
        print("Queue is empty!!!)))))")

def peek():
    if not is_empty():
        print("Top element n queue:-",queue[0])
    else:
        print("Queue is empty!!!)))))")
def size():
    print("The size of Queue:-",len(queue))

def display():
    print("The Data in queue:-",queue)

   
print(is_empty())
size()
enqueue(12)
enqueue(52)
enqueue(63)
size()
print(is_empty())
enqueue(78)
enqueue(96)
enqueue(410)
dequeue()
enqueue(310)
display()
dequeue()
size()
display()




















# x = 10


# def modify():
#     global x
#     x = 20


# print(x)
# modify()
# print(x)


# l1 = []

# for i in range(10, 100, 10):
#     l1.append(i)

# print(l1)

# numebr = 2

# l1 = [10 * 10] + numebr  # l1 = [10][10] ,[10,10] ,[20] ,invalid

# print(l1)

# l1 = [10, 20]
# l3 = [40, 50]
# l2 = l1 + l3
# print(l2)


# concept 1

# name = "radha"
# print(name * 2)
# n = 5
# for i in range(n):
#     print("jd" * i)


# concept 3

# l1 = [10, 20, 30, 40]
# l2 = []
# for i in range(1, len(l1)):
#     l2.append(l1[i])
# print(l2)