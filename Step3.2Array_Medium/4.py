# Kadane's algorithn

myList = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

maxEndingHere = 0
max_so_far = 0
startIndex = 0
endIndex = 0
tempStartIndex = 0

for i in range(len(myList)):
    maxEndingHere = myList[i] + maxEndingHere
    if maxEndingHere < 0:
        maxEndingHere = 0
        tempStartIndex = i + 1
    if maxEndingHere > max_so_far:
        max_so_far = maxEndingHere
        startIndex = tempStartIndex
        endIndex = i

print("Subarray for max sum is: ", myList[startIndex:endIndex+1])
print("Maximum sum Subarray is : ", max_so_far)
    
    