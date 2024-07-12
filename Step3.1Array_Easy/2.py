# Second largest element in an array
Size = 6
print("Enter the array: ")
my_list = []
while Size:
    num = int(input())
    my_list.append(num)
    Size -= 1

"""my_list.sort()
max_element = my_list[-1]

for num in reversed(my_list):
    if num < max_element:
        second_max = num
        break

print("Second max element is : ", second_max)
"""
#Second approach without sorting
max_element = -999999

for num in my_list:
    if num > max_element:
        max_element = num

min_distance = 99999999

for num in my_list:
    distance = max_element - num
    if (distance < min_distance and distance != 0):
        min_distance = distance

print("Second largest element is : ", max_element - min_distance)



