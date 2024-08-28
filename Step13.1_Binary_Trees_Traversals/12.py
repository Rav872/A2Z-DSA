"""
Description: Postorder traversal using 1 stack
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

    def postorder_traversal(self):
        if self.root_node is None:
            return
        stack = []
        result = []
        last_visited = None
        current = self.root_node
    
        while stack or current:
            if current:
                stack.append(current)
                current = current.left_child
            else:
                peek_node = stack[-1]
                # If right_child child exists and hasn't been visited, process right_child child
                if peek_node.right_child and last_visited != peek_node.right_child:
                    current = peek_node.right_child
                else:
                    # If no unvisited right_child child, visit the node
                    print(peek_node.value, end=" ")
                    last_visited = stack.pop()

class MyClass:
    def __init__(self):
        # Initialize variables
        self.nodes = [1,2,4,12,7,3,21,11,9]
        self.root_node = Node(1)
        self.BT = BinaryTree(self.root_node, self.nodes)

    def use_BinaryTree_class(self):
        # Call method from AnotherClass
        self.BT.process()
        print("Post order traversal:", end=" ")
        self.BT.postorder_traversal()
        print()
def main():
    # Create an instance of MyClass
    my_instance = MyClass()
    # Call a method that uses AnotherClass
    my_instance.use_BinaryTree_class()

if __name__ == '__main__':
    main()