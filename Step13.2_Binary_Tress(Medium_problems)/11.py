"""
Description: Right/Left view of binary tree
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
    
    def print_pretty(self):
        if not self.root:
            print("Empty tree")
            return
        
        def get_height(node):
            if not node:
                return 0
            return max(get_height(node.left), get_height(node.right)) + 1

        def fill_levels(node, row, col, width, levels):
            if node:
                levels[row][col] = str(node.value)
                new_width = (width - 1) // 2
                if node.left:
                    fill_levels(node.left, row + 1, col - new_width - 1, new_width, levels)
                if node.right:
                    fill_levels(node.right, row + 1, col + new_width + 1, new_width, levels)

        height = get_height(self.root)
        width = (2 ** height) - 1  # The total width required for the bottom level
        levels = [[" " for _ in range(width)] for _ in range(height)]
        
        fill_levels(self.root, 0, (width - 1) // 2, (width - 1) // 2, levels)
        
        for level in levels:
            print("".join(level))

    def right_view(self):
        self._right_view(self.root)
    def _right_view(self, root):
        if root is None:
            return
        queue = []
        queue.append(root)

        while queue:
            level = len(queue)
            level_nodes = []
            for _ in range(level):
                node = queue.pop(0)
                level_nodes.append(node.value)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print(level_nodes[-1], end=" ")

class MyClass:
    def __init__(self):
        # Initialize variables
        self.nodes = [1,2,4,12,7,3,21,11,9]
        self.BT = BinaryTree(self.nodes)

    def use_BinaryTree_class(self):
        # Call method from BinaryTree class
        self.BT.process()
        self.BT.printBT()
        self.BT.print_pretty()
        print("Right view of binary tree: ")
        self.BT.right_view()
        print()


def main():
    # Create an instance of MyClass
    my_instance = MyClass()
    # Call a method that uses AnotherClass
    my_instance.use_BinaryTree_class()

if __name__ == '__main__':
    main()