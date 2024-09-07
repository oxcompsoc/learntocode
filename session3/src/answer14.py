n = int(input("Please enter a non-negative integer: "))

while(n < 0):
    print("Invalid number! Please enter again.")
    n = int(input("Please enter a non-negative integer: "))
    
product = 1
i = 1
while i <= n:
    product *= i
    i += 1

print(product)