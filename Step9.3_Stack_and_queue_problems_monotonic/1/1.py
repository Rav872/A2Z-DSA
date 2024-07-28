# Next greater element using stack

def NGE(arr):
    n = len(arr)
    stack = []
    result = [-1] * n
    for i in range (2 * n-1, -1, -1):
        while stack and stack[-1] <= arr[i%n]:
            stack.pop()
        if i < n:
            if stack:
                result[i] = stack[-1]
        stack.append(arr[i%n])
    return result

arr = [3,10,4,2,1,2,6,1,7,2,9]

print(NGE(arr))



