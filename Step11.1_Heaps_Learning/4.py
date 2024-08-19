"""
Description: Convert min Heap to Max heap
"""
def insert(arr, index):
    i = index
    temp = arr[index]

    while i > 0 and temp > arr[(i-1)//2]:
        arr[i] = arr[(i-1)//2]
        i = (i-1) // 2
    arr[i] = temp

def convert_mean_heap_to_max_heap(arr):
    for i in range(0, len(arr)):
        insert(arr, i)

def main():
    # arr = [1, 2, 3, 4]
    arr = [3,4,8,11,13]
    convert_mean_heap_to_max_heap(arr)
    print(arr)
    pass

if __name__ == "__main__":
    main()