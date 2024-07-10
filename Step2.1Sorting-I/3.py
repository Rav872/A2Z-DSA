# Selection Sort
number = []
Size = 10
print("Enter the list integers")

for i in range(Size):
    num = int(input())
    number.append(num)
    
 
for i in range(Size):
    j = i
    while j > 0 and number[j-1] > number[j]:
        number[j], number[j-1] = number[j-1], number[j]
        j -= 1
        
print(number)