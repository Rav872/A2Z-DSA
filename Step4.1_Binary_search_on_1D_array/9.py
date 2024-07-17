# Search if item exist or not in rotate sorted array
myList = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6]
k = 10

def rotatedSearch(i, j):
    while i <= j:
        mid = (i + j) // 2
        if myList[mid] == k:
            return True
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
    return False

i = 0
j = len(myList) - 1
if rotatedSearch(i, j):
    print("Yes, Item exist")
else:
    print("No, Item doesn't exist")
