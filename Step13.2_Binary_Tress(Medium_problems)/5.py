"""
Description: Check if two trees are identical or not
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root1, root2, nodes1, nodes2):
        self.root1 = root1
        self.nodes1 = nodes1
        self.root2 = root2
        self.nodes2 = nodes2

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
        for i in range(1, len(self.nodes1)):
            self.insert(self.root1, self.nodes1[i])
        for i in range(1, len(self.nodes2)):
            self.insert(self.root2, self.nodes2[i])

    def is_two_tree_identical(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        return (root1.value == root2.value) and self.is_two_tree_identical(root1.left, root2.left) and self.is_two_tree_identical(root1.right, root2.right)


class MyClass:
    def __init__(self):
        # Initialize variables
        self.nodes1 = [1,2,4,12,7,3,21,9]
        self.nodes2 = [1,2,4,12,7,3,21,11,9]
        self.root1 = Node(self.nodes1[0])
        self.root2 = Node(self.nodes2[0])
        self.BT = BinaryTree(self.root1, self.root2, self.nodes1, self.nodes2)

    def use_BinaryTree_class(self):
        # Call method from AnotherClass
        self.BT.process()
        print("Is two tree identical: ", self.BT.is_two_tree_identical(self.root1, self.root2), end=" ")
        print()
def main():
    # Create an instance of MyClass
    my_instance = MyClass()
    # Call a method that uses AnotherClass
    my_instance.use_BinaryTree_class()

if __name__ == '__main__':
    main()