#Convert postfix to prefix
# I will convert first postfix to infix and infix to prefix

def is_operator(c):
    return c in "+-*/"

def get_symbol_precedence(prec, chr):
    return prec.get(chr, 0)

def infix_to_prefix(s, prec):
    # Reverse the infix expression and replace '(' with ')' and vice versa in one step
    s = ''.join(['(' if c == ')' else ')' if c == '(' else c for c in s[::-1]])
    stk = []
    pre = ""
    i = 0
    while i < len(s):
        if s[i].isalnum():
            pre += s[i]
        else:
            while stk and get_symbol_precedence(prec, s[i]) < get_symbol_precedence(prec, stk[-1]):
                pre += stk.pop()
            stk.append(s[i])
        i += 1
    while stk:
        pre += stk.pop()
    
    pre = pre[::-1]
    return pre

def postfix_to_infix(post):
    stack = []

    for c in post:  # reading from left to right
        if is_operator(c):
            # we need two operands to bracket around
            op2 = stack.pop()
            op1 = stack.pop()

            exp = f"({op1}{c}{op2})"
            stack.append(exp)
        else:
            stack.append(c)
    return stack.pop()  # last item in the stack is the resulting infix expression

post_expr = "abc*+de/-"
prec = {'+': 1, '-': 1, '*': 2, '/': 2}

pref = infix_to_prefix(postfix_to_infix(post_expr), prec)

print(pref)  # Expected output: "+a-*bc/de"




