score = 0

print("What day of the week are Tech Talks?")
print("A: Wednesday")
print("B: Thursday")
print("C: Saturday")
guess = input("Enter a guess: ")

if guess == "A":
    print("Correct!")
    score = score + 1
else:
    print("Wrong! It's Wednesday")

print("What day of the week is Learn to Code?")
print("A: Wednesday")
print("B: Thursday")
print("C: Friday")
guess = input("Enter a guess: ")

if guess == "B":
    print("Correct!")
    score = score + 1
else:
    print("Wrong! It's Thursday")


print("What day of the week are Geek Nights?")
print("A: Sunday")
print("B: Monday")
print("C: Saturday")
guess = input("Enter a guess: ")

if guess == "C":
    print("Correct!")
    score = score + 1
else:
    print("Wrong! It's Saturday")

print("You scored " + str(score) + " points")
