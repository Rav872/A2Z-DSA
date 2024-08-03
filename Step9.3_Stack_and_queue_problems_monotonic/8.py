# Sum of subarrays ranges

def sum_of_subarrays_ranges(arr):
    total_sum = 0
    n = len(arr)
    for i in range(n):
        sub_arr = []
        for j in range(i, n):
            sub_arr.append(arr[j])
            if len(sub_arr) > 1:
                total_sum += (max(sub_arr)-min(sub_arr))
    return total_sum

arr = [4,-2,-3,4,1]
print(sum_of_subarrays_ranges(arr))


