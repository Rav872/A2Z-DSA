"""
Description: MinHeap and MaxHeap implmentation
"""

def insertKey(arr, element):
    arr.append(element)
    i = len(arr) - 1  # Start with the index of the newly added element

    # Bubble up the new element to maintain the heap property
    while i > 0 and arr[i] < arr[(i-1)//2]:
        arr[i], arr[(i-1)//2] = arr[(i-1)//2], arr[i]
        i = (i-1) // 2

def extractMin(arr):
    if len(arr) == 0:
        return None

    min_element = arr[0]
    arr[0] = arr[-1]  # Move the last element to the root
    arr.pop()  # Remove the last element

    heapify(arr, 0)  # Restore the heap property

    return min_element

def deleteKey(arr, i):
    if i >= len(arr):
        return

    # Replace the element to be deleted with the last element
    arr[i] = arr[-1]
    arr.pop()  # Remove the last element

    # Restore the heap property
    heapify(arr, i)

def heapify(arr, i):
    left = 2 * i + 1
    right = 2 * i + 2
    smallest = i

    if left < len(arr) and arr[left] < arr[smallest]:
        smallest = left
    if right < len(arr) and arr[right] < arr[smallest]:
        smallest = right
    
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, smallest)

def main():
    arr = []
    insertKey(arr, 4)
    insertKey(arr, 2)
    insertKey(arr, 5)
    insertKey(arr, 1)
    print("Heap after insertions:", arr)  # [1, 2, 5, 4]

    deleteKey(arr, 1)
    print("Heap after deletion:", arr)  # [1, 4, 5]

    min_element = extractMin(arr)
    print("Extracted Min:", min_element)  # 1
    print("Heap after extraction:", arr)  # [4, 5]

if __name__ == "__main__":
    main()