numbers = [1.5,-2.2,-0.3,0.6,8,-0.2] # actual numbers may vary


# (a): while loop
i = 0
while i < len(numbers):
  numbers[i] = 0
  i += 1

# (b): for loop
for i in range(len(numbers)):
  numbers[i] = 0


print(numbers)
