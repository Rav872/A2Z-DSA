
"""
Description: Delete a node in binary search tree

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
    
    def delete_node(self, value):
        if self.root is None:
            return
        else:
            return self._delete_node(self.root, value)

    def is_leaf_node(self, root):
        return not (root.left or root.right)

    def is_one_child(self, root):
        return (root.left and not root.right) or (root.right and not root.left)

    def is_two_children(self, root):
        return root.left and root.right

    def get_successor(self, root):
        # Successor is the smallest node in the right subtree
        current = root.right
        while current.left:
            current = current.left
        return current

    def _delete_node(self, root, value):
        if root is None:
            return root  # Base case, node not found

        # Searching for the node to delete
        if value < root.data:
            root.left = self._delete_node(root.left, value)
        elif value > root.data:
            root.right = self._delete_node(root.right, value)
        else:  # Node found
            # Case 1: Leaf node
            if self.is_leaf_node(root):
                return None  # Delete leaf node by returning None

            # Case 2: One child
            elif self.is_one_child(root):
                return root.left if root.left else root.right  # Replace node with its child

            # Case 3: Two children
            elif self.is_two_children(root):
                # Find successor (smallest in right subtree)
                successor = self.get_successor(root)
                root.data = successor.data  # Replace root's data with successor's data
                # Delete the successor node
                root.right = self._delete_node(root.right, successor.data)

        return root  # Return the (possibly new) root of the subtree



def main():
    bst = BST()
    arr = [8, 12, 7, 2, 78, 11]
    for num in arr:
        root = bst.insert(num)
    bst.printBST(root)
    bst.delete_node(12)
    bst.delete_node(8)
    print("After deleting: ")
    bst.printBST(root)

if __name__ == '__main__':
    main()
