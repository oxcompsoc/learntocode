items = [1,5,3,2,5,1,6,2,7,3,1,6,1,9,6,3,7] # can be any list

# Count the number of items that are equal to the first
first_item = items[0]
tally = 0
for item in items:
    if item == first_item:
        tally = tally + 1 # or tally += 1

# Correcting "times" to "time" if the item only appears once
times = "times"
if tally == 1:
    times = "time"

print(
    "The first element of this list (" 
    + str(first_item) 
    + ") appears " 
    + str(tally) 
    + " " 
    + str(times) 
    + " in the list"
)
# Spacing the print statement out like this makes it a bit easier to read