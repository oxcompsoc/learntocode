# (a)
user_input = input("Please choose an option: ")

while type(user_input) == str:
  try:
    user_input = int(user_input)
    if user_input < 1 or user_input > 8:
      user_input = input("That is not an option. Please try again: ")
  except:
    user_input = input("That is not an option. Please try again: ")

# (b)
user_input = input("Please choose an option: ")

while type(user_input) == str:
  try:
    user_input = float(user_input)
    if user_input < 0.5 or user_input > 96:
      user_input = input("That is not an option. Please try again: ")
  except:
    user_input = input("That is not an option. Please try again: ")
