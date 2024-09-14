
"""
Description: Inorder Successor/Predecessor

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

    def inorder_successor(self): # smallest node in the right subtree
        if self.root is None:
            return
        return self._inorder_sucessor(self.root)

    def _inorder_sucessor(self, root):
        current = root.right
        while current.left:
            current = current.left
        return current.data

    def inorder_predecessor(self):  # greatest node in left subtree
        if self.root is None:
            return
        return self._inorder_predecessor(self.root)

    def _inorder_predecessor(self, root):

        current = root.left
        while current.right:
            current = current.right
        return current.data
    
def main():
    bst = BST()
    arr = [8,5,1,7,10,12]
    for num in arr:
        root = bst.insert(num)
    bst.printBST(root)
    print("Inorder successor: ", bst.inorder_successor())
    print("Inorder predecessor: ", bst.inorder_predecessor())

if __name__ == '__main__':
    main()