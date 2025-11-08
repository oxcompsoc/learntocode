items = [] # fill this list with any items you like
n = int(input("Split the list where: "))

take = items[0:n] # When slicing, left = 0 is the default, so we can also write take = items[:n].
drop = items[n:len(items)] # When slicing, right = len(items) is the default, so we can also write drop = items[n:].

print("List has been split: ")
print(take)
print(drop)
