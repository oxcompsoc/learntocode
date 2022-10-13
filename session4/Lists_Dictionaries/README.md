# Session 4: Lists (cont.) and Dictionaries

## Recap

In [the previous few sessions][s3notes] we took a look at *lists*, which are ordered collections of Python values. Here's an overview of all the concepts so far:

```python
# Any text after a '#' symbol on a line is a comment. It is not part of the code.

# Defining a list
shopping_list = [ "bread", "smoked salmon", "cherry tomatoes", "cream cheese" ]

# Getting the "len"gth of a list
number_of_items = len(shopping_list) # number_of_items = 4

# indexing (starts at 0)
item = shopping_list[0] # item is now "bread", Python lists start indexing at 0
item = shopping_list[1] # item is now "smoked salmon"

# We decided to get cheddar instead of cream chese so we can change the list like so:
shopping_list[3] = "cheddar" # The list is now [ "bread", "smoked salmon", "cherry tomatoes", "cheddar" ]

# Adding something to the end of a list
shopping_list.append("mayo") # shopping_list is now [ "bread", "smoked salmon", "cherry tomatoes", "cheddar", "mayo" ]

# Deleting an element (remember, indexing starts at 0)
del shopping_list[4] # shopping_list is now [ "bread", "smoked salmon", "cherry tomatoes", "cheddar" ]

# Remove a specific value
shopping_list.remove("mayo")

# Appending(i.e. "adding") 2 lists together
shopping_page1 = ["bread", "smoked salmon", "cherry tomatoes"]
shopping_page2 = ["cheddar", "mayo" ]
shopping_list = shopping_page1 + shopping_page2 # shopping_list is now [ "bread", "smoked salmon", "cherry tomatoes", "cheddar", "mayo" ]

# For loop printing the numbers from 1 to n (excl.)
n = int(input("Please enter a number: "))
for i in range(1, n):
    print(i)

# General Python for loop structure
for i in range(a, b):
    # block of code - this block will repeat (b - a) times and you will
    # have access to the number of the current "repeat" with i

# Iterating over a list
shopping_list = [ "bread", "smoked salmon", "cherry tomatoes", "cream cheese" ]
for item in shopping_list:
    print("I need to buy " + item)

# This will print out:
# I need to buy bread
# I need to buy smoked salmon
# I need to buy cherry tomatoes
# I need to buy cream cheese


# Printing a list using range
shopping_list = [ "bread", "smoked salmon", "cherry tomatoes", "cream cheese" ]
for i in range(0, len(shopping_list)):
    print("I need to buy " + shopping_list[i])

# This will print out:
# I need to buy bread
# I need to buy smoked salmon
# I need to buy cherry tomatoes
# I need to buy cream cheese

# Function examples:
def myNameRet():
    return "My name is Anton"
print(myNameRet())     # Will print "My name is Anton"

def myNameNoRet():
    print("My name is Anton")
myNameNoRet()       # Will also print "My name is Anton"

def square(x):
    return x * x

print(square(5))    # Will print "25"
print(square(10))   # Will print "100"

def rectArea(width, height):
    return width * height
print(rectArea(3, 4))   # Will print 12


# Example of None
def getShapeArea(shape_name, x, y):
    if shape_name == "rectangle":
        return x * y
    elif shape_name == "triangle":
        return x * y / 2

if getShapeArea("rectangle", 5, 10) > getShapeArea("tringle", 5, 10): # typo intentional
    print("The rectangle has a larger area")

```

[s3notes]: https://github.com/oxcompsoc/learntocode/tree/master/session3

## Exercises

In today's session we are going to keep on looking at lists by continuing with some of the exercises from last week's session (we deliberately wrote far too many for a single session). Here's a [link to the exercises](https://github.com/oxcompsoc/learntocode/blob/master/session3/README.md#Exercises-1).

