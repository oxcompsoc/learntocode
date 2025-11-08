# (a)
items = [] # list items will vary

n = len(items)
for i in range(n):
    print(items[n - 1 - i]) 
    # At i = 0, n - 1 - i will be equal to n - 1,
    # which is the index of the last item in a list of length n.

# There is another solution that looks like this:
n = len(items)
for i in range(n):
    print(items[ - 1 - i ]) 
# and this uses something we didn't talk about in the notes.
# Negative indexing.
# So items[-1] is the last item of the list, items[-2] is the second-last, and so on.
# Which code block do you prefer? (Free response)

# (b)
# After running this code, items is reversed, and backwards is empty.
# This is because calling .reverse() on a list
# does NOT yield a new list!
# Rather, it simply reverses the existing list.
