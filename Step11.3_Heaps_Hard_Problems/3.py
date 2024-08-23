# Description: "K largest elements"

def insert(max_heap, element):
    max_heap.append(element)
    i = len(max_heap) - 1

    while i > 0 and max_heap[i] > max_heap[(i-1)//2]:
        max_heap[i], max_heap[(i-1)//2] = max_heap[(i-1)//2], max_heap[i]
        i = (i-1)//2

def heapify(max_heap, i):
    left_child = 2*i+1
    right_child = 2*i+2

    greatest = i

    if left_child < len(max_heap) and max_heap[left_child] > max_heap[greatest]:
        greatest = left_child
    if right_child < len(max_heap) and max_heap[right_child] > max_heap[greatest]:
        greatest = right_child

    if i != greatest:
        max_heap[i], max_heap[greatest] = max_heap[greatest], max_heap[i]
        heapify(max_heap, greatest)

def extract_max(max_heap):
    if len(max_heap) == 1:
        return max_heap.pop()
    max_element = max_heap[0]
    max_heap[0] = max_heap[-1]
    max_heap.pop()
    if max_heap:
        heapify(max_heap, 0)
    return max_element

def getLargest(arr, kth):
    result = []
    max_heap = []
    for num in arr:
        insert(max_heap, num)

    for k in kth:
        temp_heap = max_heap[:]
        for _ in range(k-1):
            extract_max(temp_heap)
        result.append(extract_max(temp_heap))

    return result

def main():
    arr = [5,12,45,67,18,13,11,19]
    kth = [1,6,1,3,8]
    print(getLargest(arr, kth))
    arr.append(98)
    print(getLargest(arr, kth))
    pass

if __name__=='__main__':
    main()