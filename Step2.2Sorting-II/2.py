# Quick sort
def partition(my_list, low, high):
    pivot = my_list[low]
    i = low + 1
    j = high

    while True:
        while i <= j and my_list[i] <= pivot:
            i += 1
        while my_list[j] >= pivot and j >= i:
            j -= 1
        if j < i:
            break
        my_list[i], my_list[j] = my_list[j], my_list[i]

    my_list[low], my_list[j] = my_list[j], my_list[low]
    return j


def quickSort(my_list, low, high):
    if low < high:
        part = partition(my_list, low, high)
        quickSort(my_list, low, part - 1)
        quickSort(my_list, part + 1, high)


Size = 6
print("Enter the array: ")
my_list = []
for _ in range(Size):
    num = int(input())
    my_list.append(num)

l = 0
h = len(my_list) - 1

print("Original list:", my_list)
quickSort(my_list, l, h)
print("Sorted list:", my_list)
