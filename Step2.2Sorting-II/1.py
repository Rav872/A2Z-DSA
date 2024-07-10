#Merge sort algorithm

def merge(my_list, leftArr, rightArr):
    i = 0
    j = 0
    k = 0
    while i < len(leftArr) and j < len(rightArr):
        if leftArr[i] < rightArr[j]:
            my_list[k] = leftArr[i]
            i += 1
            k += 1
        else:
            my_list[k] = rightArr[j]
            j += 1
            k += 1
    while i < len(leftArr):
        my_list[k] = leftArr[i]
        i += 1
        k += 1
    while j < len(rightArr):
        my_list[k] = rightArr[j]
        j += 1
        k += 1

def mergeSort(my_list):
    Size = len(my_list)
    if Size > 1:
        mid = Size // 2
        leftArr = my_list[:mid]
        rightArr = my_list[mid:]
        #first iterative call
        mergeSort(leftArr)
        #second iterative call
        mergeSort(rightArr)
        merge(my_list, leftArr, rightArr)

Size = 6
print("Enter the array: ")
my_list = []
while Size:
    num = int(input())
    my_list.append(num)
    Size -= 1 

mergeSort(my_list)
print(my_list)
