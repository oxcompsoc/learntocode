n = int(input("Input side length of the square: "))

for i in range(0,n):
    print("*",end="")
print("")

# Without string multiplication
for i in range(0,n-2):
    print("*",end="")
    for j in range(0,n-2):
        print(" ",end="")
    print("*")

if n > 1: # so that it only outputs 1 star when n is 1
    for i in range(0,n):
        print("*",end="")
    print("")