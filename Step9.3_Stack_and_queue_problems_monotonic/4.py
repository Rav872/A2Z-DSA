# Number of next greater element using stack in normal array

def count_greater_elements_for_indexes(arr, indexes):
    stack = []
    result = [0] * len(arr)

    for i in range(len(arr) - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        count = len(stack)  # Count of elements greater than current element
        result[i] = count
        stack.append(arr[i])

    return [result[i] for i in indexes]

arr = [3, 10, 4, 2, 1, 2, 6, 1, 7, 2, 9]
indexes = [3, 6]

print(count_greater_elements_for_indexes(arr, indexes))