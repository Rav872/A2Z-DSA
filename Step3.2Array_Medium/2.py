my_list = [1,2,2,0,0,2,1,1,2,1,1,0,2]

# Three pointers approach i is for low index, j is for  mid and traverse
# k is for last index
i = 0
j = 0
k = len(my_list) - 1

while j <= k:
    if my_list[j] == 0:
        my_list[j], my_list[i] = my_list[i],my_list[j]
        i += 1
        j += 1
    elif my_list[j] == 1:
        j += 1
    else:
        my_list[j], my_list[k] = my_list[k],my_list[j]
        k -= 1

print(my_list)