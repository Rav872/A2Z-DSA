myList = [3,1,2,5,3]
maxNum = max(myList)
myList = set(myList)
totalSum = 0

summ = (maxNum * (maxNum+1)) // 2
for num in myList:
    totalSum += num

print("Missing number: ", summ - totalSum)

# Using XOR operation we will find out repeating number
