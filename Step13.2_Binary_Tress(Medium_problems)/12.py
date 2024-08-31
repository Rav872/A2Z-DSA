"""
Description: Is tree symmetric
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, nodes):
        self.nodes = nodes
        self.root = None

    def insert(self, arr, root, i):
        n = len(arr)
        if i < n:
            temp = Node(arr[i])
            root = temp

            root.left = self.insert(arr, root.left, 2 * i + 1)
            root.right = self.insert(arr, root.right, 2 * i + 2)
        return root

    def process(self):
        if self.nodes:
            self.root = self.insert(self.nodes, self.root, 0)

    def printBT(self):
        self._printBT(self.root)

    def _printBT(self, root):
        if root is None:
            return
        print(root.value, end=": ")
        if root.left:
            print("L", root.left.value, end=" ")
        if root.right:
            print("R", root.right.value, end=" ")
        print()
        self._printBT(root.left)  
        self._printBT(root.right)

    def is_symmetric(self):
        return self._is_mirror(self.root.left, self.root.right)

    def _is_mirror(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        return (left.value == right.value) and self._is_mirror(left.left, right.right) and self._is_mirror(left.right, right.left)

class MyClass:
    def __init__(self):
        # Initialize variables
        self.nodes = [16, 8, 24, 6, 10, 22, 28, 4, 12, 20, 26]
        self.BT = BinaryTree(self.nodes)

    def use_BinaryTree_class(self):
        # Call method from BinaryTree class
        self.BT.process()
        self.BT.printBT()
        print("Is binary tree symmetric:", self.BT.is_symmetric())
        print()


def main():
    # Create an instance of MyClass
    my_instance = MyClass()
    # Call a method that uses AnotherClass
    my_instance.use_BinaryTree_class()

if __name__ == '__main__':
    main()