# Sliding window maximum
from collections import deque
# Brute force creating each sub_array and checking maximum out of that
# def max_sliding_window(arr, k):
#     n = len(arr)
#     result = []
#     for i in range(n-(k-1)):
#         result.append(max(arr[i:i+k]))
#     return result

# Second approach with the help of deque keeps checking whether the incoming element is larger that the already
# present elements

def max_sliding_window(arr, k):
    if not arr:
        return []
    result = []
    dq = deque()     #appendleft, appendright, popleft, popright
    n = len(arr)
    for i in range(n):
        # Storing indices in dq, so checking the if first element is in window
        if dq and dq[0] < i - k + 1:
            dq.popleft()
        # Remove elements smaller than the current element
        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()
        # Add current element index
        dq.append(i)

        # Add the maximum for current window
        if i >= k - 1:
            result.append(arr[dq[0]])
    return result

arr = [4,0,-1,3,5,3,6,8]
k = 3
print(max_sliding_window(arr, k))