# Session 3: Lists(cont), for loops and intro to functions

See [here][s2notes] for last week's content.

[s2notes]: https://github.com/oxcompsoc/learntocode/tree/master/session2

**You can find all the [solutions here][solutions].**

[solutions]: https://raw.githubusercontent.com/oxcompsoc/learntocode/master/session3/solutions.py

## Recap

In the previous session we covered the following concepts:

```python
# Any text after a '#' symbol on a line is a comment. It is not part of the code.

# Password checker using while loops:
SECRET_PASSWORD = "pass123"
user_input = input("Please enter a password: ")

while user_input != SECRET_PASSWORD:
  print("Access denied: wrong password.")
  print() # Print a newline. This is just here to make things look nicer.
  user_input = input("Please enter the password: ")

print("Access granted.")


# Incrementing and other syntactic sugar. The shorthands for the following:
number = number + 1
number = number - 1
number = number * 2
number = number / 3

# are respectively:

number += 1     # Equivalent to saying "increase number by 1", i.e. increment it
number -= 1     # Equivalent to saying "decrement number by 1", i.e. decrement it
number *= 2     # Equivalent to saying "number becomes itself times 2"
number /= 3     # Equivalent to saying "number becomes itself divided by 3"


# Counting using while loops:

n = int(input("Please enter a number: "))
i = 1
while i <= n:
  print(i)
  i += 1 # Increment i (i becomes bigger by 1).

# Finding the sum of the first n natural numbers:
n = int(input("Please enter a number: "))
i = 1
sum = 0
while i <= n:
  sum += i
  i += 1

print("The sum of the first " + str(n) + " natural numbers is " + str(sum))

```

## Lists revisited and continued

Let's have a quick revisit of lists. Here's the example list we had last time:

```python
shopping_list = [ "bread", "smoked salmon", "cherry tomatoes", "cream cheese" ]
```

The `len` function tells us the length of a list:

```python
number_of_items = len(shopping_list) # number_of_items = 4
```

We can access a particular element of a list using **subscript notation**:

```python
item = shopping_list[0] # item is now "bread", Python lists start indexing at 0
item = shopping_list[1] # item is now "smoked salmon"

# We decided to get cheddar instead of cream chese so we can change the list like so:
shopping_list[3] = "cheddar" # The list is now [ "bread", "smoked salmon", "cherry tomatoes", "cheddar" ]
```

We can append an element to a list - basically adding it to the end:

```python
# We forgot to add mayo to the list so we can add it later like so:
shopping_list.append("mayo") # shopping_list is now [ "bread", "smoked salmon", "cherry tomatoes", "cheddar", "mayo" ]
```

Or remove an element from the list:

```python
del shopping_list[4] # shopping_list is now [ "bread", "smoked salmon", "cherry tomatoes", "cheddar" ]
```

Alternatively, you can remove an element by value, so instead of the previous
line we could have written:

```python
shopping_list.remove("mayo")
```

Do note that this is more computationally expensive because the computer needs to go through the entire list to find the mayo, similarly to how you would go down a list from the start to find it.

You can also join two lists together:

```python
shopping_page1 = ["bread", "smoked salmon", "cherry tomatoes"]
shopping_page2 = ["cheddar", "mayo" ]
shopping_list = shopping_page1 + shopping_page2 # shopping_list is now [ "bread", "smoked salmon", "cherry tomatoes", "cheddar", "mayo" ]
```

**Note:** you may have seen what Python calls lists called *arrays* in other programming languages. In most programming languages [there is a difference][listvsarray] but it is not relevant to Python or this course.

[listvsarray]: https://www.quora.com/What-is-the-difference-between-an-array-a-list-and-a-linked-list/answer/Gregory-Schoenmakers?share=ccf41042&srid=RsVE

## For loops

We've already covered `while` loops but there is another type of loop that lets us execute a piece of code multiple times. Remember the example for counting using `while` loops:

```python
n = int(input("Please enter a number: "))
i = 1
while i < n:
    print(i)
    i += 1 # Increment i (i becomes bigger by 1).
```

Here's the same program written using a `for` loop:

```python
n = int(input("Please enter a number: "))
for i in range(1, n):
    print(i)
```

In general you write a `for` loop like so:
```python
for i in range(a, b):
    # block of code - this block will repeat (b - a) times and you will
    # have access to the number of the current "repeat" with i
```

As you can see `for` loops take care of a lot of things for us - you don't have to define your own `i` and increment it yourself. On the other hand, that makes `for` loops less flexible - there are some cases where you might not want to have a counter or you might want to decrement it.

What `for` loops are really useful for is *iterating* over lists. Here's an example:

```python
shopping_list = [ "bread", "smoked salmon", "cherry tomatoes", "cream cheese" ]
for item in shopping_list:
    print("I need to buy " + item)

# This will print out:
# I need to buy bread
# I need to buy smoked salmon
# I need to buy cherry tomatoes
# I need to buy cream cheese
```

