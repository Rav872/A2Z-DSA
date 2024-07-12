# Left rotate an array by one place
Size = 6
print("Enter the array: ")
my_list = []
while Size:
    num = int(input())
    my_list.append(num)
    Size -= 1

length = len(my_list)
print("Original array: ", my_list)

lastNum = my_list[-1]
for i in reversed(range(length)):
    my_list[i] = my_list[i-1]

my_list[0] = lastNum

print("Rotated array is: ", my_list)

