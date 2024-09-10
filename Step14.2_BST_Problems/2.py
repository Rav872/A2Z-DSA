
"""
Description: Floor in a binary search tree

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
    
    def get_floor(self, element):
        max_element = float('-inf')
        if self.root is None:
            return -1
        else:
            return self._get_floor(self.root, element, max_element)

    def _get_floor(self, root, element, max_element):
        if root:
            if root.data <= element:
                max_element = max(max_element, root.data)
            if element < root.data and root.left:
                return self._get_floor(root.left, element, max_element)
            if element > root.data and root.right:
                return self._get_floor(root.right, element, max_element)
        if max_element == float('-inf'):
            return -1
        else:
            return max_element


def main():
    bst = BST()
    arr = [8, 12, 7, 2, 78, 11]
    for num in arr:
        root = bst.insert(num)
    bst.printBST(root)
    print("Floor:", bst.get_floor(9))

if __name__ == '__main__':
    main()
