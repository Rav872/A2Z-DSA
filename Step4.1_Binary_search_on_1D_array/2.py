# Implement lower bound :
# The lower bound is the smallest index, ind, where arr[ind] >= x. But if any such index is not found, 
# the lower bound algorithm returns n i.e. size of the given array.
myList = [3, 4, 6, 7, 7, 7, 9, 12, 16, 17]
target = 8
def binarySearch(i, j):
    print("Value of i and j: ", i , " ", j)
    if i > j:
        return i
    mid = (i + j) // 2
    if target == myList[mid]:
        return mid
    elif target < myList[mid]:
        return binarySearch(i, mid-1)
    elif target > myList[mid]:
        return binarySearch(mid+1, j)


i = 0
j = len(myList)

index = binarySearch(i, j-1)
print("Lower bound of target is: ", index)