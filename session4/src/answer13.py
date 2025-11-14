int_count = 0

while int_count != 1:
    input1 = input("The first input: ")
    try:
        int(input1)
        int_count += 1
    except:
        pass

    input2 = input("The second input: ")
    try:
        int(input2)
        int_count += 1
    except:
        pass

    if int_count == 0:
        print("That is too few integers. Please try again.")
    elif int_count == 1:
        print("Exactly one of these is an integer!")
    else: # Because of how the progrmais designed we already know that int_count == 2 and don't have to check it.
        print("That is too many integers. Please try again.")
