# Implement binary search using iterative method and recursion
myList = [3, 4, 6, 7, 9, 12, 16, 17]
target = 6

def binarySearch(i, j):
    mid = (i + j) // 2
    if target == myList[mid]:
        return mid
    elif target < myList[mid]:
        return binarySearch(i, mid-1)
    else:
        return binarySearch(mid+1, j)

i = 0
j = len(myList)

index = binarySearch(i, j)
#Iterative method first
'''
while i < j:
    mid = (i + j) // 2
    if target == myList[mid]:
        index = mid
        break
    elif target < myList[mid]:
        j = mid - 1
    else:
        i = mid + 1
'''
#Recursive method:

print("Index of target is: ", index)