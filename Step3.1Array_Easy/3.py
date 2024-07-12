# Check if array is sorted

Size = 6
print("Enter the array: ")
my_list = []
while Size:
    num = int(input())
    my_list.append(num)
    Size -= 1

isSorted = True
for i in range(1, len(my_list)):
    if my_list[i] < my_list[i-1]:
        isSorted = False
        break

if isSorted:
    print("Array is sorted!")
else:
    print("Array is not sorted!")