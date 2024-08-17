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
Creating heap algo:
    It is inplace heap
"""

def insert(arr, N):
    i = N
    temp = arr[N]

    while i > 0 and temp > arr[i//2]:
        arr[i] = arr[i//2]
        i = i // 2
    arr[i] = temp
    print(arr)

def createHeap():
    arr = [14, 12, 1 , 19, 13, 28, 45]
    for i in range(1, len(arr)):
        insert(arr, i)


def main():
    arr = [30, 20, 15, 5, 10, 12, 6]
    element = 40
    arr.append(element)
    N = len(arr) - 1
    insert(arr, N)
    createHeap()



if __name__ == "__main__":
    main()