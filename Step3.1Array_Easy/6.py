# Left rotate an array by D places
Size = 6
print("Enter the array: ")
my_list = []
while Size:
    num = int(input())
    my_list.append(num)
    Size -= 1

D = int(input("Enter number of rotation: "))
length = len(my_list)
D = D % length
print("Original array: ", my_list)

for j in range(D):
    lastNum = my_list[-1]
    for i in reversed(range(length)):
        my_list[i] = my_list[i-1]

    my_list[0] = lastNum
    print("After Rotation", j+1, " ", my_list)

print("Rotated array is: ", my_list)