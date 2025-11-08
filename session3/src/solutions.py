# Ex. 1

cities = ["Sofia", "Plovdiv", "Suceava"]
print(cities)
print(cities[0])
print(cities[1])
print(cities[2])
print("The length of the list was: " + str(len(cities)))

# Ex. 2

shopping_list = ["bread", "smoked salmon", "cherry tomatoes", "cream cheese"]

i = 0
length = len(shopping_list)
while i < length:
    print(shopping_list[i])
    i += 1

# Ex. 3

shopping_list = ["bread", "smoked salmon", "cherry tomatoes", "cream cheese"]
n = int(input("Please enter a number: "))

i = 0
while i < n:
    j = 0
    while j < len(shopping_list):
        print(shopping_list[j])
        j += 1
    i += 1

# Ex. 4

print('Welcome to the shopping list app!')
i = 0
shopping_list = []
last_item = ""
while i < n:
    last_item = input('Please enter item number ' + str(i) + ' ')
    shopping_list.append(last_item)
    i += 1

print('Your shopping list is:')
# From Ex 2
i = 0
length = len(shopping_list)
while i < length:
    print(shopping_list[i])
    i += 1

# Ex. 5
# Same as Ex. 4 with an additional +1 at the line last_item = input('Please enter item number ' + str(i+1) + ' ')
print('Welcome to the shopping list app!')
i = 0
shopping_list = []
last_item = ""
while i < n:
    last_item = input('Please enter item number ' + str(i+1) + ' ')
    shopping_list.append(last_item)
    i += 1

print('Your shopping list is:')
# From Ex 2
i = 0
length = len(shopping_list)
while i < length:
    print(shopping_list[i])
    i += 1

# Ex. 6
# Same as Ex. 4 but with the while loop condition changed
print('Welcome to the shopping list app!')
i = 0
shopping_list = []
last_item = ""
while last_item != "end":
    last_item = input('Please enter item number ' + str(i) + ' ')
    shopping_list.append(last_item)
    i += 1

shopping_list.remove("end")

print('Your shopping list is:')
# From Ex 2
i = 0
length = len(shopping_list)
while i < length:
    print(shopping_list[i])
    i += 1

