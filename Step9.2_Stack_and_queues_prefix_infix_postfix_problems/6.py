#Convert infix to prefix conversion

def get_symbol_precedence(prec, chr):
    return prec.get(chr, 0)

def infix_to_prefix(s, prec):
    s = s[::-1]
    # Reverse the infix expression and replace '(' with ')' and vice versa in one step
    s = ''.join(['(' if c == ')' else ')' if c == '(' else c for c in s])
    stk = []
    pre = ""
    i = 0
    while i < len(s):
        if s[i].isalnum():
            pre = pre + s[i]
        else:
            while stk and get_symbol_precedence(prec, s[i]) <= get_symbol_precedence(prec, stk[-1]):
                pre = pre + stk.pop()
            stk.append(s[i])
        i += 1
    while stk:
        pre = pre + stk.pop()
    
    pre = pre[::-1]
    return pre


s = "a+b*c-d/e"
prec = {'+': 1, '-': 1, '*': 2, '/': 2}

pre = infix_to_prefix(s, prec)

print(pre)