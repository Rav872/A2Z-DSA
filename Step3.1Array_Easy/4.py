# Remove duplicate items from sorted array
Size = 6
print("Enter the array: ")
my_list = []
while Size:
    num = int(input())
    my_list.append(num)
    Size -= 1

length = len(my_list)
i = 1
while (i < length-1):
    my_list[i] == my_list[i-1]
    my_list.remove(my_list[i-1])
    length -= 1
    i += 1
    
print("Unique list is: ", my_list)