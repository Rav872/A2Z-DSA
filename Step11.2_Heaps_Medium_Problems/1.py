"""
Description: Kth largest element in an array, To make it easy we can use heapq inbuild library too
"""

def insert(min_heap, num):
    min_heap.append(num)
    index = len(min_heap) - 1

    while index > 0 and min_heap[index] < min_heap[(index-1)//2]:
        min_heap[index], min_heap[(index-1)//2] = min_heap[(index-1)//2], min_heap[index]
        index = (index-1)//2

def heapify(arr, i):
    smallest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < len(arr) and arr[left_child] < arr[smallest]:
        smallest = left_child
    if right_child < len(arr) and arr[right_child] < arr[smallest]:
        smallest = right_child
    
    if i != smallest:
        arr[smallest], arr[i] = arr[i], arr[smallest]
        heapify(arr, smallest)

def delete(arr):
    if not len(arr):
        return None
    arr[0] = arr[-1]
    arr.pop()
    heapify(arr, 0)

def kthLargestElement(arr, k):
    min_heap = []
    for num in arr:
        insert(min_heap, num)
        print(min_heap)
        if len(min_heap) > k:
            delete(min_heap)
    return min_heap[0]

def main():
    arr = [7,3,1,17,5,9,11]
    print(kthLargestElement(arr, 4))
    pass

if __name__ == "__main__":
    main()