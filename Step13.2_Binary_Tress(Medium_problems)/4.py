"""
Description: Maximum path sum of a binary tree
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

    def maximum_path_sum(self, root):
        self.max_sum = float('-inf')

        def sum(root):
            if root is None:
                return 0
            left_sum = max(sum(root.left), 0)  # Only add positive contributions
            right_sum = max(sum(root.right), 0)  # Only add positive contributions
        
            # Compute the path sum passing through this node
            current_sum = root.value + left_sum + right_sum
            self.max_sum = max(self.max_sum, current_sum)
        
            # Return the maximum sum path starting from this node
            return root.value + max(left_sum, right_sum)

        sum(root)
        return self.max_sum

class MyClass:
    def __init__(self):
        # Initialize variables
        self.nodes = [1,2,4,12,7,3,21,11,9]
        self.root = Node(1)
        self.BT = BinaryTree(self.root, self.nodes)

    def use_BinaryTree_class(self):
        # Call method from AnotherClass
        self.BT.process()
        print("Maximum path sum of a binary tree: ", self.BT.maximum_path_sum(self.root), end=" ")
        print()
def main():
    # Create an instance of MyClass
    my_instance = MyClass()
    # Call a method that uses AnotherClass
    my_instance.use_BinaryTree_class()

if __name__ == '__main__':
    main()