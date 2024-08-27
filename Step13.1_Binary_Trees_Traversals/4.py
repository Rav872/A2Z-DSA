"""
Description: Binary tree traversal(Inorder, preorder, postorder, levelorder)
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

    def insert(self, root, value):
        if root is None:
            return Node(value)
        else:
            if value < root.value:
                root.left_child = self.insert(root.left_child, value)
            else:
                root.right_child = self.insert(root.right_child, value)
        return root

    def process(self):
        # Process the value and display it
        for i in range(1, len(self.nodes)):
            self.insert(self.root_node, self.nodes[i])
    
    def printBT(self, root_node):
        if root_node == None:
            return
        print(root_node.value, end=": ")
        if root_node.left_child:
            print("L", root_node.left_child.value, end=" ")
        if root_node.right_child:
            print("R", root_node.right_child.value, end=" ")
        print()
        self.printBT(root_node.left_child)
        self.printBT(root_node.right_child)

    def in_order_traversal(self, node):  # left_child -> root -> right_child
        if node:
            self.in_order_traversal(node.left_child)
            print(node.value, end=" ")
            self.in_order_traversal(node.right_child)

    def pre_order_traversal(self, node):          # Time complexity : O(n) , Root, left_child subtree, right_child subtree
        if node:
            print(node.value, end=" ")
            self.pre_order_traversal(node.left_child)
            self.pre_order_traversal(node.right_child)

    def post_order_traversal(self, node):    # left_child -> right_child -> root
        if node:
            self.post_order_traversal(node.left_child)
            self.post_order_traversal(node.right_child)
            print(node.value, end=" ")

    def level_order_traversal(self):
        if self.root_node is None:
            return
        queue = []
        queue.append(self.root_node)

        while queue:
            curr = queue.pop(0)
            print(curr.value, end=" ")

            if curr.left_child:
                queue.append(curr.left_child)
            if curr.right_child:
                queue.append(curr.right_child)

class MyClass:
    def __init__(self):
        # Initialize variables
        self.nodes = [1,2,4,12,7,3,21,11,9]
        self.root_node = Node(1)
        self.BT = BinaryTree(self.root_node, self.nodes)

    def use_BinaryTree_class(self):
        # Call method from AnotherClass
        self.BT.process()
        print("Printing Tree: ")
        self.BT.printBT(self.root_node)
        print("In order traversal:", end=" ")
        self.BT.in_order_traversal(self.root_node)
        print()
        print("Preorder traversal:", end=" ")
        self.BT.pre_order_traversal(self.root_node)
        print()
        print("Post order traversal:", end=" ")
        self.BT.post_order_traversal(self.root_node)
        print()
        print("Level order traversal:", end=" ")
        self.BT.level_order_traversal()
        print()
def main():
    # Create an instance of MyClass
    my_instance = MyClass()
    # Call a method that uses AnotherClass
    my_instance.use_BinaryTree_class()

if __name__ == '__main__':
    main()