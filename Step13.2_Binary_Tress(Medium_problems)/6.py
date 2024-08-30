"""
Description: Zigzag traversal of binary tree
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root, nodes):
        self.root = root
        self.nodes = nodes

    def insert(self, root, value):
        if root is None:
            return Node(value)
        else:
            if value < root.value:
                root.left = self.insert(root.left, value)
            else:
                root.right = self.insert(root.right, value)
        return root

    def process(self):
        # Process the value and display it
        for i in range(1, len(self.nodes)):
            self.insert(self.root, self.nodes[i])

    def zig_zag_traversal(self, root):
        if not root:
            return
        stack = []
        values = []
        stack.append(root)
        left_to_right = True
        while stack:
            while stack:
                current = stack.pop()
                print(current.value, end=" ")
                if left_to_right:
                    if current.left:
                        values.append(current.left)
                    if current.right:
                        values.append(current.right)
                if not left_to_right:
                    if current.right:
                        values.append(current.right)
                    if current.left:
                        values.append(current.left)
            left_to_right = not left_to_right
            stack, values = values, []

class MyClass:
    def __init__(self):
        # Initialize variables
        self.nodes = [16,8,24,6,10,22,28,4,12,20,26]
        self.root = Node(self.nodes[0])
        self.BT = BinaryTree(self.root, self.nodes)

    def use_BinaryTree_class(self):
        # Call method from AnotherClass
        self.BT.process()
        print("Zigzag traversal of binary tree: ")
        self.BT.zig_zag_traversal(self.root)
        print()
def main():
    # Create an instance of MyClass
    my_instance = MyClass()
    # Call a method that uses AnotherClass
    my_instance.use_BinaryTree_class()

if __name__ == '__main__':
    main()