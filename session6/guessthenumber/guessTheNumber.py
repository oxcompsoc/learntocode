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

