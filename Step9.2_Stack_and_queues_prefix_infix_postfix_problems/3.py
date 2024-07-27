# Prefix to postfix conversion
# Convert prefix to infix and then infix to postfix, combination of fist two questions

# Prefix to Infix -> Infix to postfix

def is_operator(c):
    return c in "+-*/"

def get_symbol_precedence(prec, chr):
    return prec.get(chr, 0)

def infix_to_postfix(s, prec):
    stk = []
    i = 0
    post = ""
    while i < len(s):
        if s[i].isalnum():
            post = post + s[i]
        else:
            while stk and get_symbol_precedence(prec, s[i]) <= get_symbol_precedence(prec, stk[-1]):
                post = post + stk.pop()
            stk.append(s[i])
        i += 1
    while stk:
        post = post + stk.pop()
    return post

def prefix_to_infix(pref):
    stack = []

    for c in pref[::-1]: # reading from right to left
        if is_operator(c):
            # we need two operands to bracket around
            op1 = stack.pop()
            op2 = stack.pop()

            exp = f"({op1}{c}{op2})"
            stack.append(exp)
        else:
            stack.append(c)
    return stack.pop()     # last item in the stack is resulting infix operation

prec = {'+': 1, '-': 1, '*': 2, '/': 2}
pref_expr = "*-A/BC+/DEFG"
postfix = infix_to_postfix(prefix_to_infix(pref_expr), prec)

print(postfix)