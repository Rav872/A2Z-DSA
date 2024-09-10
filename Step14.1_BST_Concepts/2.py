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

    def binary_search(self, element):
        if self.root is None:
            return False
        else:
            return self._binary_search(self.root, element)

    def _binary_search(self, root, element):
        if element == root.data:
            return True
        elif element < root.data:
            return self._binary_search(root.left, element)
        else:
            return self._binary_search(root.right, element)


def main():
    bst = BST()
    arr = [8, 12, 7, 2, 78, 11]
    for num in arr:
        root = bst.insert(num)
    bst.printBST(root)
    print(bst.binary_search(7))
    print(bst.binary_search(75))

if __name__ == '__main__':
    main()
