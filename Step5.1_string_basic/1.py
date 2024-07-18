strArr = "(())())(())()"
 
count = 0
c = 0
print("Length of string array is: ", len(strArr))
result = ""
while c < len(strArr):
    if strArr[c] == '(' and count > 0:
        print("Adding", c, strArr[c])
        result += strArr[c]
    if strArr[c] =='(':
        count += 1
    if strArr[c] == ')' and count > 1:
        print("Adding", c, strArr[c])
        result += strArr[c]
    if strArr[c] == ')':
        count -= 1
    c += 1
    
print(result)