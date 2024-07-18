# Reverse word in a string
 
s = "this is an amazing program"
 
stack = []
temp = ""
result = ""
for char in s:
    if char != ' ':
        temp += char
    elif char == ' ':
        stack.append(temp)
        temp = ""
stack.append(temp)
print(stack)
length = len(stack) 
while length > 1:
    result += stack.pop() + " "
    length -= 1
 
result += stack.pop()
 
print(result)