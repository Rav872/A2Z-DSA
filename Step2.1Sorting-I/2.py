#Bubble Sort: Compare first two elements(easiest one)
 
# Bubble sorted
 
number = []
Size = 10
print("Enter the list integers")
 
for i in range(Size):
    num = int(input())
    number.append(num)
 
for i in range(Size-1):
    for j in range(i, Size):
        if number[i] > number[j]:
            number[i], number[j] = number[j], number[i]
 
print(number)