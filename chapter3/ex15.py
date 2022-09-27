n = 0
sum = 0
num = float(input("Please enter a number: "))

while not num == -1:
    sum += num
    n += 1
    num = float(input("Please enter a number: "))

avg = sum/n
print("The average was "+str(avg))