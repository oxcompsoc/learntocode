# (a). Letting the user input their number of numbers
int_count = input("Number of numbers to be inputted: ")

while type(int_count) == str:
  try:
    int_count = int(int_count)
  except:
    int_count = input("That was not an integer. Please try again: ")

while (int_count > 0):
    user_input = input("Input: ")
    try:
        int(user_input) 
        # This tries to convert user_input into an int
        # and does nothing with the resulting value.

        int_count -= 1
    except:
        pass 
        # Python doesn't allow us to have nothing in the except block,
        # so we write "pass", which means "do nothing".
print("You have inputted the maximum allowed number of integers. Goodbye!")



# (b). What about negative numbers and zero?
# This implementation allows the user to enter 0,
# but asks the user for another number if they enter a negative number.
int_count = input("Number of numbers to be inputted: ")

while type(int_count) == str:
  try:
    int_count = int(int_count)
    if int_count < 0:
        # This line sets int_count back to a string, so we don't exit the while loop.
        int_count = input("That is not a valid number of numbers. Please try again: ")
  except:
    int_count = input("That was not an integer. Please try again: ")

