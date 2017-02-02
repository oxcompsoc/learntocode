print("Please think of a number between 1 and 1000 (inclusive)")
print("When I guess, enter low, high, or right")

low = 1
high = 1000
correct = False

while not correct:
    # We need to right // instead of / for integer division
    guess = (low + high) // 2
    response = input("I guess " + str(guess) + ": ")
    if response == "right":
        correct = True
    elif response == "high":
        high = guess - 1
    elif response == "low":
        low = guess + 1

print("Yay!")
