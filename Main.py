class MyCircularQueue:
    def __init__(self, size: int):
        # Write code here
        self.size = size 
        self.rear = -1
        self.front = -1 
        self.queue = []
        
        

    def enqueue(self, value: int) -> bool:
        # Write code here
        if not is_full():
            self.rear = (self.rear+1)%len(self.queue)
            
            self.size = self.size+1
            
        

    def dequeue(self) -> bool:
        # Write code here
        self.front = (self.front+1)%len(self.size)
        self.size = self.size-1

    def get_front(self) -> int:
        # Write code here
        if not self.is_empty():
            self.front+=1
            return self.queue[self.front]
        else:
            return -1
                

    def get_rear(self):
        # Write code here
        if not self.is_empty():
            self.rear+=1
            return self.queue[self.rear]
        else:
            return -1

    def is_empty(self):
        # Write code here
        if self.size == 0:
            return 1
        else :
            return 0 

    def is_full(self):
        # Write code here
        if self.size == len(self.queue):
            return 1
        else :
            return 0
        
            


# Do not change the following code
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
data = []
for item in input().split(','):
    item = item.strip()
    if item == '-':
        data.append([])
    else:
        data.append([int(item)])
obj = MyCircularQueue(data[0][0])
result = []
for i in range(len(operations)):
    if i == 0:
        result.append(None)
    elif operations[i] == "enqueue":
        result.append(obj.enqueue(data[i][0]))
    elif operations[i] == "get_rear":
        result.append(obj.get_rear())
    elif operations[i] == "get_front":
        result.append(obj.get_front())
    elif operations[i] == "dequeue":
        result.append(obj.dequeue())
    elif operations[i] == "is_full":
        result.append(obj.is_full())
    elif operations[i] == "is_empty":
        result.append(obj.is_empty())

print(result)
