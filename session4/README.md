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
