# find largest odd number in string 
largest = 0
temp = ""
number = 0
s = "24445"
 
for c in s:
    temp += c
    number = int(temp)
    if number % 2 == 1:
        largest = max(largest, number)
        
if largest == 0:
    print("Wrong string is even")
else:
    print("Largest odd number in a string is: ", largest)