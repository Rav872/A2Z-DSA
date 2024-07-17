#First and last occurrence  in array:

myList = [2,4,6,8,8,8,11,13]

k = 8
i = 0
j = len(myList)
def binarySearchFirstOcc(i, j):
    if i > j:
        return i
    mid = (i+j) // 2
    if myList[mid] == k:
        return mid
    elif myList[mid] > k:
        binarySearchFirstOcc(i, mid-1)
    else:
        binarySearchFirstOcc(mid+1, j)

def binarySearchLastOcc(i, j):
    if i > j:
        return j
    mid = (i+j) // 2    
    if k >= myList[mid]:
        return binarySearchLastOcc(mid+1, j)
    else:
        return binarySearchLastOcc(i, mid-1)

first = binarySearchFirstOcc(i, j-1)
last = binarySearchLastOcc(i, j-1)

print("first occurence: ", first, "last occurrence: ", last)