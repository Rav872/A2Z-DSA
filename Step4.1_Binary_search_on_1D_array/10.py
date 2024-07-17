#Find the minimum element in rotated sorted array

# Search if item exist or not in rotate sorted array
myList = [4,5,6,7,0,1,2,3]
def rotatedSearch(i, j):
    minElement = 999999
    while i <= j:
        mid = (i + j) // 2
        if myList[i] <= myList[j]:
            minElement = min(minElement, myList[i])
        if myList[i] <= myList[mid]:     #means left half is sorted
            minElement = min(minElement, myList[i])
            i = mid + 1
        else:              # right half is sorted
            minElement = min(minElement, myList[mid])
            j = mid - 1
    return minElement
i = 0
j = len(myList) - 1

print("Min element is : ", rotatedSearch(i, j))