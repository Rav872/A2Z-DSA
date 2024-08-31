class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def print_pretty(self, space=5):  # Space parameter to control spacing
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
                
                # Adjusting positions for child nodes with added space
                left_col = col - (new_width + 1 + space)
                right_col = col + (new_width + 1 + space)
                
                # Ensure that positions don't go out of bounds
                if left_col >= 0 and left_col < len(levels[row]):
                    if node.left:
                        fill_levels(node.left, row + 1, left_col, new_width, levels)
                if right_col >= 0 and right_col < len(levels[row]):
                    if node.right:
                        fill_levels(node.right, row + 1, right_col, new_width, levels)

        height = get_height(self.root)
        width = (2 ** height) - 1 + space * (2 ** (height - 2))  # Adjusted width calculation
        levels = [[" " for _ in range(width)] for _ in range(height)]
        
        fill_levels(self.root, 0, (width - 1) // 2, (width - 1) // 2, levels)
        
        for level in levels:
            print("".join(level))

# Example usage:
root = Node(16)
root.left = Node(8)
root.right = Node(24)
root.left.left = Node(6)
root.left.right = Node(10)
root.right.left = Node(22)
root.right.right = Node(28)
root.left.left.left = Node(4)
root.left.right.right = Node(12)
root.right.left.left = Node(20)
root.right.right.left = Node(26)

bt = BinaryTree(root)
bt.print_pretty(space=5)  # Increased space between child nodes

