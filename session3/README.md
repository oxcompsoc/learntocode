# Session 3: Lists

See [here][s2notes] for last week's content.

[s2notes]: https://github.com/oxcompsoc/learntocode/tree/master/session2

## Lists

So far we've seen two different *types* of values: strings (pieces of text) and
numbers. This week we're going to be looking at lists, which are lists of
values. Python denotes lists as `[ x, y, z, ...]`:

```python
beatles = [ "John", "Paul", "George", "Ringo" ]
```

You must surround the list by square brackets and comma separate values.

The `len` function tells us the length of a list:

```python
number_of_beatles = len(beatles) # number_of_beatles = 4
```

We can access a particular element of a list using **subscript notation**:

```python
beatle = beatles[0] # beatle is now "John", Python lists start numbering at 0
beatle = beatles[1] # beatle is now "Paul"

beatles[3] = "Ringo Starr" # The list is now [ "John", "Paul", "George", "Ringo Starr" ]
```

We can add an element to a list:

```python
# Pete Best was the original drummer before Ringo
beatles.append("Pete") # beatles is now [ "John", "Paul", "George", "Ringo Starr", "Pete"]
```

Or remove an element from the list:

```python
del beatles[4] # beatles is now [ "John", "Paul", "George", "Ringo Starr" ]
```

Alternatively, you can remove an element by value, so instead of the previous
line we could have written:

```python
beatles.remove("Pete")
```

**Exercise:** Investigate which is more efficient

You can also join two lists together:

```python
one_direction = ["Niall", "Liam", "Harry", "Louis"]
names = beatles + one_direction
```

Finally, we can also loop over lists:

```python
for name in names:
    print(name)
```

Which outputs the following:

```
John
Paul
George
Ringo Starr
Niall
Liam
Harry
Louis
```

You can also get the index simultaneously:

```python
for index, name in enumerate(names): 
    print(str(index) + ": " + name)
```

This outputs:

```
0: John
1: Paul
...
```

**Note:** you may have seen what Python calls lists called *arrays* in other
programming languages. In most programming languages [there is a
difference][listvsarray] but it is not relevant to Python or this course.

[listvsarray]: https://www.quora.com/What-is-the-difference-between-an-array-a-list-and-a-linked-list/answer/Gregory-Schoenmakers?share=ccf41042&srid=RsVE