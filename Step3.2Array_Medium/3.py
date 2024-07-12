# Majority elements greater than n/2
myList = [2,2,1,1,1,2,2]
#myList = [4,4,2,4,3,4,4,3,2]

N = len(myList)

newList = set(myList)

for num in newList:
    if myList.count(num) > N // 2:
        print("Number is : ", num)
        break