If you get stuck, as well as asking a volunteer for help, you can also look at [last week's solutions][s3solutions] and [the video of this session from a previous year][s3video].

[s3solutions]: https://raw.githubusercontent.com/oxcompsoc/learntocode/master/session3/solutions.py
[s3video]: https://www.youtube.com/watch?v=TU1aisio7IU

## Dictionaries

Once you're comfortable with the idea of lists, we're going to take a look at
*dictionaries*. These are another fundamental data structure and they work
pretty similarly to lists, only that instead of being indexed by integers they
are indexed by *keys*, which can be any Python value that we've seen so far. We
will say that a dictionary *maps keys to values*.

We create an empty dictionary called `d` with the following

```python
d = {}      # This makes an empty dictionary called d
```

Then, when we want the dictionary to map a *key* to a *value* we write

```python
d["some_key"] = "some_value"
```

It's really important to note that we could have written *anything* that we've
seen so far as the subscript index inside the square brackets but we'll
continue to use strings. Please note that the above is equivalent to:

```python
a = "some_key"
b = "some_value"
d[a] = b
```

Just as with lists, we don't have to initialise a dictionary to the empty
dictionary, and we could instead initialise it with some mappings:

```python
fav_nums = { "good": 3, "better": 7, "best": 37 }
```

To access an element of a dictionary we just write `d[k]` where `d` is the name
of a dictionary variable, and `k` is a key. So in this case:

```python
fav_nums = { "good": 3, "better": 7, "best": 37 }
print(fav_nums["better"])   # prints 7
print(fav_nums["good"])     # prints 3
print(fav_nums["best"])     # prints 37
```

While dictionaries are most often used with strings as keys you can use anything you want as a key. So the following is also valid:

```python
numStrings = {}
numStrings[12] = "twelve"
numStrings[8] = "eight"
print(numStrings[1])        # Question: What will this print?

constants = {}
constants[3.14] = "pi"
constants[2.72] = "e"
```

**Question:** What's the difference between a dictionary with integer keys and a list?

Dictionaries, like lists, are incredibly important data structures in Computer
Science because we can use them to model relations between sets. For example,
we can model a phone book with a dictionary:

```python
phone_book = { "+44 01337 ******": "Jeff", ... }
num = input("Enter a phone number: ")
print("Belongs to " + phone_book[num])
```

If we then wanted to *iterate* through all the keys (i.e. phone numbers) and
values (i.e. names) we can then do the following:

```python
for phone_number in phone_book:
    person = phone_book[phone_number]
    print(person + " has phone number " + phone_number)
```

**Question:** Why should we represent phone numbers with strings? Why shouldn't
we use a list instead?

Dictionaries are also often used to represent [graphs][].

[graphs]: https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)

Please note that in many other programming languages what Python calls a
dictionary is instead called a [map][].

[map]: https://en.wikipedia.org/wiki/Associative_array 

### Dictionary exercise

This exercise is designed to be bit more challenging than others we've seen so
far, and therefore we've broken it down into smaller parts.

The goal is to create a program that takes a piece of text from the user,
splits it into separate words, and count the number of times each unique word
occurs. For example, the execution might like look:

```
Please enter some text: The Ten dollar, founding father without a father got a lot farther by working a lot harder by being a lot smarter by being a self-starter by fourteen, they placed him in charge of a trading charter

The: 1
Ten: 1
dollar,: 1
founding: 1
father: 2
without: 1
a: 6
got: 1
lot: 3
farther: 1
by: 4
working: 1
harder: 1
being: 2
smarter: 1
self-starter: 1
fourteen,: 1
they: 1
placed: 1
him: 1
in: 1
charge: 1
of: 1
trading: 1
charter: 1
```

Broadly, you can break the program down into a few different stages:

* Getting input from the user
* Separating the text entered by the user into separate words. **Hint:** you want to *split* the string on spaces - feel free to ask a volunteer
* Count the number of occurrences of each word by using a dictionary to map from words to the number of times they occur
* Output the result

There are lots of extensions to this:

* Should you consider `The` and `the` to be the same word? If so, how can you handle this?
* Can you output the words in alphabetical order or ordered by the number of occurrences
* Can you avoid including punctuation in words?
