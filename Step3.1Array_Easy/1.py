# Find largest element in array
Size = 6
print("Enter the array: ")
my_list = []
while Size:
    num = int(input())
    my_list.append(num)
    Size -= 1

max_num = -99999999
for num in my_list:
    if num > max_num:
        max_num = num

print("Maximumum number in the list: ", max_num)

# 2nd approach Sort and return last element
