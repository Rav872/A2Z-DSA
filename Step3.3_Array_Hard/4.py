#Largest subarray with sum 0
myList = [9, -3, 3, -1, 6, -5]
preSum = {}
target = 5
maxLen = 0
summ = 0

for i in range(len(myList)):
    summ = summ + myList[i]
    if summ == 0:
        maxLen = i +1
    else:
        if summ in preSum:
            maxLen = max(maxLen, i - preSum[summ])
        else:
            preSum[summ] = i

print(maxLen)