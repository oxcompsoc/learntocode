# Session 5: Coding some games 

In this session we will code some games, to consolidate what we have learnt in the previous sessions.

## Game 1: Guess the Number

The computer would generate a mystery number between 1 and 100, you and your friends will take turns to guess the number, and the range will narrow down based on the number the player guessed. The player who finally guesses the number loses.

First of all, we need the computer to randomly generate a number between 1 and 100. We can do that using this line of code:

```python
mystery = random.randint(1,100)
```

The `randint` is from the `random` library, which needs to be imported beforehand

```python
import random
mystery = random.randint(1,100)
```

We will loop until someone guesses the correct number.

```python
correct = False
while not correct:
  # ...
```

The loop body should ask for input, and set `correct` to true when the guess is correct.

```python
correct = False
while not correct:
  # ...
  guess = int(input("Please make a choice between 1 and 100: "))
  if(guess==mystery):
    win = True
print("You guessed the number! It is " + str(mystery))
```

We narrow the range if the guess is incorrect, with the help of two variables, `upper` and `lower`.

```python
upper = 100
lower = 1
correct = False
while not correct:
  # ...
  guess = int(input("Please make a choice between "+str(lower) + " and " + str(upper)": "))
  if(guess==mystery):
    win = True
  elif(guess>mystery):
    upper = guess - 1
  elif(guess<mystery):
    lower = guess + 1
```

We check if the input is out of range, and loops until we get a valid input. 

```python
guess = int(input("Please make a choice between "+str(lower) + " and " + str(upper)": "))
if(guess>upper or guess<lower): # Can we change the order of the if statements?
  print("Out of range! Input again!")
if(guess==mystery):
  win = True
elif(guess>mystery):
  upper = guess - 1
elif(guess<mystery):
  lower = guess + 1
```

Finally we also ask for the number of players, count the number of rounds, and decide on who loses.

```python
players = int(input("How many players are there? "))
currentRound = 0
...
while not correct:
  guess = int(input("Player " + str(getPlayerNumber(players,currentRound)) + ", please make a choice between "+str(lower) + " and " + str(upper) + ": "))
  if(guess>upper or guess<lower): # Can we change the order of the if statements?
    print("Out of range! Input again!")
  if(guess==mystery):
    win = True
  elif(guess>mystery):
    upper = guess - 1
    currentRound += 1
  elif(guess<mystery):
    lower = guess + 1
    currentRound += 1
print("Player " + str(getPlayerNumber(players,currentRound)) +  " guessed the number! It is " + str(mystery))
```

For the sake of it, let's use a function to calculate the player number.

```python
def getPlayerNumber(players,currentRound):
  return currentRound%players+1
```

The full code:

```python
import random

def getPlayerNumber(players,currentRound):
  return currentRound%players+1

mystery = random.randint(1,100)

players = int(input("How many players are there? "))
currentRound = 0

correct = False
upper = 100
lower = 1
while not correct:
    print("Guess a number between %d and %d" % (lower, upper))
    guess = int(input("Player " + str(getPlayerNumber(players,currentRound)) + ", please make a choice between "+str(lower) + " and " + str(upper) + ": "))
    if(guess>upper or guess<lower):
        print("Out of range! Input again!")
    elif(guess==mystery):
        correct = True
    elif(guess>mystery):
        upper = guess-1
        currentRound += 1
    elif(guess<mystery):
        lower = guess+1
        currentRound += 1
print("Player " + str(getPlayerNumber(players,currentRound)) +  " guessed the number! It is " + str(mystery))
```