We can write an equivalent program with `range` too:

```python
shopping_list = [ "bread", "smoked salmon", "cherry tomatoes", "cream cheese" ]
for i in range(0, len(shopping_list)):
    print("I need to buy " + shopping_list[i])

# This will print out:
# I need to buy bread
# I need to buy smoked salmon
# I need to buy cherry tomatoes
# I need to buy cream cheese
```

This gives us an insight as to what `range(a, b)` does - it's a function (we'll get to what that means later) that is equivalent to writing `[a, a + 1, a + 2, ..., b - 2, b - 1]` so we were iterating over lists all along.

## Exercises

What we'll do next is finish up the exercises from last session. You can find them [here](https://github.com/oxcompsoc/learntocode/tree/master/session2#Exercises-1). If you've already completed the exercises then try to replace your uses of `while` with equivalent `for` loops. There are some exercises where that is impossible which will give you a good idea of the limitations of `for`.

## Functions

Until now we've been putting our code all in one place. This is fine for small toy programs but if we want to write something bigger it becomes incredibly difficult to follow. This is where the idea of functions comes in - they're basically mini programs that you can run or *call* in your *main* one that provide us with various advantages. In order to understand them we must first see how functions work in practice. Here's a few examples:

```python
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
```

 1. We *define* a function with `def`.
 2. We follow that with the function *name*.
 3. Next we have a pair of parentheses in which we list the *arguments* to the function - these are equivalent to the *x* and *y* you might be familiar with from functions in Maths. We can have as many arguments as we want and inside the function they're treated as variables with some value already stored in them.
 4. After the parentheses we have a colon signifying that what follows is an indented block, similar to what we have for loops.
 5. That block is where we write our "mini-program", also known as the *body* of our function. Inside the body we may have the `return` keyword - this signifies the end of a function and whatever is right of `return` will be the *return statement* of the function - think of it as the thing that replaces the function at the place where it was called. A function that doesn't end up calling `return` automatically returns `None` which is a special value with type `NoneType`.

**Note:** You could have multiple return statements in a function - consider using an `if`/`else` to return different values depending on some condition. You should try to keep the type of all return statements in a function the same because otherwise you might get type errors. Consider the example:

```python

def getShapeArea(shape_name, x, y):
    if shape_name == "rectangle":
        return x * y
    elif shape_name == "triangle":
        return x * y / 2

if getShapeArea("rectangle", 5, 10) > getShapeArea("tringle", 5, 10): # typo intentional
    print("The rectangle has a larger area")
```

Here a typo in the name of the shape can result in `getShapeArea` not returning anything which has type `NoneType` and you can't compare `NoneType` with `int`, causing an error.

Back to the usefulness of functions - they let us do 4 useful things:
 - We can split our code into multiple chunks that are easier to reason about. Otherwise big programs would become one big chunk of code that would be incredibly difficult to understand.
 - A useful property of functions is that they can also call functions. They can even call themselves. This is known as recursion and, sadly, it is outside of the scope of this course but is so useful that some other programming languages have completely removed loops in favour of recursion.
 - On a similar note, when getting errors Python gives us a very convenient *call stack* - basically a list of all the functions that were called but haven't ended when we get the error. This makes tracking down bugs far easier.
 - We can reuse functions as many times as we want, reducing code repetition

A good rule of thumb is to keep functions below 200 lines of code. This includes the *main* function (i.e. the non-indented code). Anything larger should be split up into multiple functions.

## Exercises

For today's session we have a large number of different exercises that you can
choose from. They are roughly ordered by difficulty. If you find an exercise easy, consider skipping a few. It is somewhat difficult to finish most of them by the end of the session so we'll begin the next session with some exercise time as well after the recap. We would also encourage doing some of the exercises at home. In that case you could check the `solutions.py` file and the recordings from a previous run of the course [here](https://www.youtube.com/watch?v=TU1aisio7IU).

Each exercise has some tests associated with it so you can test your solution. To run the tests, download the associated file, open it in IDLE, and edit the function at the top. An example of how to do exercise 1 will be shown during the lecture.

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

**Exercise (not part of the tests):** what should the product of the empty list be?

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
rotated around by `n`, i.e. `rot([1, 2, 3], 1) == [2, 3, 1]` and `rot([1, 2, 3,
4, 5], 2) == [3, 4, 5, 1, 2]`.

```python
def rot(xs, n):
	# return a list of xs rotated by n
```

[Download Test Cases][exercise10]

## Sorting lists

For the second set of the exercises you'll need to be able to sort a list into
ascending order. To do this in Python you need to use the `sorted` function:

```python
beatles = [ "John", "Paul", "George", "Ringo" ]
beatles2 = sorted(beatles) # == [ "George", "John", "Paul", "Ringo" ]

nums = [13, 56, 26, 2, 12, 12, 2, 4]
nums2 = sorted(nums) # == [2, 2, 4, 12, 12, 13, 26, 56]
```

### Exercise 11: Removing duplicates

