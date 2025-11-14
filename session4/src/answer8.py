sum = 0
count = 0
num = input("Please enter a number: ")

while num != "":
    sum += float(num)
    count += 1
    num = input("Please enter a number: ")

avg = sum / count
print("The average was: " + str(avg))