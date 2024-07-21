#Implement queue using stack

class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []
    
    def enqueue(self, element):
        self.s1.append(element)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"

        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def isEmpty(self):
        return len(self.s1) == 0 and len(self.s2) == 0
    
    def length(self):
        return len(self.s1) + len(self.s2)
    
    def firstItem(self):
        if self.isEmpty():
            return "Queue is empty"

        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

q1 = Queue()

q1.enqueue(58)
q1.enqueue(90)
q1.enqueue(71)
q1.enqueue(44)
q1.enqueue(13)

q1.firstItem()
print("Length: ", q1.length())
print(q1.isEmpty())
q1.dequeue()
print(q1.firstItem())