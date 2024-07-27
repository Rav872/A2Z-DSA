# postfix to infix conversion using stack

def is_operator(c):
    return c in "+-*/"

def postfix_to_infix(post):
    stack = []

    for c in post: # reading from left to right
        if is_operator(c):
            # we need two operands to bracket around
            op1 = stack.pop()
            op2 = stack.pop()

            exp = f"({op1}{c}{op2})"
            stack.append(exp)
        else:
            stack.append(c)
    return stack.pop()     # last item in the stack is resulting infix operation


post_expr = "abc*+de/-"
print(postfix_to_infix(post_expr))
