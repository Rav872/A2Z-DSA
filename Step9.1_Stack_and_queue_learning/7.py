# Check for balanced parenthesis

def balance_parenthesis(s):
    stk = []
    i = 0
    while i < len(s):
        if s[i] == '{' or s[i] == '(' or s[i] == '[':
            stk.append(s[i])
        if stk:
            if (s[i] == ')' and stk[-1] == '(') or (s[i] == '}' and stk[-1] == '{') or (s[i] == ']' and stk[-1] == '['): # stk[-1] means stk[top]
                stk.pop()
        else:
            return False
        i += 1
    return len(stk) == 0

# s = "()[{()}]"
s = "{[({[]})]}"
print(balance_parenthesis(s))
