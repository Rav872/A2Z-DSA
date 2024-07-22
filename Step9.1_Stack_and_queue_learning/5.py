# Implement stack using linked list
# Stack using linked list is single linked list implementation of insertion in first and deletion in first

class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.prevPtr = None
        self.topPtr = None

    def push(self, data):
        newNode = Node(data)
        if self.topPtr is None:
            self.topPtr = newNode
            self.prevPtr = None
        else:
            newNode.next = self.topPtr
            self.prevPtr = self.topPtr
            self.topPtr = newNode

    def pop(self):
        temp = self.prevPtr
        if self.topPtr is None:
            return "stack is empty"
        if self.prevPtr is None:
            self.topPtr =  None
        else:
            self.prevPtr = temp.next
            self.topPtr = None
            self.topPtr = temp

    def top(self):
        if self.topPtr is None:
            return "stack is empty"
        return self.topPtr.data

    def isEmpty(self):
        return self.topPtr is None

s = Stack()

s.push(15)
s.push(36)
s.push(19)
s.push(34)
s.push(82)
s.pop()
s.pop()

print(s.top())
print(s.isEmpty())


