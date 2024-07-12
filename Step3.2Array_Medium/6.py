# Rearrange positive and negative elements alternative

elements = [1,2,-4,-5]
#elements = [1,2,-3,-1,-2, 3]


index = 0
i = 0
j = 1

while (index < len(elements)):
    if index % 2 == 1 and elements[index] < 0:
        elements[i], elements[j] = elements[j], elements[i]
        if j < len(elements) - 1:
            j += 2
    elif index % 2 == 0 and elements[index] > 0:
        elements[i], elements[j] = elements[j], elements[i]
        if i < len(elements) - 2:
            i += 2
    index += 1




print(elements)
