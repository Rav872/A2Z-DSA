#Implement stack using queue
from collections import deque


class Stack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
        self.topPtr = -1
    def push(self, element):
        self.topPtr += 1
        return self.q1.append(element)

    def pop(self): # restriction is that you can remove last item from queue directly
        if not self.isEmpty():
            while len(self.q1) > 1:
                self.q2.append(self.q1.popleft())
            self.q1.popleft()
            self.topPtr -=1
            self.q2, self.q1 = self.q1, self.q2
        else:
            return "stack is empty"
    
    def peek(self):
        if not self.isEmpty():
            return len(self.q1)
        else:
            return "stack is empty"

    def top(self):      # from queue, you can direct access last item because of FIFO property
        if not self.isEmpty():
            while len(self.q1) > 1:
                self.q2.append(self.q1.popleft())
            result = self.q1[0]
            self.q2.append(self.q1.popleft())
            self.q2, self.q1 = self.q1, self.q2
            return result
        else:
            return "stack is empty"

    def isEmpty(self):
        return len(self.q1) == 0

s = Stack()
s.push(40)
s.push(10)
s.push(9)
s.push(12)
s.push(28)
s.pop()

print("Peek:", s.peek())
print("Top: ", s.top())
print(s.isEmpty())

