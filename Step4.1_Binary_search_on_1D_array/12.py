#Search single element in a sorted array:

myList = [1,1,2,2,3,3,4,5,5,6,6]
    
i = 0
j = len(myList)-1

# Use iterative method
print("Only number appear once is: ", binarySearchSingleElement(i, j))