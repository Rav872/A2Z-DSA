#Infix to postfix conversion using stack
# Not pragmatic to implement all operations(+, -, *) in one scan in infix conversion so we need to convert into postfix
# or prefix through symbol and their precedence

# equation should make fully parenthesis using parenthesisation(precedence)

def get_symbol_precedence(prec, chr):
    return prec.get(chr, 0)

def infix_to_postfix(s, stk, prec):
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

s = "a+b*c-d/e"
stk = []
prec = {'+': 1, '-': 1, '*': 2, '/': 2}

post = infix_to_postfix(s, stk, prec)

print(post)