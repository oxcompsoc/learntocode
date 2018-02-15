# Session 4: Lists (cont.) and Dictionaries

In [last week's session][s3notes] we took a look at *lists*, which are ordered
collections of Python values. We saw that if we could create an empty list
called `xs` (pronounced "exes", i.e. the plural of a single "x") with

```python
xs = []
```

Alternatively, we could initialise `xs` to contain some values:

```python
xs = [ "Anything", "Can", "Go", "Here" ]
```

We also saw that we can access individual elements of a list with *subscription
notation*, and that the first element of a list is indexed by `0`:

```python
#      0           1      2     3
xs = [ "Anything", "Can", "Go", "Here" ]
first_element = xs[0] # has value "Anything"
last_element = xs[3] # has value "Here"
```

[s3notes]: https://github.com/oxcompsoc/learntocode/tree/master/session3

In today's session we are going to continue looking at lists by continuing with
some of the exercises from last week's session (we deliberately wrote far too
many for a single session). As we covered solutions to the first three
exercises in last week's session, we'd like to encourage you to start at
[exercise 4][s3e4].

[s3e4]: https://github.com/oxcompsoc/learntocode/tree/master/session3#exercise-4-flattening-lists

If you get stuck, as well as asking a volunteer for help, you can also look at
[last week's solutions][s3solutions] and [last week's video][s3video].

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
d = {}
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
of a dictionary variable, and `k` is a key.

Dictionaries, like lists, are incredibly important data structures in Computer
Science because we can use them to model relations between sets. For example,
we can model a phone book with a dictionary:

```python
phone_book = { "+44 01865 ******": "Thomas", ... }
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

**Exercise:** Why should we represent phone numbers with strings? Why shouldn't
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
