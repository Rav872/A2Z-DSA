# Sum of subarray minimums
# This approach takes O(n^2)
def sum_of_subarray_minimums(arr):
    total_sum = 0
    n = len(arr)

    for i in range(n):
        current_min = arr[i]
        for j in range(i, n):
            current_min = min(current_min, arr[j])
            total_sum += current_min
    return total_sum

arr = [3,1,2,4]

print(sum_of_subarray_minimums(arr))

# There is another approach using stack which needs to find previous less of an index and next les of an index
# then leftcount will be index - prevLess and right count will nexLess - index
# total sum will be sum += arr[index] *leftcount * right_count