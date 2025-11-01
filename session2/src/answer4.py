# Directly following the flowchart gives you this:
year = int(input("Enter year: "))
if year % 400 == 0:
    print(str(year)+" is a leap year")
elif year % 100 == 0:
    print(str(year)+" is not a leap year")
elif year % 4 == 0:
    print(str(year)+" is a leap year")
else:
    print(str(year)+" is not a leap year")

# These blocks can be compressed into a single condition that looks like this:
year = int(input("Enter year: "))
if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
    print(str(year)+" is a leap year")
else:
    print(str(year)+" is not a leap year")
