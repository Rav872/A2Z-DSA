# Stock span problem


def stock_spanner(arr):

    n = len(arr)
    result = []
    stack = []
    for i in range(n): # we need to store index in the stack
        # Pop element from stack while current element is greater or equal
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        # If stack is empty, the span is entire range from current day
        if not stack:
            span = i + 1
        else:
            span = i - stack[-1]
        result.append(span)
        stack.append(i)
    return result


arr = [100,80,60,70,60,75,85]

print(stock_spanner(arr))