"""
Description: Check if an array represent heap or not
"""

def isMaxHeap(arr, index):
    N = len(arr)
    left_child = 2 * index + 1
    right_child = 2 * index + 2

    # If the node is a leaf node, return True
    if left_child >= N:
        return True

    # Check if current node is greater than both children
    if left_child < N and arr[index] < arr[left_child]:
        return False
    if right_child < N and arr[index] < arr[right_child]:
        return False

    # Recursively check the subtrees
    return isMaxHeap(arr, left_child) and isMaxHeap(arr, right_child)

def isMinHeap(arr, index):
    N = len(arr)
    left_child = 2 * index + 1
    right_child = 2 * index + 2

    # If the node is a leaf node, return True
    if left_child >= N:
        return True

    # Check if current node is less than both children
    if left_child < N and arr[index] > arr[left_child]:
        return False
    if right_child < N and arr[index] > arr[right_child]:
        return False

    # Recursively check the subtrees
    return isMinHeap(arr, left_child) and isMinHeap(arr, right_child)

def main():
    max_heap_arr = [90, 15, 10, 7, 12, 2]
    min_heap_arr = [1, 3, 6, 5, 9, 8]
    print(isMaxHeap(max_heap_arr, 0))  # Should return True
    print(isMinHeap(min_heap_arr, 0))  # Should return True

if __name__ == "__main__":
    main()