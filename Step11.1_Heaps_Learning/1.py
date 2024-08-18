"""
Description: Implementation of priority queue using Binary Heap
"""
def insert(arr, index):
    i = index
    temp = arr[index]

    while i > 0 and temp > arr[(i-1)//2]:
        arr[i] = arr[(i-1)//2]
        i = (i-1) // 2
    arr[i] = temp

def createHeap(arr):
    for i in range(1, len(arr)):
        insert(arr, i)

def heapify_down(arr, index, heap_size):
    largest = index
    left_child = 2*index + 1
    right_child = 2*index + 2

    if left_child < heap_size and arr[left_child] > arr[largest]:
        largest = left_child
    if right_child < heap_size and arr[right_child] > arr[largest]:
        largest = right_child
    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]
        heapify_down(arr, largest, heap_size)

def deleteHeap(arr):
    heap_size = len(arr)
    if not heap_size:
        return None
    arr[0], arr[heap_size-1] = arr[heap_size-1], arr[0]

    # remove the last element:
    arr.pop()
    heapify_down(arr, 0, len(arr))

def main():
    arr = [4,2,8,16,24,6,5]
    # Convert array to max heap and delete first maximum which is always root
    # Without max heap insertion is O(n) but deletion is find item first and then delete which takes O(nlogn)
    # After creating to max heap we know it will max take O(logn) to delete max item which is root
    createHeap(arr)
    print("Max heap: ", arr)
    deleteHeap(arr)
    deleteHeap(arr)
    print("Max heap after deleting element: ", arr)
    pass

if __name__ == "__main__":
    main()