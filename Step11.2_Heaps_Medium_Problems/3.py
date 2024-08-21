"""
Description: Sort k sorted array
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

def extract_min(arr):
    if not len(arr):
        return None
    min_element= arr[0]
    arr[0] = arr[-1]
    arr.pop()
    heapify(arr, 0)
    return min_element

def merge_sorted_arrays(arr):
    min_heap = []
    sort_arr = []
    for i in range(0, len(arr[0])):
        for j in range(0, len(arr)):
            insert(min_heap, arr[i][j])
    while min_heap:
        sort_arr.append(extract_min(min_heap))
    return sort_arr

def main():
    min_heap = []
    arr = [
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9]
    ]
    print(merge_sorted_arrays(arr))

if __name__ == "__main__":
    main()