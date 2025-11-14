shouts = []
word = input("Shout: ")

while word != "":
  shouts.append(word)
  word = input("Shout: ")

# There are several ways to handle 
# printing the shouts in reverse order.

# This approach loops backwards down the list
# using a while loop.
# It does not erase the shouts as it shouts them.
i = len(shouts) - 1
while i >= 0:
  print(shouts[i])
  i -= 1

# This approach uses a while loop
# checking to see if the list is empty yet.
# It DOES erase the shouts as it shouts them.
while len(shouts) > 0:
  print(shouts.pop())

# This approach reverses the list, 
# then uses a for-in loop.
# It does not erase the shouts as it shouts them.
shouts.reverse()
for shout in shouts:
  print(shout)
