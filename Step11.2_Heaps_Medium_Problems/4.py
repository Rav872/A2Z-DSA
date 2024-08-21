"""
Description: Replace each array element by its corresponding rank
"""

def insert(min_heap, element):
    min_heap.append(element)
    i = len(min_heap) - 1

    while i > 0 and min_heap[i] < min_heap[(i-1)//2]:
        min_heap[i], min_heap[(i-1)//2] = min_heap[(i-1)//2], min_heap[i]
        i = (i-1)//2

def extract_min(min_heap):
    minimum_element = min_heap[0]
    min_heap[0] = min_heap[-1]
    min_heap.pop()
    heapify(min_heap, 0)
    return minimum_element

def heapify(min_heap, i):
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    smallest = i
    
    if left_child < len(min_heap) and min_heap[left_child] < min_heap[smallest]:
        smallest = left_child
        if right_child < len(min_heap) and min_heap[right_child] < min_heap[smallest]:
            smallest = right_child
            
        if i != smallest:
            min_heap[smallest], min_heap[i] = min_heap[i], min_heap[smallest]
            heapify(min_heap, smallest)

def rank(arr):
    min_heap = []
    rank_dict = {}
    res = []
    for num in arr:
        insert(min_heap, num)
        
    for i in range(1,len(min_heap)+1):
        rank_dict[extract_min(min_heap)] = i
    for num in arr:
        res.append(rank_dict.get(num))

    return res

def main():
    arr = [34,5,56,1,67,7,2,11]
    print(rank(arr))
    pass

if __name__=='__main__':
    main()