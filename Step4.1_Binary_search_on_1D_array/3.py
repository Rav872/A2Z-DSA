#The upper bound algorithm finds the first or the smallest index in a sorted 
#array where the value at that index is greater than the given key

myList = [3, 4, 6, 7, 9, 12, 16, 17]
target = 8
def binarySearch(i, j):
    if (i > j):
        return len(myList) # Upper bound: return len if not found item
    mid = (i + j) // 2
    if target == myList[mid]:
        return mid + 1
    elif target < myList[mid]:
        return binarySearch(i, mid-1)
    elif target > myList[mid]:
        return binarySearch(mid+1, j)


i = 0
j = len(myList)

index = binarySearch(i, j-1)
print("Upper bound of target is: ", index)