Given a list `xs`, return a new sorted list with all the duplicate elements
removed.

```python
def uniques(xs):
	# return a list of all the unique elements
```

[Download Test Cases][exercise11]

### Exercise 12: Binary search

**Note:** This exercise is harder than the others.

This exercise requires you to adapt the [binary search algorithm][binsearch]
seen last week. Given a sorted list of strings, find the least index of an
element with that value. One way we could do this is:

[binsearch]: https://github.com/oxcompsoc/learntocode/tree/master/session2#binary-search-algorithm

```python
def search(xs, x):
    for i in range(0, len(xs)):
        if xs[i] == x:
            return i
    return None
```

However, this isn't particularly efficient. The binary search reduces the
number of comparisons we have to do from `len(xs)` to `log2(len(xs))` where
`log2` is the base 2 logarithm.

```python
def bin_search(xs, x):
    # return the least index of an element equal to x in the sorted list xs
```

**Note:** don't worry about what you return if the item isn't in the list.
Often when implementing binary search it is useful to return the index that an
element *would* be at, *were* it in the list (i.e. so it could be inserted
whilst keeping the list in sorted order).

[Download Test Cases][exercise12]

### Exercise 13: Merging lists

Given two sorted lists, return a sorted list containing the contents of the two
lists merged in order, i.e. `merge([0, 1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5, 6])
== [0, 1, 1, 1, 2, 2, 3, 3, 4, 5, 6, 8]`. You should not assume that the lists
are the same length.

```python
def merge(xs, ys):
    # return a sorted list with the merged contents of the sorted lists xs and ys
```

[Download Test Cases][exercise13]

### Exercise 14: Merge sort

[Merge sort][mergesort] is a common sorting algorithm, and you can implement it
using the merge function from the previous exercise. The result of this
function should be the same as the result of the `sorted` function:

```python
def merge_sort(xs):
    # A sorted copy of xs
```

[Download Test Cases][exercise14]

**Hint:** In Python, if you want to split an array in two you can do:

```python
first_half = xs[:(len(xs) // 2)]
second_half = xs[(len(xs) // 2):]
```

[mergesort]: https://en.wikipedia.org/wiki/Merge_sort

## Mathematical exercises

The remainder of the exercises are intended for maths students or those that
have studied maths at some point (A-Level Core Maths should be enough).

### Exercise 15: Representing polynomials

For the next few exercises we will represent polynomials with a list, where
each element of the list represents the corresponding coefficient of `x`. For
example, the list `[1, 2, 3, 4]` represents the polynomial `1x^0 + 2x^2 + 3x^3
+ 4x^4 = 1 + 2x^2 + 3x^3 + 4x^4`.

In this exercise you should just write a function that takes a polynomial
represented in this way and outputs the equivalent equation, as above.

Can you make this nicer by not printing a term if the coefficient is zero?

**Note:** This exercise doesn't come with a test case; the intention is that
you write some code that you can use later for debugging. If you get stuck
however, the solution is [here][exercise15].

### Exercise 16: Adding polynomials

Given two lists that represent a polynomial, return a new list that represents
the polynomial that is the sum of those polynomial. For example, `poly_sum([1,
2, 3], [4, 5, 6]) = [5, 7, 9]` because `(1 + 2x + 3x^2) + (4 + 5x + 6x^2) = 5 +
7x + 9x^2`. Be careful to consider the result of adding two polynomials of
different degrees.

```python
def poly_sum(xs, ys):
    # return the list representing the sum of the polynomials represented by the
    # lists xs and ys
```

[Download Test Cases][exercise16]

**Hint:** This is *exactly* the same as one of the earlier exercises.

### Exercise 17: Multiplying polynomials

Given two lists that represent a polynomial, return a new list representing the
product of those two polynomials. For example, `(1 + x)(2 + x) = 2 + 3x + x^2`,
so we want `poly_prod([1, 1], [2, 1]) == [2, 3, 1]`.

```python
def poly_prod(xs, ys):
    # return the list representing the product of the polynomials represented by
    # the lists xs and ys
```

[Download Test Cases][exercise17]

**Hint:** you can create a list of `0`s of length `n` in Python with `[0] * n`.

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
[exercise11]: https://raw.githubusercontent.com/oxcompsoc/learntocode/master/session3/exercise11.py
[exercise12]: https://raw.githubusercontent.com/oxcompsoc/learntocode/master/session3/exercise12.py
[exercise13]: https://raw.githubusercontent.com/oxcompsoc/learntocode/master/session3/exercise13.py
[exercise14]: https://raw.githubusercontent.com/oxcompsoc/learntocode/master/session3/exercise14.py
[exercise15]: https://raw.githubusercontent.com/oxcompsoc/learntocode/master/session3/exercise15.py
[exercise16]: https://raw.githubusercontent.com/oxcompsoc/learntocode/master/session3/exercise16.py
[exercise17]: https://raw.githubusercontent.com/oxcompsoc/learntocode/master/session3/exercise17.py
