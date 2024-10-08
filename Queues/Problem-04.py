# Q4. find time and space complexity

# Make a queue data structure
# Create a list name queue
queue=[]
# Create a function to inster element into queue::
def enqueue(element):
    global queue
    queue=queue+[None]
    queue[len(queue)-1]=element
     # time complexity = o(1)
    # space complexity = o(1)

# Create a function for check Queue is empty ant not empty
def is_empty():
    global queue
    if len(queue)==0:
        return True
    else:
        return False
    
    # time complexity = o(1)
    # space complexity = o(1)

# Create an function to delete element in queue

def dequeue():
    global queue
    if not is_empty():
        temp_queue=[]
        for i in range(1,len(queue)):
            temp_queue.append(queue[i])
        queue=temp_queue
    else:
        print("Queue is empty!!)))")

    # time complexity = o(n)
    # space complexity = o(n)


# Create an function to check size of queue
def size():
    print("The size of the Queue:-",len(queue))
    # time complexity = o(1)
    # space complexity = o(1)

# Create an function to print all data in queue
def display():
    print("The queue Data:-",queue)
    # time complexity = o(1)
    # space complexity = o(1)