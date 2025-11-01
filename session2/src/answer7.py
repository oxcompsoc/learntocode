n = int(input("How many numbers? "))
sum = 0
for i in range(n):
    num = float(input("Please enter a number: "))
    sum += num
avg = sum/n
print("The average was "+str(avg))