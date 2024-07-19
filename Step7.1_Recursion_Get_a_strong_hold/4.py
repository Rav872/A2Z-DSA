# Sort a stack using recursion

def insertSortedStack(stack, item):
    if len(stack) == 0 or stack[-1] >= item:
        stack.append(item)
    else:
        top_element = stack.pop()
        print("Top element: ", top_element)
        insertSortedStack(stack, item)
        stack.append(top_element)

def sortStack(stack):
    if len(stack) > 0:
        top = stack.pop()
        sortStack(stack)
        print("top: ", top)
        insertSortedStack(stack, top)


stack = [1,5,2,4]
sortStack(stack)
print("Sorted stack: ", stack)
