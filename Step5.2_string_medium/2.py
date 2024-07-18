#Maximum depth of nested parenthesis
 
s = "( a(b) (c) (d(e(f)g)h) I (j(k)l)m)"
 
count = 0
 
stack = []
 
for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
    elif s[i] == ')':
        if count < len(stack):
            count = len(stack)
        stack.pop()
        
print("Max count is : ", count)