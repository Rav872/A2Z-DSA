# Search in rotate sorted array
myList = [4,5,6,7,0,1,2,3]
k = 0

def rotatedSearch(i, j):
    while i <= j:
        mid = (i + j) // 2
        if myList[mid] == k:
            return mid
        if myList[i] <= myList[mid]:     #means left half is sorted
            if k >= myList[i] and k <= myList[mid]: # means target exist in this portion
                j = mid - 1
            else:
                i = mid + 1

        else:              # right half is sorted
            if k >= myList[mid] and k <= myList[j]:
                i = mid + 1
            else:
                j = mid - 1
    return -1

i = 0
j = len(myList) - 1
index = rotatedSearch(i, j)
if index == -1:
    print("Item not present the list")
else:
    print("Item is present at index:", index)
                                    