"""
Description: Diameter of a binary tree
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

    def diameter_of_tree(self, root):
        self.diameter = 0

        def height(root):
            if root is None:
                return 0
            left_height = height(root.left)
            right_height = height(root.right)

            self.diameter = max(self.diameter, left_height + right_height)
            return max(left_height, right_height) + 1

        height(root)
        return self.diameter



class MyClass:
    def __init__(self):
        # Initialize variables
        self.nodes = [1,2,4,12,7,3,21,11,9]
        self.root = Node(1)
        self.BT = BinaryTree(self.root, self.nodes)

    def use_BinaryTree_class(self):
        # Call method from AnotherClass
        self.BT.process()
        print("Diameter of a binary tree: ", self.BT.diameter_of_tree(self.root), end=" ")
        print()
def main():
    # Create an instance of MyClass
    my_instance = MyClass()
    # Call a method that uses AnotherClass
    my_instance.use_BinaryTree_class()

if __name__ == '__main__':
    main()