# The following will work correctly if you enter a number, but what happens if
# you don't?
x = input("Enter a number: ")
print(int(x) * 2)

# To resolve the issue, comment out the code above and uncomment the below:
# x = input("Enter a number: ")
# try:
    # The computer will try to run the code
#     print(int(x) * 2)
# except:
    # But if it can't - and only if it can't - this code is executed instead
#    print("Please enter a number")
