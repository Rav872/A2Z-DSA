"""
Description: Kth smallest element in an array, we need max heap, To make it easy we can use heapq inbuild library too
"""

def insert(arr, element):
    arr.append(element)
    i = len(arr) - 1

    while i > 0 and arr[i] > arr[(i-1)//2]:
        arr[i], arr[(i-1)//2] = arr[(i-1)//2], arr[i]
        i = (i-1) // 2

def heapify(arr, i):
    greatest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < len(arr) and arr[left_child] > arr[greatest]:
        greatest = left_child
    if right_child < len(arr) and arr[right_child] > arr[greatest]:
        greatest = right_child
    
    if i != greatest:
        arr[greatest], arr[i] = arr[i], arr[greatest]
        heapify(arr, greatest)

def delete(arr):
    if not len(arr):
        return None
    arr[0] = arr[-1]
    arr.pop()
    heapify(arr, 0)

def kthSmallestElement(arr, k):
    max_heap = []
    for num in arr:
        insert(max_heap, num)
        if len(max_heap) > k:
            delete(max_heap)
        print(max_heap)
    return max_heap[0]

def main():
    arr = [7,3,1,17,5,9,11]
    print(kthSmallestElement(arr, 5))
    pass

if __name__ == "__main__":
    main()