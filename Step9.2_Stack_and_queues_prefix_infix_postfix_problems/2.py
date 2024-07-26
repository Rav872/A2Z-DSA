#Prefix to infix conversion

def is_operator(c):
    return c in "+-*/"

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


pref_expr = "*-A/BC+/DEFG"
print(prefix_to_infix(pref_expr))
