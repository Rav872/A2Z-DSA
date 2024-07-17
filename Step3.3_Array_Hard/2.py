# Majority element N/3

myList = [1,2,2,3,2]

newList = set(myList)

result = 0
for ele in newList:
    if myList.count(ele) > len(myList) // 3:
        result = ele
        break

print("Majority element is : ", result)