numbers = []
x = None
while x != "done":
    x = input("Enter a number or done: ")
    try:
        # int() will throw an exception if the number isn't a number
        numbers.append(int(x))
    except:
        x = "done"

# Sort the list
numbers.sort()

if len(numbers) % 2 == 0: # Even length
    median = (numbers[len(numbers) // 2 - 1] + numbers[len(numbers) // 2]) / 2
else:
    median = numbers[len(numbers) // 2]

print("Median = {}".format(median))
