
"""
Description: Kth maximum in a binary search tree, for kth minimum use inorder traversal

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
    
    def kth_maximum(self, k):
        if self.root is None:
            return
        return self._kth_maximum(self.root, k).data
    
    def _kth_maximum(self, root, k):
        result = [None]
        count = [0]

        def reverse_inorder(node):
            if node.right:
                reverse_inorder(node.right)
            count[0] += 1
            result[0] = node
            if count[0] >= k:
                return
            if node.left:
                reverse_inorder(node.left)
        reverse_inorder(root)
        return result[0]

def main():
    bst = BST()
    arr = [8, 12, 7, 2, 78, 11]
    for num in arr:
        root = bst.insert(num)
    bst.printBST(root)
    bst.printBST(root)
    print("Kth maximum:", bst.kth_maximum(3))

if __name__ == '__main__':
    main()
