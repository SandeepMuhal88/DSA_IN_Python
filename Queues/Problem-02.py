# Q2. implement queue with function ?
# 1. different data types (store)
# 2. muttable
queue=[]
def enqueue(item):
        global queue
    # queue.append(item)
        queue+=[None]
        queue[len(queue) - 1] = item

def size():
    print("The size of Queue:-",len(queue))
def is_empty():
    if len(queue)==0:
        return True
    else:
        return False

def peek():
    if not is_empty():
        print(f"Top element in queue:-{queue[0]}")

    else:
        print("Queue is empty:))")

def denqueue():
    if not is_empty():
        print(f"Element is delete:-{queue.pop(0)}")

    else:
        print("Queue is empty:))")


def display():
    print("Display Queues:-",queue)

print(is_empty())
size()
enqueue(12)
enqueue(52)
enqueue(63)
enqueue(78)
enqueue(96)
size()
