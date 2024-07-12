# Next permutation

# First find the break point : break point is element where element is
# less than next element on right side
# Find the next smallest greater element right to that break point and swap
# Sort right side of array from breakpoint

#myList = [2,1,5,4,3,0,0]

breakPoint = 0

for i in range(len(myList)-2, -1, -1):
    if myList[i] < myList[i+1]:
        for j in range(len(myList)-1, i, -1):
            if myList[j] > myList[i]:
                myList[j], myList[i] = myList[i], myList[j]
                break
        myList[i+1:] = sorted(myList[i+1:])
        break

print(myList)
        
        