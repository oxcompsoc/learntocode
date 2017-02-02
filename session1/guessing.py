# We'll cover what this does later on
from random import randint

number = randint(1, 1000)
guess = None

while guess != number:
    # See the doubling exercise for why we use try and except
    try:
        guess = int(input("Enter a guess: "))
        if guess < number:
            print("You guessed too low")
        elif guess > number:
            print("You guessed too high")
    except:
        print("Only numeric entry is allowed")
        exit()

print("Correct!")
