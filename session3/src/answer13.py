MY_FIRST_NAME = "Tommy"
MY_LAST_NAME = "Wiseau"

first_name = input("Please enter the first name: ")
last_name = input("Please enter the last name: ")

while first_name != MY_FIRST_NAME or last_name != MY_LAST_NAME:
    print("Wrong name!")
    first_name = input("Please enter the first name: ")
    last_name = input("Please enter the last name: ")

print("Cool name!")