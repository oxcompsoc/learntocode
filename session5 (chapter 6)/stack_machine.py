instructions = [ 1, 2, 3, "+", "+" ]
stack = []

for instruction in instructions:
    if instruction == "+":
        x = stack.pop()
        y = stack.pop()
        stack.append(x + y) # Push the result
    else:
        stack.append(instruction) # This is just a number
        
print(stack)