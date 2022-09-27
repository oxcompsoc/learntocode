# These are the solutions to all the exercises in this session

# Ex. 1

n = int(input("Please enter a number: "))

i = n
while i >= 1:
    print(i)
    i -= 1

# Ex. 2

n = int(input("Please enter a number: "))

product = 1
i = 1
while i <= n:
  product *= i
  i += 1

print(product)

# Ex. 3

number = int(input("Please enter a number: "))

while number <= 9:
    print("That number is too small!")
    number = int(input("Please enter a number: "))

print("That's a good number!")

# Ex. 4

MY_FIRST_NAME = "Tommy"
MY_LAST_NAME = "Wiseau"

first_name = input("Please enter the first name: ")
last_name = input("Please enter the last name: ")

while first_name != MY_FIRST_NAME or last_name != MY_LAST_NAME:
    print("Wrong name!")
    first_name = input("Please enter the first name: ")
    last_name = input("Please enter the last name: ")

print("Cool name!")

# Ex. 5

n = int(input("How many numbers: "))

sum = 0
i = 1
while i <= n:
    number = int(input("Please enter a number: "))
    sum += number
    i += 1

print(sum / n)

# Ex. 6

n = int(input("Please enter a number: "))

i = 1
while i <= n:
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    
    print() # Print a new line
    i += 1

# Ex. 7

cities = ["Sofia", "Plovdiv", "Suceava"]
print(cities)
print(cities[0])
print(cities[1])
print(cities[2])
print("The length of the list was: " + str(len(cities)))

# Ex. 8

shopping_list = ["bread", "smoked salmon", "cherry tomatoes", "cream cheese"]

i = 0
length = len(shopping_list)
while i < length:
    print(shopping_list[i])
    i += 1

# Ex. 9

shopping_list = ["bread", "smoked salmon", "cherry tomatoes", "cream cheese"]
n = int(input("Please enter a number: "))

i = 0
while i < n:
    j = 0
    while j < len(shopping_list):
        print(shopping_list[j])
        j += 1
    i += 1


# Ex. 10

print('Welcome to the shopping list app!')
n = int(input('Please enter the size of your shopping list: '))
i = 0
shopping_list = [0] * n
while i < n:
    shopping_list[i] = input('Please enter item number ' + str(i))
    i += 1

print('Your shopping list is:')
# From Ex 8
i = 0
length = len(shopping_list)
while i < length:
    print(shopping_list[i])
    i += 1

# Ex. 11

print('Welcome to the shopping list app!')
i = 0
shopping_list = []
last_item = ""
while last_item != "end":
    last_item = input('Please enter item number ' + str(i))
    shopping_list.append(last_item)
    i += 1

shopping_list.remove("end")

print('Your shopping list is:')
# From Ex 8
i = 0
length = len(shopping_list)
while i < length:
    print(shopping_list[i])
    i += 1