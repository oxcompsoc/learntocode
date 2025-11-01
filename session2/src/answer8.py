t = int(input("Input a number: "))
a = 0
b = 1
for i in range(t):
    c = a + b # calculate new term
    # shift the terms by 1
    a = b
    b = c
print("Term " + str(i) + " is " + str(a))

# Instead of the three lines 
#   c = a + b
#   a = b
#   b = c
# you can simply write
#   a,b = b,a+b
# because Python updates a and b "at the same time",
# meaning you don't need to do any storing and shifting.
# With this in mind, you may enjoy revisiting question 2. :)
