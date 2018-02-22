# Session 5: Dictionaries, stacks, and where to go next

You can find the resources for last week's session [here][s4notes].

In this week's session we are going to continue looking at dictionaries, a
common Python data structure introduced at the end of last week's session. Once
we've spent a little more time working through an exercise with dictionaries
we'll move on to seeing how we can use a list as a stack, which are useful
tools in a broad variety of problems. Stacks are oen of the most important data
structures in the execution of any programming language.

Finally, we'll take a look at other places that the knowledge that you've
gained from Python can be applied, such as data processing, machine learning,
and image recognition.

[s4notes]: https://github.com/oxcompsoc/learntocode/tree/master/session4/README.md

**The screencast for this week is [here][s5video].**

[s5video]: https://youtu.be/uDT3xMpaCKY

## Dictionaries

We [introduced dictionaries in last week's session][dictS4]. The idea behind a
dictionary is to map from a *key* to a *value*. There is no inherent order to a
dictionary, but it does allow us to *randomly access* values (i.e. we can
access elements in any order we like).

To create a empty dictionary, stored in the variable `d`, we write the following:

```python
d = {}
```

Then, to store a value `v` with key `k` we write `d[k] = v`; this is just like
arrays except that we are no longer restricted to using integers for the key,
and we don't need to 'append' to a dictionary; we just insert directly into it
instead.

Once a value `v` is stored at key `k` in `d` we can access it with `d[k]`. Note
that just as in the case of a list, a value can appear multiple times in a
dictionary but only one value can be associated with a key.

**Exercise:** how you can associate multiple values with the same key? What if
you aren't permitted duplicates?

Finally, we can iterate through all they **keys** of a dictionary with the following:

```python
d = {}
d["a"] = "Aardvark"
d["b"] = "Badger"
d["c"] = "Cat"

for k in d:
    print(k)
    
# prints:
# a
# b
# c
```

This could have alternatively been written:

```python
d = { "a" : "Aardvark", "b": "Badger", "c": "Cat" }

for k in d:
    print(k)
    
# prints:
# a
# b
# c
```

Then, if we want to print the values instead:

```python
d = { "a" : "Aardvark", "b": "Badger", "c": "Cat" }

for k in d:
    print(d[k])
    
# prints:
# Aardvark
# Badger
# Cat
```

Last week we introduced an [exercise][s4exercise] for counting which words
appear in a piece of text. You can find the [solution here][s4solution].

[dictS4]: https://github.com/oxcompsoc/learntocode/blob/master/session4/README.md#dictionaries
[s4exercise]: https://github.com/oxcompsoc/learntocode/tree/master/session4#dictionary-exercise
[s4solution]: https://github.com/oxcompsoc/learntocode/blob/master/session4/wc.py

We can use dictionaries to represent **graphs**. A graph is a collection of
**vertices** (also called **nodes**) connected by **edges** (i.e. arrows
between the vertices). For example, suppose we had the following graph:

![Graph](graph.png)

We can then use a dictionary to represent the arrows between nodes; the keys can be the names of nodes whilst the values they are associated with a list of nodes that the arrows point to:

```python
g = {
    "a": ["b", "d"],
    "b": ["c"],
    "c": ["f"],
    "d": ["e"],
    "e": ["b","f"],
    "f": []
}
```

**Exercise:** do we need to explicitly say that `"f"` maps to `[]`, i.e. that
it has no arrows coming out of it? Could we represent it another way?

**Exercise:** Implement a function that takes a graph and the names of two
nodes and determines if there is an edge from the first node to the second.

**Exercise:** Implement a function that determines if there is a path between
two nodes in a graph.

**Exercise:** Implement a function that determines the shortest path through a
graph (assuming each edge is the same length). For example, in the above we can
get from `"a"` to `"f"` via `["a", "b", "c", "f"]` or `["a", "d", "e", "b",
"c", "f"]`.

## Stacks

The third, and final, data structure that we are going to look at in this
course is actually one that we've seen before! A stack is just a literally a
list with two operations: *push*, which pushes an element on to the *top* of
the stack, and *pop* which removes the top element from the stack and returns
it. The analogy here is just a stack of plates.

For example, we declare an empty stack in exactly the same way that we declare
an empty list:

```python
stack = []
```

To push onto a stack, we just append to the end of the stack:

```python
stack.append(10)
stack.append(20)
```

The top of the stack is now `20`, which we can retrieve via popping it from the
top of the stack:

```python
x = stack.pop()
```

`x` is now `20`, and `stack` is now `[10]`.

## A stack machine

Stacks are useful in a broad variety of algorithms, but Python uses them
internally too. We are going to explore how to use stacks to implement a very
simple programming language that does basic calculations.

Suppose we are given the instruction sequence `[10, 20, "+"]`. We will
interpret this as:

* Push 10 onto a stack
* Push 20 onto a stack
* Pop the top two values from the stack, add them together, and then push the result back to the stack

It is reasonably easy to see that the end state of the stack is `[30]`.
Alternatively, suppose we are given a list of instructions `[1, 2, 3, "+",
"+"]`:

* Push 1 to the stack
* Push 2 to the stack
* Push 3 to the stack
* Pop the top two values (3, 2) and push the result (5) to the stack
* Pop the top two values (5, 1) and push the result (6) to the stack

The end result here is `[6]`.

Here's a simple implementation:

```python
instructions = [ 1, 2, 3, "+", "+" ]
stack = []

for instruction in instructions:
    if instruction == "+":
        x = stack.pop()
        y = stack.pop()
        stack.append(x + y) # Push the result
    else:
        stack.append(instruction) # This is just a number
        
print(stack)
```

**Exercise:** add support for other mathematical operations, such as
subtraction, multiplication, division, and powers.

Our instructions are written in [Reverse Polish Notation][rpn], which can
represent any expression that we would normally write using infix notation. For
example, the infix expression `d - ((a + b) * c)` is equivalently written as
the RPN expression `d a b + c * -`.

**Exercise:** how you can convert an expression written in infix notation into
one written in Reverse Polish Notation.

[rpn]: https://en.wikipedia.org/wiki/Reverse_Polish_notation

Internally Python takes *exactly* the same approach for computing expressions.
It also uses a stack for remembering the values of local variables inside
functions when you call another function.

## Where to go next

In this course we've only had the opportunity to scrape the surface of what you
can do with Python. We've compiled a collection of other sites and resources
that we think are useful as stepping stones.

### Learning more Python

* [Python documentation](https://docs.python.org/3/)
* [Official Python tutorial](https://docs.python.org/3/tutorial/index.html)
* [Learn Python the Hard Way](https://www.learnpythonthehardway.org)
* [Codecademy](https://www.codecademy.com/catalog/language/python)

### Programming challenges and exercises

* [Project Euler](https://projecteuler.net) - tend to be a bit more mathematical
* [HackerRank](https://www.hackerrank.com) - beginner to advanced exercises

### Computer Science concepts

* [Khan Academy Computer Science](https://www.khanacademy.org/computing/computer-science)
* [MIT Open Courseware: Introduction to Computer Science and Programming in Python](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/index.htm)
* [MIT Open Courseware: Introduction to Computational Thinking and Data Science](https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-0002-introduction-to-computational-thinking-and-data-science-fall-2016/index.htm) - note that this is a successor to the above

### Processing data and scientific problems

* [Coursera/Nanjing University: Data Processing Using Python](https://www.coursera.org/learn/python-data-processing)
* [Pandas (Python Data Analysis Library)](https://pandas.pydata.org)
* [NumPy](http://www.numpy.org)
* [SciPy](https://www.scipy.org)
* [Python CSV processing](https://docs.python.org/3/library/csv.html)

### Machine Learning

Although we haven't (yet) covered machine learning in the Learn to Code course,
but Python is widely popular in ML.

You can probably implement straightforward problems like [linear
regression][linreg] with the Python knowledge that you have so far (provided
that you've seen some linear algebra before).

[linreg]: https://en.wikipedia.org/wiki/Linear_regression 

You might want to take a look at [Applied Machine Learning in
Python](https://www.coursera.org/learn/python-machine-learning) on Coursera.

One of the most popular machine libraries for neural networks,
[TensorFlow](https://www.tensorflow.org), is written by Google and freely
available. Alternatively, you might like to look at [Keras](https://keras.io),
which avoids some of TensorFlow's complexity.

### Image Recognition

[OpenCV][] is the leader here. With a bit more time we might cover this in a
future course.

[OpenCV]: https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html

### Other programming languages

Python has a fairly simple syntax, and aside from its wide applicability in a
broad range of fields, that is one of the main reasons we taught the course
using it. The following are useful resources for a broad range of topics,
including web development:

* [Khan Academy (general)](https://www.khanacademy.org/computing/computer-programming)
* [Codecademy (general)](https://www.codecademy.com)

### CompSoc and other Oxford societies

[CompSoc][] itself regularly hosts coding challenges, Geek Nights, and talks
from leading industry partners that are working at the forefront of technology.
Everyone is welcome at our events, and they are always a good opportunity to
chat to people with experience across computer science.

[CodeSoc][] also host a borad variety of introductory programming events, and
[Oxford Women in Computer Science][oxwocs] host a number of technical talks and
events.

[CompSoc]: https://www.facebook.com/oxcompsoc/
[CodeSoc]: https://www.facebook.com/groups/108792712905292/?ref=br_rs
[oxwocs]: https://www.facebook.com/OxWoCS/
