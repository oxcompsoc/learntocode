n = int(input("Input side length of the square: "))

# The square can be printed with no string multiplication like this:
for i in range(0,n):
    print("*", end="")
print()
for i in range(0,n-2):
    print("*",end="")
    for j in range(0,n-2):
        print(" ",end="")
    print("*")
for i in range(0,n):
    print("*", end="")
print()


# Here's a version that uses string multiplication:
print("*" * n)
for i in range(0,n-2):
    print("*" + " " * (n-2) + "*")
print("*" * n)


# Here's a version that checks if n >= 2
# before adding the "bottom" of the square in.
print("*" * n)
for i in range(0,n-2):
    print("*" + " " * (n-2) + "*")
if n >= 2:
    print("*" * n)


# With string addition, we can build the entire square as one string before printing it in one go:
output = "*" * n + "\n"
for i in range(0,n-2):
    output += ("*" + " " * (n-2) + "*\n")
if n >= 2:
    output += "*" * n
print(output)
# but this isn't really an improvement over the previous version.
