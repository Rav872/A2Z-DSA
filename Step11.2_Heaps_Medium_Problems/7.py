"""
Description: Hands of straight
"""

from collections import Counter

def insert(min_heap, element):
    min_heap.append(element)
    i = len(min_heap) - 1

    while i > 0 and min_heap[i] < min_heap[(i-1)//2]:
        min_heap[(i-1)//2], min_heap[i] = min_heap[i], min_heap[(i-1)//2]
        i = (i-1)//2

def heapify(min_heap, i):
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    smallest = i
    if left_child < len(min_heap) and min_heap[left_child] < min_heap[smallest]:
        smallest = left_child
    if right_child < len(min_heap) and min_heap[right_child] < min_heap[smallest]:
        smallest = right_child

    if i != smallest:
        min_heap[i], min_heap[smallest] = min_heap[smallest], min_heap[i]
        heapify(min_heap, smallest)

def delete(min_heap):
    min_heap[0] = min_heap[-1]
    min_heap.pop()
    heapify(min_heap, 0)

def straight_hands(arr, n):

    if len(arr) % n != 0:
        return False

    counter = Counter(arr)
    min_heap = []
    for num in counter.keys():
        insert(min_heap, num)

    print(min_heap)

    while min_heap:
        first = min_heap[0] # Get minimum count of any key

        for i in range(n): # We will make group here, e.g In first iteration group will be 1,2,3, now one 2 and one 3 left,
        # In next iteration one 2 one 3 and 4 will be grouping then got deleted from min_heap and then grouping will be 5,6,7
            if counter[first + i] > 0:
                counter[first + i] -= 1
                if counter[first + i] == 0:
                    delete(min_heap)
            else:
                return False
    return True

def main():
    hand = [1,2,3,4,5,6,7,2,3]
    n = 3
    print(straight_hands(hand, n))

    pass

if __name__=='__main__':
    main()