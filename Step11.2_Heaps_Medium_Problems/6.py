"""
Description: Task scheduler
"""

from collections import Counter, deque

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
    max_element = max_heap[0]
    max_heap[0] = max_heap[-1]
    max_heap.pop()

    heapify(max_heap, 0)
    return max_element

def minInterval(arr, n):
    max_heap = []
    counter = Counter(arr)
    for num in counter.values():
        insert(max_heap, num)

    cool_down_queue = deque()

    time = 0

    while max_heap or cool_down_queue:
        time += 1

        if max_heap:
            current_task = extract_max(max_heap)

            if current_task - 1 > 0:
                cool_down_queue.append((current_task - 1, time + n))
        if cool_down_queue and cool_down_queue[0][1] == time:
            insert(max_heap, cool_down_queue.popleft()[0])
    return time

def main():
    arr = ['A','A','A','B','B','B']
    n = 2
    print(minInterval(arr, n))
    pass

if __name__=='__main__':
    main()