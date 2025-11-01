# I think it's VERY WEIRD that Python lets you do this.
# This is partially because Python is dynamically typed.
# To illustrate what this means, consider the code:
x = 12
print(x)
x = "twelve"
print(x)
# The variable x changed types over the course of this program.
# It started as a number and changed into a string.

# If a programming language doesn't allow variables to change types over the course of a program,
# then that language is said to be statically typed,
# as opposed to languages like Python here.

# Static typing is very useful for proving that your code has no errors in it,
# but dynamically typed languages are more lenient to learn, and easier to read.

# Well, static typing is only half the story.
# The other half is that a language probably shouldn't allow people to overwrite the default functions like this.
# But that's just what I think, of course. What do you think?
