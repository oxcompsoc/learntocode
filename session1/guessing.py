# Imports the functions from the 'random' library so that we can access them
import random

# https://docs.python.org/3/library/random.html#random.randint
answer = random.randint(0, 999)
    
for n in range(0, 10):
    guess = int(input("Guess: "))
    if guess < answer:
        print("Too low!")
    elif guess == answer:
        print("Correct, you got " + str(answer))
        break
    else:
        print("Too high")