"""
Description: Binary tree representation in python, similar like C++, python
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

class BinaryTree:
    def __init__(self, root_node, nodes):
        self.root_node = root_node
        self.nodes = nodes

    def insert(self, root, value):
        if root is None:
            return Node(value)
        else:
            if value < root.value:
                root.left_child = self.insert(root.left_child, value)
            else:
                root.right_child = self.insert(root.right_child, value)
        return root

    def process(self):
        # Process the value and display it
        for i in range(1, len(self.nodes)):
            self.insert(self.root_node, self.nodes[i])
    
    def printBT(self, root_node):
        if root_node == None:
            return
        print(root_node.value, end=": ")
        if root_node.left_child:
            print("L", root_node.left_child.value, end=" ")
        if root_node.right_child:
            print("R", root_node.right_child.value, end=" ")
        print()
        self.printBT(root_node.left_child)
        self.printBT(root_node.right_child)

class MyClass:
    def __init__(self):
        # Initialize variables
        self.nodes = [1,2,4,12,7,3,21,11,9,10]
        self.root_node = Node(1)
        self.BT = BinaryTree(self.root_node, self.nodes)

    def use_BinaryTree_class(self):
        # Call method from AnotherClass
        self.BT.process()
        self.BT.printBT(self.root_node)


def main():
    # Create an instance of MyClass
    my_instance = MyClass()
    # Call a method that uses AnotherClass
    my_instance.use_BinaryTree_class()

if __name__ == '__main__':
    main()