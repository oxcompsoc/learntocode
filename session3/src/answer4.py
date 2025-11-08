# (a)
print('Welcome to the shopping list app!')
n = int(input("Please enter the size of your shopping list: "))

# Adding items to the shopping list
shopping_list = []
for i in range(n):
    last_item = input('Please enter item number ' + str(i) + ' ')
    shopping_list.append(last_item)

# Printing the shopping list
# This can either be done with:
#   for i in range(n), print shopping_list[i] 
# or:
#   for item in shopping_list, print item
print('Your shopping list is:')
for item in shopping_list:
    print(item)



# (b)
# The difference with part (a) is one line. 

print('Welcome to the shopping list app!')
n = int(input("Please enter the size of your shopping list: "))

shopping_list = []
for i in range(n):
    last_item = input('Please enter item number ' + str(i + 1) + ' ') # <- this line
    shopping_list.append(last_item)

print('Your shopping list is:')
for item in shopping_list:
    print(item)
