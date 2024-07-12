# Leaders in array
# myList = [10, 22, 12, 3, 0, 6]
# brut force approach is o(n^2), checking every element to its right positions
# optimal approach
myList = [4, 7, 1, 0]
 
result = []
maxNum = 0
i = -1
for num in reversed(myList):
    if num > maxNum:
        maxNum = num
        result.insert(i, maxNum)
        i -= 1
    
print(result)