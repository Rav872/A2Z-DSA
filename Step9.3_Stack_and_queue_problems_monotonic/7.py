# Asteroid collision

def is_empty(arr):
    return len(arr) == 0

def is_all_elements_positive(arr):
    for ele in arr:
        if ele < 0:
            return False
    return True

def is_all_elements_negative(arr):
    for ele in arr:
        if ele > 0:
            return False
    return True

def astroid_collision(arr):

    while not (is_all_elements_positive(arr) or is_all_elements_negative(arr) or is_empty(arr)):
        n = len(arr)
        i = 0
        while i < n-1:
            j = i + 1
            first_val = arr[i]
            second_val = arr[j]
            if arr[j] < 0:
                if abs(arr[i]) < abs(arr[j]):
                    arr.remove(first_val)
                elif abs(arr[i]) > abs(arr[j]):
                    val = arr[j]
                    arr.remove(second_val)
                else:
                    arr.remove(first_val)
                    arr.remove(second_val)
            i += 1
            n = len(arr)

    return arr
ast = [5,10,-5]

print(astroid_collision(ast))