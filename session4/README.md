# Data Structures

In the course so far we have looked at the *syntax* of Python, i.e. the text
that constitutes a valid Python program, and the *semantics* of Python, i.e.
what a valid program does. These are useful tools for building basic programs
and solving simple problems, but in order to build more advanced programs we
need to look at other ways of storing and using data in our programs.

So far, we've seen that variables can store nothing, truth values, numbers, and
strings:

```python
empty = None
truth = False
number = 42
text = "Hello, world"
```

In this session, we'll look at lists and dictionaries, and how we can use them
for basic problem solving.

## Lists

The syntax for creating lists in Python is intuitive:

```python
# We can't name a variable list, because list is a *reserved keyword* in Python
my_list = [3, 7, 42]

# Iterate through every item in the list
for x in my_list:
    print("One of my favourite numbers is {}".format(x))
```

Lists can contain any number of values, and we can create lists that contain
values of multiple types. Generally, we prefer to only have a list of numbers, a
list of strings, or even a list of lists.

Sometimes we want to access a specific value in a list. Take the previous
example and run it:

```python
my_list = [3, 7, 42]
print(my_list[1])
```

You may have expected that this would print `3`, because that is the first value
in the list. If we actually wanted to get the first element from the list we'd
have to write `my_list[0]`, and if we wanted to access the third element we
write `my_list[2]`. But why is this?

Firstly, for a lot of problems it turns out to be slightly more convenient to
start at zero, otherwise we may find ourselves adding or subtracting 1 to get a
value from the array.

Secondly, we need to briefly consider how computer memory works. In the course
so far we have used "boxes" to describe variables, and we can imagine a list as
a "box of boxes". In this analogy, Python will store the memory locations for
each side of the box where the list begins and ends:

```
    |----|----|----|
    | 03 | 07 | 42 |
    |----|----|----|
    ^              ^
    |              |
  start           end
```

If we want to get the first value of from the list, we need to get the box that
starts at `start`, whereas if we want to get the second element we need to go
one box past `start`, and if we want to get the third element we have to go two
elements past `start`.

If you don't understand this don't worry yet; just make sure you remember that
we have to start at zero. Also recall that floor numbering in buildings (in the
UK) works in exactly the same way.

### Joining lists

Just like strings, we can add two lists together:

```python
committee = ['matt', 'chris', 'thomas']
volunteers = ['nick', 'sauyon', 'calin']
helpers = committee + volunteers
for person in helpers:
    print(person)
```

### Appending to lists

If we want to add a value to the end of a list we could do `list + [x]`, but
this creates a new list; we might want to add to an existing list instead:

```python
committee = ['matt', 'chris']
committee.append('thomas')
for person in committee:
    print(person)
# Prints matt, chris, thomas
```

This doesn't create a new list, but adds an extra value into the existing list.

### Inserting into lists

We can also pick a specific index for a new element to be inserted at:

```python
committee = ['matt', 'thomas']
committee.insert(1, 'chris')
# committee now contains matt, chris, thomas
```

The way to remember this is that the insertion index is new index of the value,
i.e. the number of values that will *precede* it in the list.

### Other list operations

Another core operation is finding the length of a list, because this doesn't
have to be fixed. We do this with `len(list)`. At this point we need to make an
important distinction between **functions** and **methods**. A method is a
function that always takes at least one parameter, the `self` object. For
example, the `insert` *method* on a list is effectively a `function` that takes
a list *and* an element to insert. Somewhere, it will actually be defined like
this:

```python
def insert(self, element):
    # Insert element into the list self
```

Meanwhile, `len` is defined as a function because we can use it on types other
than lists, e.g. strings and dictionaries - it isn't associated with one
specific type (there is more to the reasoning here, we won't worry about it now).

Another common function is `sorted`, which takes a list and gives us back a new
list in sorted order. Alternatively, we can sort a list without having to create
a new list: `list.sort()

We will look at methods in far more detail next week.

To get the last element in a list, we could do `list[len(list) - 1]` but Python
provides some shorthand for this: `list[-1]`. I find the former a bit more
explicit, but you may prefer the latter.

### Exerise: Generating squares

```python
n = 0
try:
    n = int(input("Enter a number: "))
catch:
    print("You didn't enter a number")

squares = []

for x in range(0, n):
    squares.append(x * x)

for sq in squares:
    print(sq)
```

### Exercise: Finding the median from a dataset

```python
numbers = []
x = None
while x != "done":
    x = input("Enter a number or done: ")
    try:
        # int() will throw an exception if the number isn't a number
        numbers.append(int(x))
    except:
        x = "done"

# Sort the list
numbers.sort()

if len(numbers) % 2 == 0: # Even length
    median = (numbers[len(numbers) // 2 - 1] + numbers[len(numbers) // 2]) / 2
else:
    median = numbers[len(numbers) // 2]

print("Median = {}".format(median))
```

## Dictionaries

We can view lists as a way of mapping between numbers and values of any type
(mathematicians: a list is a function of `f: N -> U` where `N` is the set of
natural numbers and `U` is the universe of all values representable in Python).
Dictionaries are the same concept, except they allow us to lookup an **element**
by a **key** of *any* type. For example:

```python
committee = { "president": "matt", "secretary": "thomas", "treasurer": "chris" }
print(committee["president"]) # prints matt
print(committee["secretary"]) # prints thomas
```

The analogy here is the OED: it maps strings (words) to strings (their
definitions). We can easily add values to a dictionary, reassign existing keys,
or remove keys from a dictionary:

```python
college = {} # Creates an empty collegeionary
# Add a few elements to the collegeionary:
college["catz"] = "St. Catherine's"
college["bnc"] = "Brasenose"
college["b"] = "Baliol"
# Oops, spelt that wrong
college["b"] = "Balliol"
# Delete an entry from a collegeionary
del college["b"]
print(college) # Only outputs entries for catz and bnc
```

The `del` keyword is neither a function nor a method, it is an operator. We will
not go into detail about why this is the case (yet).

### Exercise: Word counting

```python
text = input("Enter some text: ")
words = text.split(" ")
counts = {}

for word in words:
    if word in counts:
        counts[word] = counts[word] + 1
    else:
        counts[word] = 1

for word in counts:
    print("{}: {}".format(word, counts[word]))
```
