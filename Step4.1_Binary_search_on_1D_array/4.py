# search insert position
myList = [3, 4, 6, 7, 9, 12, 16, 17]
target = 2
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

maxElement = max(myList)

if target >= maxElement:
    index = len(myList)
else:
    index = binarySearch(i, j-1)
print("Insert position for target is : ", index)