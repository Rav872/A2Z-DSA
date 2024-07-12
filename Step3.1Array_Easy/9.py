# Union of two sorted arrays
# Can solve using map and set too
"""my_list1 = [1,2,3,4,5]
my_list2 = [2,3,4,4,5,6]

my_list3 = []

len1 = len(my_list1)
len2 = len(my_list2)
i = 0
j = 0

for num in my_list1:
    if num in my_list3:
        continue
    else:
        my_list3.append(num)

for num in my_list2:
    if num in my_list3:
        continue
    else:
        my_list3.append(num)
"""
# best approach
my_list1 = [1,2,3,4,5]
my_list2 = [2,3,4,4,5,6]
my_list3 = []
i = 0
j = 0

while i < len(my_list1) and j < len(my_list2):
    if my_list1[i] <= my_list2[j]:
        if len(my_list3) == 0 or my_list3[-1] != my_list1[i]:
            my_list3.append(my_list1[i])
        i += 1
    else:
        if len(my_list3) == 0 or my_list3[-1] != my_list2[j]:
            my_list3.append(my_list2[j])
        j += 1

while (i < len(my_list1)):
    my_list3.append(my_list1[i])
    i += 1

while (j < len(my_list2)):
    my_list3.append(my_list2[j])
    j += 1

print("Union of two sorted array is :", my_list3)
