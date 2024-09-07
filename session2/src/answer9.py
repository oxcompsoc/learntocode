t = int(input("Input a number: "))
a = 0
b = 1
for i in range(t):
    c = a + b # calculate new term
    #shift the terms by 1
    a = b
    b = c
    # Alternatively:
    # a,b = b,a+b
print("Term " + str(i) + " is " + str(a))