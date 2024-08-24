"""
Description: Introduction to Binary Tree, Count number of node in binaryTree with h height

Binary Tree Representation:
A binary tree is a type of data structure in which each node has at most two children.
These children are referred to as the left child and the right child.
Types of Binary Trees:
1. Full Binary Tree: Every node has either 0 or 2 children.

2. Complete Binary Tree: All levels are fully filled except possibly the last level, which is filled from left to right.

3. Perfect Binary Tree: All internal nodes have two children, and all leaves are at the same level.

4. Balanced Binary Tree: A binary tree in which the depth of the left and right subtrees of every node differs by at most one.

5. Binary Search Tree (BST): A binary tree where for every node, the left subtree has only values less than the node, and the 
   right subtree has only values greater than the node.
"""

class BinaryTree:
    def __init__(self, height):
        self.height = height

    def process(self):
        # Process the data and display it
        self.nodes = 2**(self.height - 1)
        print(f"Number of nodes are : {self.nodes}")

class MyClass:
    def __init__(self):
        # Initialize variables
        self.height = 5
        self.another_instance = BinaryTree(self.height)

    def use_BinaryTree_class(self):
        # Call method from AnotherClass
        self.another_instance.process()

def main():
    # Create an instance of MyClass
    my_instance = MyClass()
    # Call a method that uses AnotherClass
    my_instance.use_BinaryTree_class()

if __name__ == '__main__':
    main()