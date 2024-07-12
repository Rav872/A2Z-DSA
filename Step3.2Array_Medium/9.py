#Longest consective subarray
myList = [100, 200, 1, 3, 2, 4]
print(myList)
 
myList.sort()
 
result = 1
maxResult = 0
 
for i in range(len(myList)-1):
    if myList[i+1]-1 == myList[i]:
        result += 1 
        maxResult = result 
    else:
        result = 1 
        
print(maxResult)