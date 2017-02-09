# While loops and functions

In the previous session we explored how to use `for` loops and `while` loops to
repeat Python statements several, or even an infinite, number of times. In this
session we are going to continue that theme by writing a simple guessing game,
before defining our own functions.

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

## Guessing game: the other way

```python
print("Please think of a number between 1 and 1000 (inclusive)")
print("When I guess, enter low, high, or right")

low = 1
high = 1000
correct = False

while not correct:
    # We need to right // instead of / for integer division
    guess = (low + high) // 2
    response = input("I guess " + str(guess) + ": ")
    if response == "right":
        correct = True
    elif response == "high":
        high = guess - 1
    elif response == "low":
        low = guess + 1

print("Yay!")
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
but for more complex tasks we would find that defining functions enables us to
write far more succinct programs.

## Lists

We've previously seen iteration through a list of numbers using `for` loops and
`range`, but quite often we will want lists of other things. Therefore we
introduce a new kind of variable: `list`.

```python
empty_list = []
list_with_some_numbers = [1, 2, 3]
list_with_some_numbers.append(4)
print(list_with_some_numbers)

for x in list_with_some_numbers:
    print(x)
```

**Challenge: adapt the guessing game to show a list of all the previous
guesses**

## Where next?

Here we hit an interesting impasse: we've now shown you most of the basic
compositional units of programs: variables, if statements, while loops, for
loops, and functions. We won't introduce many more in the remaining four
sessions.

What we've seen so far is mostly just syntax, i.e. what we write. We haven't
really looked at problem solving at all yet.
