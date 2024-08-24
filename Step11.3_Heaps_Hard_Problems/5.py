"""
Description: Medium of running stream
"""

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

def find_median(arr):
    max_heap = []
    min_heap = []

    for num in arr:
        if not max_heap or num <= max_heap[0]:
            insert(max_heap, num, "max")
        else:
            insert(min_heap, num, "min")

        if len(max_heap) > len(min_heap) + 1:
            insert(min_heap, extract_root(max_heap, "max"), "min")
        elif len(min_heap) > len(max_heap):
            insert(max_heap, extract_root(min_heap, "min"), "max")

    if len(max_heap) > len(min_heap):
        return max_heap[0]
    else:
        return (max_heap[0] + min_heap[0]) / 2


def main():
    arr = [10,23,14,67,11,78,16,89,73]
    print(find_median(arr))
    pass

if __name__ == "__main__":
    main()