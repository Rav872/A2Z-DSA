# Stack using an array

class Stack:
    def __init__(self):
        self.lst = []
        self.topPtr = -1

    def push(self, element):
        self.element = element
        self.lst.append(self.element)
        self.topPtr += 1

    def pop(self):
        if not self.isEmpty():
            self.topPtr -= 1
            return self.lst.pop()
        else:
            return "Stack is empty"
        

    def peek(self):            # peek index
        if not self.isEmpty():
            return self.topPtr
        else:
            return "stack is empty"

    def top(self):
        if not self.isEmpty():
            return self.lst[-1]
        else:
            return "stack is empty"
    
    def isEmpty(self):
        return len(self.lst) == 0

s = Stack()

s.push(15)
s.push(36)
s.push(45)
s.push(90)
s.pop()
print(s.top())
print(s.peek())
print(s.isEmpty())