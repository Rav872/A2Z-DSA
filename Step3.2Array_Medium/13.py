myList = [3,1,2,4]

Sum = 6
count = 0
totalSum = 0
for i in range(len(myList)):
    totalSum = totalSum + myList[i]
    if totalSum < 0:
        totalSum = 0
    if totalSum == Sum:
        count += 1

print("Number of subarrays are: ", count)