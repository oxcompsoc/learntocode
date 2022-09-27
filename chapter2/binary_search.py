print("Please think of a number that is >= 0 and < 1000")

numberIsGeqTo = 0
numberIsLtThan = 1000

while numberIsGeqTo + 1 != numberIsLtThan:
    # We need to right // instead of / for integer division
    guess = (numberIsGeqTo + numberIsLtThan) // 2
    response = input("Is your number less than " + str(guess) + "? ")
    if response == "yes":
        numberIsLtThan = guess
    elif response == "no":
        numberIsGeqTo = guess

print("Your number is " + str(numberIsGeqTo))