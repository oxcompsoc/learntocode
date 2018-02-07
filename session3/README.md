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

## Exercises

For today's session we have a large number of different exercises that you can
choose from. At the end of the session we'll go through solutions for a few of
them (the remainder will be released as part of the screencast). They are
roughly ordered by difficulty. If you find an exercise easy, consider skipping
a few.

Each exercise has some tests associated with it so you can test your solution.
To run the tests, download the associated file, open it in IDLE, and edit the
function at the top.

### Exercise 1: Summing a list

Write a function `sum` that takes a list of numbers and returns the sum of all
the numbers in the list.

```python
def sum(xs):
    # return the sum of all the elements in the list xs
```

[Download Test Cases][exercise1]

### Exercise 2: Product of a list

Write a function `product` that takes a list of numbers and returns the product of all the numbers in the list.

```python
def product(xs)
    # return the product of all the elements in the list xs
```

[Download Test Cases][exercise2]

**Exercise (not party of the tests):** what should the product of the empty list be?

**Exercise:** can you optimise this if you find a zero in the list?

### Exercise 3: Mean of a list

```python
def mean(xs):
    # return the mean of all the elements in the list xs
```

[Download Test Cases][exercise3]


### Exercise 4: Flattening lists

Lists can contain lists, so take a list `[ [ a, b, c, ... ], [ d, e, f, ... ],
... ]` and flatten it to `[ a, b, c, ... , d, e, f, ... ]`.

```python
def flatten(xs):
    # return a flatted copy of xs
```

**Hint:** The code for this is *almost* exactly the same as one of the earlier exercises.

**Hint:*** The empty list is `[]`

[Download Test Cases][exercise4]

### Exercise 5: Pairwise sum

Given two lists `xs` and `ys`, return a new list `zs` where each element is the
sum of the corresponding elements in `xs` and `ys`, i.e. `sum2([1, 2, 3], [10,
11, 12]) == [11, 13, 15]`. You may assume that the lists are the same length.

```python
def sum2(xs, ys):
    # return a list pairwise summing the elements
```

[Download Test Cases][exercise5]

### Exercise 6: Pairwise sum

This is exactly the same as the previous exercise, only you may not assume that
the lists are of the same length. The list returned should be the length of the
longer list, as if the remainder of the shorter list were zeroes. For example,
`sum2([1, 2], [1, 2, 3, 4]) == [2, 4, 3, 4]`.

```python
def sum2(xs, ys):
	# pairwise sum assuming that xs and ys aren't the same length
```

[Download Test Cases][exercise6]

### Exercise 7: Divisibility

Given a number `n`, compute a list of all the integers `x` divisible by 3 or 5
that are `0 <= x < n`. For example, `three_or_five(10) == [0, 3, 5, 6, 9]`.

```python
def threes_or_fives(n):
	# return a list of all the integers greater than or equal to zero that are
	# divisible by three or five and less than n
	# You might want to look up the modulus (%) operator, which computes the
	# remainder of division
```

**Exercise:** See if you can combine this function with your solution to exercise 1 for solving the [first Project Euler problem][euler1].

[euler1]: https://projecteuler.net/problem=1

[Download Test Cases][exercise7]

### Exercise 8: Filtering a list

Given a list of numbers, return a copy of the list that only includes the even
numbers.

```python
def filtered_even(xs):
	# Return a copy of the list that only includes even numbers
```

[Download Test Cases][exercise8]

### Exercise 9: Filtering a list of strings

Given a list of strings, return a copy of the list that only includes the strings that start with an lowercase letter.

```python
def filtered_text(xs):
	# Return a copy of xs that only contains the strings that start with a
	# lowercase letter
```

**Hint:** you can treat strings like lists, so to get the first character of a
string you can do `s[0]` where `s` is a string variable.

**Hint:** you can compare characters to other characters, e.g. `"a" <= "b"` is `True` but `"a" >= "z"` is `False`; you need to include the quote marks around the character still.

[Download Test Cases][exercise9]

### Exercise 10: Rotating a list

Given a list `xs` and an integer `n`, produce a list where each element is
rotated around by `n`, i.e. `rot([1, 2, 3], 1) == [3, 1, 2]` and `rot([1, 2, 3,
4, 5], 2) == [3, 4, 5, 1, 2]`.

```python
def rot(xs, n):
	# return a list of xs rotated by n
```

[Download Test Cases][exercise10]

[exercise1]: https://raw.githubusercontent.com/oxcompsoc/learntocode/master/session3/exercise1.py
[exercise2]: https://raw.githubusercontent.com/oxcompsoc/learntocode/master/session3/exercise2.py
[exercise3]: https://raw.githubusercontent.com/oxcompsoc/learntocode/master/session3/exercise3.py
[exercise4]: https://raw.githubusercontent.com/oxcompsoc/learntocode/master/session3/exercise4.py
[exercise5]: https://raw.githubusercontent.com/oxcompsoc/learntocode/master/session3/exercise5.py
[exercise6]: https://raw.githubusercontent.com/oxcompsoc/learntocode/master/session3/exercise6.py
[exercise7]: https://raw.githubusercontent.com/oxcompsoc/learntocode/master/session3/exercise7.py
[exercise8]: https://raw.githubusercontent.com/oxcompsoc/learntocode/master/session3/exercise8.py
[exercise9]: https://raw.githubusercontent.com/oxcompsoc/learntocode/master/session3/exercise9.py
[exercise10]: https://raw.githubusercontent.com/oxcompsoc/learntocode/master/session3/exercise10.py
