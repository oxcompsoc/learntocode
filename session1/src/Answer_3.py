a = float(input("Input the first number: "))
b = float(input("Input the second number: "))
average = (a+b)/2
print("The average is "+str(average))

# whether using float or int as INPUT is used depends on scenario
# if you are averaging heights of different people (in meters), then it certainly has to be float
# if you are averaging MC test scores then int would be more appropriate

# But regardless, the OUTPUT should be a float, because avaerage of integers can have decimal places. (e.g. average of 3 and 4 is 3.5)

# To extend the program to calculate the average of a few more numbers, just add a few more variables.
# Or a better approach is looping, which we would introduce in the third session.
