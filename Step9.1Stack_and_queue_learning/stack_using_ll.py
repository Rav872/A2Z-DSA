# stack using linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, val):
        self.node = Node(self.val)
        if self.node is None:
            return "Stack overflow"
        else:
            self.node.next = top
            top = self.node
    def pop(self):
        x = -1
        p = None
        if self.top is None:
            return "Stack underflow"
        else:
            p = self.top
            self.top = self.top.next
            x = self.p.data
    def isEmpty(self):
        return not self.top
    
s = Stack()
s.push()
        