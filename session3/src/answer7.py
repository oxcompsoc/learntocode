# This question really is extremely hard.
# If you got it, give yourself a hearty pat on the back.

current_sequence = [1]

# (b): user iteration count
n = int(input("Look-and-say depth: "))

# (b): looping
# We only need to compute n - 1 terms, since the first term is given (1).
# Though, of course, we shouldn't print 1 if the user asked for 0 terms.
if n > 0:
    print(1)
for i in range(n - 1):
    next_sequence = [] # Store the next sequence
    currently_looking_at = current_sequence[0] # Start looking at the first digit
    digit_chain_length = 0 
    for digit in current_sequence:
        # (a): If the digits are the same: tally
        if digit == currently_looking_at:
            digit_chain_length += 1
        # (a): If the digits are different: add stuff to the sequence
        else:
            next_sequence.append(digit_chain_length)
            next_sequence.append(currently_looking_at)

            # (a): Update currently_looking_at and reset the tally
            currently_looking_at = digit
            digit_chain_length = 1

    # When we hit the end of the sequence,
    # we should append the length and current digit one more time.
    next_sequence.append(digit_chain_length)
    next_sequence.append(currently_looking_at)
            
    # Set the current sequence to the next sequence
    current_sequence = next_sequence

    # (b): Print the current sequence
    # Session 2, exercise 9 showed us how to print out this list
    # with no square brackets and no extra spacing.
    for digit in current_sequence:
        print(digit, end="") # prints the digits right next to each other on the same line
    print() # moves to the next line

# The printing of the sequence can actually be done while we're computing it,
# but it's more sensible to do all the computing first,
# then the outputting afterward.

# Sometimes it's more sensible to mix in the output logic
# into the computing logic, though.
# Can you think of any examples of this?
