# Implement queue using array

class Queue:
    def __init__(self):
        self.que = []
        self.front = -1

    def enqueue(self, element):
        self.que.append(element)
        self.front += 1

    def dequeque(self):
        if not self.isEmpty():
            self.que.pop(0)
            self.front -= 1
        else:
            return "Queue is empty"

    def isEmpty(self):
        return len(self.que) == 0

    def lastItem(self):
        if not self.isEmpty():
            return self.que[-1]
        else:
            return "Queue is empty"

    def firstItem(self):
        if not self.isEmpty():
            return self.que[0]
        else:
            return "Queue is empty"

q = Queue()
q.enqueue(34)
q.enqueue(90)
q.enqueue(45)
q.enqueue(41)
q.dequeque()
print(q.lastItem())
print(q.firstItem())
