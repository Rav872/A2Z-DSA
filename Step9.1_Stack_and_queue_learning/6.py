# Implement queue using linked list

class Node:
    def __init__(self, data=0):
        self.next = None
        self.data = data

class Queue:
    def __init__(self):
        self.front = None
        self.init = None

    def enqueue(self, data):
        newNode = Node(data)
        if self.front is None:
            self.init = newNode
            self.front = newNode
        else:
            self.front.next = newNode
            self.front = newNode
    
    def dequeue(self):
        temp = self.init
        if self.front is None:
            return "Queue is empty"
        else:
            self.init = temp.next
            temp = None
        
    def firstItem(self):
        if self.init is None:
            return "Queue is empty"
        return self.init.data
    
    def isEmpty(self):
        return self.init is None
    
q = Queue()

q.enqueue(56)
q.enqueue(23)
q.enqueue(29)
q.enqueue(5)
q.enqueue(33)

print("Next in line: ", q.firstItem())
q.dequeue()
print(q.isEmpty())
print("Next in line: ", q.firstItem())



