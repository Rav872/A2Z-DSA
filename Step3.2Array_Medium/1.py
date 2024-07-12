my_list = [1,2,3,4,10,12]

result = []
Sum = 25
for i in range(len(my_list)):
    value = Sum - my_list[i]
    if value in my_list:
        j = my_list.index(value)
        if i != j:
            result.append(i)
            result.append(j)
            break

if len(result) == 0:
    result.append(-1)
    result.append(-1)

print(result)