# Moves zeroes to end
Size = 8
print("Enter the array: ")
my_list = []
while Size:
    num = int(input())
    my_list.append(num)
    Size -= 1

lenght = len(my_list)
print("Original array is : ", my_list)
i = 0
while (i < lenght):
    if my_list[i] == 0:
        my_list.remove(my_list[i])
        my_list.append(0)
    i += 1

print("New list: ", my_list)

# Less Optimal approach is using 2 pointers approach