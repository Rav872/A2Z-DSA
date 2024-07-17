# Floor and ceil in sorted array
#The floor of x is the largest element 
#   in the array which is smaller than or equal to x.
#The ceiling of x is the smallest element 
#   in the array greater than or equal to x.

# Implement lower bound :
# The lower bound is the smallest index, ind, where arr[ind] >= x. But if any such index is not found, 
# the lower bound algorithm returns n i.e. size of the given array.
myList = [3, 4, 4, 7, 8, 10]
target = 8
'''
def binarySearch(i, j):
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

index = binarySearch(i, j)
if target in myList:
    print("floor: ", myList[index], "ceil: ", myList[index])
else:
    print("floor: ", myList[index-1], "ceil: ", myList[index])
'''
# You can use two binarySearchCeil and binarySearch floor functions separately too
def binarySearchCeil(i, j):
    if i > j:
        return i
    mid = (i + j) // 2
    if target == myList[mid]:
        return mid
    elif target < myList[mid]:
        return binarySearchCeil(i, mid-1)
    elif target > myList[mid]:
        return binarySearchCeil(mid+1, j)

def binarySearchFloor(i, j):
    if i > j:
        return i - 1
    mid = (i + j) // 2
    if target == myList[mid]:
        return mid
    elif target < myList[mid]:
        return binarySearchFloor(i, mid-1)
    elif target > myList[mid]:
        return binarySearchFloor(mid+1, j)

i = 0
j = len(myList)

ceil = binarySearchCeil(i, j-1)
print("Floor: ", myList[floor], "Ceil: ", myList[ceil])