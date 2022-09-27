n = int(input("Input side length of the square: "))

print("*"*n)

# With string multiplication
for i in range(0,n-2):
    print("*" + " "*(n-2) + "*")

if n > 1: # so that it only outputs 1 star when n is 1
    print("*"*n)