d = {}      # This makes an empty dictionary called d

d["some_key"] = "some_value"    # Setting the value of some_key in the dictionary to "some_value"

# Different way of achieving the same as above
a = "some_key"
b = "some_value"
d[a] = b

# Concrete examples:
fav_nums = { "good": 3, "better": 7, "best": 37 }
print(fav_nums["better"])   # prints 7
print(fav_nums["good"])     # prints 3
print(fav_nums["best"])     # prints 37

numStrings = {}
numStrings[12] = "twelve"
numStrings[8] = "eight"
print(numStrings[1])        # Question: What will this print?

constants = {}
constants[3.14] = "pi"
constants[2.72] = "e"

phone_book = { "+44 01337 ******": "Jeff", ... }
num = input("Enter a phone number: ")
print("Belongs to " + phone_book[num])

# Printing the elements of a dictionary
for phone_number in phone_book:
    person = phone_book[phone_number]
    print(person + " has phone number " + phone_number)