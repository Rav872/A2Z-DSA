# Find the number that appear once
myList = [5,3,2,1,7,8,12,12,1,2,3,7,8,5,11,11,17,18,17]

"""newList = set(myList)

for num in newList:
    if myList.count(num) == 1:
        print("Number appears that once is :", num)
        break
"""
# Another approach is can sort and find if next number is not same
myList.sort()
print("My list after soring", myList)
last = True
length = len(myList)
for i in range(0, length - 1, 2):
    print(i)
    if myList[i] != myList[i+1]:
        last = False
        print("Number appears that once is : ", myList[i])
        break

if last:
    print("Number appears that once is : ", myList[-1])
    

