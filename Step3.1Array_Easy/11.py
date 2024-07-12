# Maximum consecutive ones

my_list = [1,1,2,3,5,7,1,1,1,10,23,1,1,1,1,1]
max_ones = 0
ones = 0
for i in range(len(my_list)):
    if (my_list[i] == 1 and my_list[i-1] == 1) or my_list[i] == 1:
        ones += 1
        if ones > max_ones:
            max_ones = ones
    else:
        ones = 0

print("Consecutive ones are: ", max_ones)