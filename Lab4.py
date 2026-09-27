##LAB 4 
#1.Implement stack using python
class stack:
    def __init__(self):
        self.stack = []

    def push(self,item):
        self.stack.append(item)
        print(item, "pushed into stack")

    def pop(self):
        if not self.stack:
            print("stack is empty")  
        else:
            print(self.stack.pop() , "popped from stack")   

    def display(self):
        print("stack:" , self.stack)   

stack = stack()     
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()
stack.pop()
stack.display()
#2.Implementing queue using python
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self , item):
        self.queue.append(item)  
        print(item, "added to queue")

    def dequeue(self):
        if not self.queue:
            print("queue is empty")   
        else:
            print(self.queue.pop(0), "removed from queue")

    def display(self):
        print("queue:" , self.queue)     

queue = Queue()
queue.enqueue(10) 
queue.enqueue(20)
queue.enqueue(30)
queue.display()
queue.dequeue()
queue.display()
#3.Binary search
def binary_search(arr , target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1
numbers = [10,20,30,40,50,60,70]
target = 50

result =  binary_search(numbers , target)

if result != -1:
    print("element found at index:" , result)
else:
    print("element not found")



