"""
Description: Check if binary tree balanced
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

class BinaryTree:
    def __init__(self, root_node, nodes):
        self.root_node = root_node
        self.nodes = nodes

    def insert(self, root_node, value):
        if root_node is None:
            return Node(value)
        else:
            if value < root_node.value:
                root_node.left_child = self.insert(root_node.left_child, value)
            else:
                root_node.right_child = self.insert(root_node.right_child, value)
        return root_node

    def process(self):
        # Process the value and display it
        for i in range(1, len(self.nodes)):
            self.insert(self.root_node, self.nodes[i])

    def height_of_a_binary_tree(self, root_node):
        if root_node is None:
            return 0
        
        left_height = self.height_of_a_binary_tree(root_node.left_child)
        right_height = self.height_of_a_binary_tree(root_node.right_child)
        return max(left_height, right_height) + 1

    def is_tree_height_balanced(self, root_node):
        if self.root_node is None:
            return True
        return self.height_of_a_binary_tree(root_node.left_child) == self.height_of_a_binary_tree(root_node.right_child)
    
class MyClass:
    def __init__(self):
        # Initialize variables
        self.nodes = [1,2,4,12,7,3,21,11,9]
        self.root_node = Node(1)
        self.BT = BinaryTree(self.root_node, self.nodes)

    def use_BinaryTree_class(self):
        # Call method from AnotherClass
        self.BT.process()
        print("Is Binary tree balanced: ", self.BT.is_tree_height_balanced(self.root_node))
def main():
    # Create an instance of MyClass
    my_instance = MyClass()
    # Call a method that uses AnotherClass
    my_instance.use_BinaryTree_class()

if __name__ == '__main__':
    main()