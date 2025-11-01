# The key here is print(j, end=" "),
# which prints each number on the same row.
# Then, to advance a row,
# we use print().

n = int(input("Input a number: "))

for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print() # next line
