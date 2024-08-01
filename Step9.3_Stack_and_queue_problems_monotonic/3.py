# Next smaller element using stack

def NSE(arr):
    stack = []
    result = []

    for item in arr:
        if not stack:
            result.append(-1)
        else:
            while stack and stack[-1] >= item:
                stack.pop()
            if stack:
                result.append(stack[-1])
            else:
                result.append(-1)
        stack.append(item)
    return result

arr = [3,10,4,2,1,2,6,1,7,2,9]

print(NSE(arr))