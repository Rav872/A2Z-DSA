"""
Description: K most frequent element
"""
from collections import Counter

def insert(heap, num, heapType):
    heap.append(num)
    index = len(heap) - 1

    while index > 0 and (heap[index] < heap[(index-1)//2] if heapType == "min" else heap[index] > heap[(index-1)//2]):
        heap[index], heap[(index-1)//2] = heap[(index-1)//2], heap[index]
        index = (index-1)//2

def heapify(arr, i, heapType):
    index = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < len(arr) and (arr[left_child] < arr[index] if heapType == "min" else arr[left_child] > arr[index]):
        index = left_child
    if right_child < len(arr) and (arr[right_child] < arr[index] if heapType == "min" else arr[right_child] > arr[index]):
        index = right_child
    
    if i != index:
        arr[index], arr[i] = arr[i], arr[index]
        heapify(arr, index, heapType)

def extract_root(arr, heapType):
    if not len(arr):
        return None
    element= arr[0]
    arr[0] = arr[-1]
    arr.pop()
    heapify(arr, 0, heapType)
    return element

def topKFrequent(arr, k):
    max_heap = []
    counter = Counter(arr)
    print(counter)
    result = []
    for key, value in counter.items():
        insert(max_heap, (key, value), "max")
    
    for _ in range(k):
        result.append(extract_root(max_heap, "max")[0])
    
    return result

def main():
    nums = [1,1,1,2,2,2,3,3,3,3]
    k = 2
    print(topKFrequent(nums, k))
    pass

if __name__ == "__main__":
    main()