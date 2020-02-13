### Recap:

# Any text after a '#' symbol on a line is a comment. It is not part of the code.

# Password checker using while loops:
SECRET_PASSWORD = "pass123"
user_input = input("Please enter a password: ")

while user_input != SECRET_PASSWORD:
  print("Access denied: wrong password.")
  print() # Print a newline. This is just here to make things look nicer.
  user_input = input("Please enter the password: ")

print("Access granted.")


# Incrementing and other syntactic sugar. The shorthands for the following:
number = number + 1
number = number - 1
number = number * 2
number = number / 3

# are respectively:

number += 1     # Equivalent to saying "increase number by 1", i.e. increment it
number -= 1     # Equivalent to saying "decrement number by 1", i.e. decrement it
number *= 2     # Equivalent to saying "number becomes itself times 2"
number /= 3     # Equivalent to saying "number becomes itself divided by 3"


# Counting using while loops:

n = int(input("Please enter a number: "))
i = 1
while i <= n:
  print(i)
  i += 1 # Increment i (i becomes bigger by 1).

# Finding the sum of the first n natural numbers:
n = int(input("Please enter a number: "))
i = 1
sum = 0
while i <= n:
  sum += i
  i += 1

print("The sum of the first " + str(n) + " natural numbers is " + str(sum))



#### Defining lists
shopping_list = [ "bread", "smoked salmon", "cherry tomatoes", "cream cheese" ]

#### len
number_of_items = len(shopping_list) # number_of_items = 4

#### Reading elements
item = shopping_list[0] # item is now "bread", Python lists start indexing at 0
item = shopping_list[1] # item is now "smoked salmon"

#### Reassinging list elements
shopping_list[3] = "cheddar" # The list is now [ "bread", "smoked salmon", "cherry tomatoes", "cheddar" ]

#### Appending to a list
shopping_list.append("mayo") # shopping_list is now [ "bread", "smoked salmon", "cherry tomatoes", "cheddar", "mayo" ]

#### Removing an element from the end of a list
del shopping_list[4] # shopping_list is now [ "bread", "smoked salmon", "cherry tomatoes", "cheddar" ]

#### Remove an element with a specific value
shopping_list.remove("mayo")

#### Joining lists
shopping_page1 = ["bread", "smoked salmon", "cherry tomatoes"]
shopping_page2 = ["cheddar", "mayo" ]
shopping_list = shopping_page1 + shopping_page2 # shopping_list is now [ "bread", "smoked salmon", "cherry tomatoes", "cheddar", "mayo" ]

#### For loop example:
n = int(input("Please enter a number: "))
for i in range(1, n):
    print(i)


#### Generic for loop:
for i in range(a, b):
    # block of code - this block will repeat (b - a) times and you will
    # have access to the number of the current "repeat" with i


#### Iterating over lists:
shopping_list = [ "bread", "smoked salmon", "cherry tomatoes", "cream cheese" ]
for item in shopping_list:
    print("I need to buy " + item)

# This will print out:
# I need to buy bread
# I need to buy smoked salmon
# I need to buy cherry tomatoes
# I need to buy cream cheese
