# Making decisions

Last week we looked at the very basics of Python, including basic functions like
`print` and `input`, variables, strings, and `if` statements. The following code
summarises what we looked at last week:

```python
# This is a comment; it doesn't get executed

# Basic arithmetic:
x = 1 + 2 - 3 * 4 / 5 + 6 - 7 * 8 / 9
print(x)

# If we want to use a piece of text we must enclose it in quotation marks
# Text inside quotation marks is called a string
name = "Thomas"

# x and name are the names for variables

print("Hello " + name)

# The input function shows a prompt on the screen, and gives us back the text
# that the user entered
friend = input("Who is you friend?")

# If we want to compare two variables we have to use ==, not =
if friend == name:
    # Code that needs to execute if friend and name are the same must be
    # indented. To indent either use 4 spaces or press tab
    print("You can't be friends with yourself")
else:
    # This code is only executed if friend and name are not the same
    print(name + " and " + friend + " are friends")
```

## If, elif, and else

Last week we only saw `if` and `else`, but if we have multiple different cases
we want to consider we can use `elif` as well:

```python
x = input("Enter a name: ")
if x == "Thomas":
    print("Secretary of CompSoc")
elif x == "Matt":
    # This code is only executed if x == "Matt"
    print("President of CompSoc")
elif x == "Chris":
    print("Treasurer of CompSoc")
else:
    # This code is only executed if none of the other conditions hold
    print(x + " is not on the committee")
```

Sometimes we want multiple conditions to hold. To do this we could nest lots of
`if` statements inside each other:

```python
if it_is_raining then:
    if we_are_in_oxford:
        print("Makes sense")
```

However, we can write this more compactly:

```python
if it_is_raining and we_are_in_oxford:
    print("Makes sense")
```

Alternatively if we just want one condition to hold then we can use `or`:

```python
if x < -100 or x > 100:
    print("|x| > 100")
```

This is not like `or` as we traditionally use it in English: it is OK for both
of the conditions to hold:

```python
if x >= 0 or x < 0:
    print("Always true if x is a number")
```

Finally, we can use `not` if we want to do something if something isn't true:

```python
if not x > 10:
    print("x <= 10")

# Which is the same as:
if x > 10:
    # Do nothing
else:
    print("x <= 10")
```

## For loops

Suppose you wanted to add up every number between 1 and 10. You could write out
the following:

```python
x = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
```

But that's tedious! Instead we can use `for` loops to do something a certain
number of times:

```python
total = 0
for i in range(1, 11):
    total = total + i
# Mathematicians will note there is a much easier way to do this
```

Here we had to go up to `11` in the `range` because `range(start, end)` will
give us every number from `start` that is *less than* `end` (i.e. all `i` such
that `start <= i < end`.

## While loops

While loops are almost exactly the same as `if` statements, except that they
will repeat their code whilst the condition is true:

```python
x = 0
while x < 5:
    print(x)
    x = x + 1
```

We could build a simple password prompt, for example:

```python
# This is really insecure...
password = "Pa55w0rd"
attempt = None

while attempt != password:
    attempt = input("Please enter your password: ")
print("You're in!")
```

## Guessing game

```python
number = 337
guess = None

while guess != number:
    # See the doubling exercise for why we use try and except
    try:
        guess = int(input("Enter a guess: "))
        if guess < number:
            print("You guessed too low")
        elif guess > number:
            print("You guessed too high")
    except:
        print("Only numeric entry is allowed")
        exit()

print("Correct!")
```

## String formatting

So far when we have wanted to output a mix of strings, or numbers and strings,
we have just concatenated them together with `+`. To make life easier, we can
alternatively do this:

```python
name = "Thomas"
age = 19

message = name + " is " + str(age) + " years old"

# Becomes
message = "{} is {} years old".format(name, age)

# We write {} for each substitution, and then list them
```

## Defining functions

We've used a few functions so far, but we haven't made any of our own yet. We
write functions so that we can encapsulate common ideas and avoid have to repeat
ourselves.

Consider the following code:

```python
name = "Thomas"
role = "secretary"
message = "{} is the {}".format(name, role)
print(message)

name = "Matt"
role = "president"
message = "{} is the {}".format(name, role)
print(message)
```

Here we have repeated the process of making the message twice, which seems a bit
wasteful. Lets define a function that does it instead:

```python
def make_message(name, role):
    # name and role are local to the function
    return "{} is the {}".format(name, role)

# Now we can write this instead
name = "Thomas"
role = "secretary"
message = make_message(name, role)
print(message)

name = "Matt"
role = "president"
message = make_message(name, role)
print(message)

# We don't need the message variable, we can just take the value from
# make_message and give it to print

name = "Thomas"
role = "secretary"
print(make_message(name, role))

name = "Matt"
role = "president"
print(make_message(name, role))

# Furthermore, we don't even need the name and role variables
print(make_message("Thomas", "secretary"))
print(make_message("Matt", "president"))
```

In this example we managed to make the overall program length a little shorter,
but 

## Where next?

Here we hit an interesting impasse: we've now shown you most of the basic
compositional units of programs: variables, if statements, while loops, for
loops, and functions. We won't introduce many more in the remaining four
sessions.

What we've seen so far is mostly just syntax, i.e. what we write. We haven't
really looked at problem solving at all yet.
