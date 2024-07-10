# Selection sort: select min and replace it with desired pos

 
# Selection sorted
 
number = []
Size = 10
print("Enter the list integers")
 
for i in range(Size):
    num = int(input())
    number.append(num)
 
for i in range(Size):
    subList = number[i:Size]
    print(subList)
    ind = number.index(min(subList))
    number[i], number[ind] = number[ind], number[i]
    
print(number)