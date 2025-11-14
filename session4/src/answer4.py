sum = 0
num = input("Add: ")

while num != "":
    sum += float(num)
    num = input("Add: ")

print("Your total is: " + str(sum))