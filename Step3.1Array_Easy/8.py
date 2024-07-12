#Linear search

# Left rotate an array by D places
"""
num = int(input("Enter the number you want to search: "))

# 0 based indexing and first index match
isFound = False
index = 0
for i in range(length):
    if my_list[i] == num:
        isFound = True
        index = i
        break

#Binary Search: Only used on sorted array


def binarySearch(my_list, l, h, num):
    mid = l + (h-1) // 2
    if h > 0:
        if my_list[mid] ==  num:
            print("Returing index is: ", mid)
            return mid
        elif num < my_list[mid]:
            return binarySearch(my_list, l , mid-1, num)
        else:
            return binarySearch(my_list, mid+1, h, num)
    else:
        return -1

index = binarySearch(my_list, 0, length-1, num)

if index != -1:
    print("Item found at index ", index)
else:
    print("Item didn't find")
"""
def binarySearch(my_list, l, h, num):
    if h >= l:
        mid = l + (h - l) // 2
        if my_list[mid] == num:
            return mid
        elif num < my_list[mid]:
            return binarySearch(my_list, l, mid - 1, num)
        else:
            return binarySearch(my_list, mid + 1, h, num)
    else:
        return -1  # Element is not present in the list

# Example usage:
my_list = [2, 3, 4, 10, 40]
num = 90
length = len(my_list)
result = binarySearch(my_list, 0, length - 1, num)
if result != -1:
    print("Item found at index", result)
else:
    print("Item not found in the list")





        
   

