"""
Description: Learning Binary heaps
Heap : Complete binary tree or almost complete, 
Conditions: i) Binary heap are represented using array
            ii) Every node have element greater that or equal to its decendants, duplicates are allowed
            iii) Mean heap and max heap, height of tree will be log(n) only
            iv) Heap is not useful for searching purpose
Node at index i
Left child at 2 * i
Right child at 2 * i + 1

# Inserting in a max heap : In a heap always insert in a free space
                    30
            20              15
        5       10     12        6
Now we have to insert 40 in upper tree

arr = 30, 20, 15, 5, 10, 12, 6 .. .. .. 
So next free space is after 6, we will insert after 6
arr = 30, 20, 15, 5, 10, 12, 6 40 .. ..

Insert algo:
    call algo after inserting element at free space
    Takes log(n) time
Creating heap algo: O(nlogn)
    It is inplace heap
    call insert function for each element
Deleting from heap:O(nlogn)
    we are using max heap here so only can delete maximum element or can say highest priority element
    Approach is delete the max element and readjust it to max heap again
    Compare the children and if greater than interchange with parent
Heap sort:O(nlogn)
    i) Create heap of n elements
    ii) Delete n elements 1 by 1
"""

def insert(arr, N):
    i = N
    temp = arr[N]
    
    while i > 0 and temp > arr[(i-1)//2]:
        arr[i] = arr[(i-1)//2]
        i = (i-1) // 2
    arr[i] = temp

def createHeap(arr):
    for i in range(1, len(arr)):
        insert(arr, i)

def deleteFromHeap(arr, N):
    i = 0
    temp = arr[0]
    arr[0] = arr[N-1]  # Move the last element to the root
    N -= 1  # Reduce the heap size
    
    while True:
        left = 2*i + 1
        right = 2*i + 2
        largest = i
        
        if left < N and arr[left] > arr[largest]:
            largest = left
        if right < N and arr[right] > arr[largest]:
            largest = right
        
        if largest == i:
            break
        
        arr[i], arr[largest] = arr[largest], arr[i]
        i = largest

    arr[N] = temp

def heapSort():
    arr = [10,20,30,25,5,40,35]
    createHeap(arr)
    print("Max heap array: ", arr)

    for i in range(len(arr)-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap root with the last element
        deleteFromHeap(arr, i)  # Re-heapify the reduced heap
    
    print("Sorted array: ", arr)

def main():
    heapSort()


if __name__ == "__main__":
    main()