
"""
Description: Two sum in BST

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
        if root.left or root.right:
            print(root.data, end=": ")
        if root.left and root.right:
            print(f"L: {root.left.data} R: {root.right.data}")
        elif root.left or root.right:
            print(f"L: {root.left.data}", end=" ") if root.left else print("L: null", end=" ")
            print(f"R: {root.right.data}") if root.right else print("R: null")
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
    
    def find_node(self, root, val):
        # Base case
        if root is None:
            return False
        # Found the node
        if val == root.data:
            return True
        # Use BST property to search more efficiently
        if val < root.data:
            return self.find_node(root.left, val)
        else:
            return self.find_node(root.right, val)

    def two_sum(self, k):
        if self.root is None:
            return False
        return self._two_sum(self.root, k)

    def _two_sum(self, root, k):
        # Base case: if the node is None
        if root is None:
            return False

        # Check if there exists a node such that node.data + root.data == k
        complement = k - root.data
        if complement != root.data and self.find_node(self.root, complement):
            return True

        # Recursively check the left and right subtrees
        return self._two_sum(root.left, k) or self._two_sum(root.right, k)


def main():
    bst = BST()
    arr = [8,5,2,1,7,10,12]
    for num in arr:
        root = bst.insert(num)
    bst.printBST(root)
    print(bst.two_sum(12))

if __name__ == '__main__':
    main()