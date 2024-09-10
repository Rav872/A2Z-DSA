
"""
Description: Ceil in a binary search tree

"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def printBST(self, root):
        if root is None:
            return
        print(root.data, end=": ")
        if root.left:
            print("L:", root.left.data, end=" ")
        if root.right:
            print("R:", root.right.data, end=" ")
        print()
        self.printBST(root.left)
        self.printBST(root.right)

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.root = self._insert(self.root, value)
        return self.root

    def _insert(self, root, value):
        if value < root.data:
            if root.left:
                root.left = self._insert(root.left, value)
            else:
                root.left = Node(value)
        else:
            if root.right:
                root.right = self._insert(root.right, value)
            else:
                root.right = Node(value)
        return root
    def get_ceil(self, element):
        min_element = float('inf')
        if self.root is None:
            return -1
        else:
            return self._get_ceil(self.root, element, min_element)

    def _get_ceil(self, root, element, min_element):
        if root:
            if root.data >= element:
                min_element = min(min_element, root.data)
            if element < root.data and root.left:
                return self._get_ceil(root.left, element, min_element)
            if element > root.data and root.right:
                return self._get_ceil(root.right, element, min_element)
        if min_element == float('inf'):
            return -1
        else:
            return min_element

def main():
    bst = BST()
    arr = [8, 12, 7, 2, 78, 11]
    for num in arr:
        root = bst.insert(num)
    bst.printBST(root)
    print(bst.get_ceil(9))

if __name__ == '__main__':
    main()
