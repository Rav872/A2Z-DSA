
"""
Description: Check if a tree is BST

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
    
    def LCA(self, value1, value2):
        if self.root is None:
            return
        return self._LCA(self.root, value1, value2)
    
    def _LCA(self, root, value1, value2):
        if root is None:
            return None

        if value1 < root.data and value2 < root.data:
            return self._LCA(root.left, value1, value2)

        if value1 > root.data and value2 > root.data:
            return self._LCA(root.right, value1, value2)
        
        return root

    
def main():
    bst = BST()
    arr = [8, 12, 7, 2, 78, 11]
    for num in arr:
        root = bst.insert(num)
    bst.printBST(root)
    bst.printBST(root)
    print("LCA: ", bst.LCA(2,7).data)

if __name__ == '__main__':
    main()