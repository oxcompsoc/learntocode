int_count = 2
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
