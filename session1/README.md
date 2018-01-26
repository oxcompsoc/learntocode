# Introduction to Python

The first thing that you’ll need to do is install Python installed on your
computer. You can find information on how to do that [here][install].

[install]: https://github.com/oxcompsoc/learntocode/tree/master/session0

Throughout these documents note that text in a `monospaced font` is Python code.

**If you missed this session or you want a recap, you can watch the screencast
from this session [here][video].**

[video]: https://youtu.be/yAzp_pRXVPg

## Information about CompSoc

The [Oxford University Computer Society][compsoc] was founded in 1978, making
it one of the oldest university computing societies in the country. Today we
host regular talks from large companies, geek nights each Saturday, and Learn
to Code each Hilary Term. Later this term we'll be celebrating our 40th
anniversary with a dinner welcoming back former members.

[compsoc]: https://ox.compsoc.net

## IDLE

Once you have Python installed you’ll be able to launch a piece of software
called IDLE. When you first launch it you will be greeted with a prompt where
you can type in statements or expressions in Python. In these sessions we will
not be using the prompt, so instead create a new file (**File > New File**).

### Problems installing Python or using IDLE

If you can't get Python installed on your computer, don't worry! Instead,
please go to [this website][replit], which allows you to run Python programs
online. All our examples (until the final session) should run fine in either
the online version or IDLE.

[replit]: http://repl.it/languages/python3

## Hello, world

The programs that we are going to be writing in this course will all be
text-based, i.e. they can take text that you enter as input and produce text as
output. Although this might seem limited in the age of animated, interactive
apps they provide us with a strong foundation for programming.

One of the most basic programs we can write is one that just outputs some text.
In a new file in IDLE (or empty editor on `repl.it`) enter the following Python
program:

```python
print("Hello, world!")
```

In IDLE, then click **Run > Run Module** (or F5) or click the run button on
`repl.it`. IDLE will then run the program in the prompt window, and you should
see the output `"Hello, world!"`.

There are three elements to consider here:

* `print` is the name of a **function**. Functions are pieces of code that do
  something and/or calculate something. The `print` function outputs text
  (historically, the some of the earliest computers used physical printers as
  their primary form of output)
* `( )` (parentheses) are used to indicate that we are **calling** the function
  `print`, i.e. that we are telling Python to execute the `print` function
* `"Hello, world!"` is the **argument** to the function `print`, i.e. the text
  that we would like the code inside the `print` function to output. You'll
  notice that when the text is printed the quote marks are missing -
  this is because we have to indicate to Python that the argument is text,
  rather than other symbols. We call text that appears in programs like this
  **strings**

## Strings

We called `"Hello, world!"` a **string**, i.e. a piece of text that appears in
our source code that we can either print or manipulate. One such example is
that we can split this string in two:

```python
print("Hello, " + "world!")
```

Here Python will join (`+`) the two strings together to form one string that is
then given to the `print` function.

**Exercise:** there are many other ways to manipulate strings in Python.
Investigate how to multiply a string or convert it to uppercase/lowercase.

## Variables

Python programs store data in **variables**. There are two analogies that we
like to use:

* A variable is a bit like a box that has a name, and inside the box we can
  store values
* Python maintains a *dictionary* of names that map to definitions

For now, we can consider these equivalent.

To assign a value to a variable we write `name = value` where `name` can be
replaced with any piece of text that Python allows as a variable name
(**Exercise:** investigate what Python does and doesn't allow) and `value` can
be replaced with any Python value. Then, to get the value associated with a
variable we just write its name - this is exactly the same as if we'd written
the value in the first place. The following program functions in exactly the
same way as the first program we wrote

```python
message = "Hello, world!"
print(message)
```

## Functions

A function is a piece of code that is available to your program that can be
reused in different contexts. We've already seen the example of the `print`
function, which outputs text to the user. Next, we're going to see the `input`
function, which receives text from the user:

```python
message = input("Enter a message: ")
print("Your message was " + message)
```

The `input` function takes an argument that is output to the user, just like
the `print` function. It then waits for the user to enter some text and press
enter, and **returns** this value, which we then store in the variable called
`message`, after which the program behaves similarly to before.

## If statements

Our programs so far have done exactly the same thing each time we run them,
unless we enter different text. However, we can easily get the program to
behave differently each time we run it. In Python we can write statements that
do

> if "this condition is true" then "execute this code"

We write the above as:

```python
if condition_is_true:
    execute_this_code
```

Notice that we write "then" as `:`. The most important thing to notice is that
the code we want to execute *only* when the condition holds As a more concrete
example, consider the following program:

```python
answer = input("What gets wetter the more it dries?")
if answer == "towel":
    print("You answered the riddle correctly")
```

We can write any number of statements inside the **body** of the `if`
statement, i.e. statements that are intended (press `TAB`) will only be
executed if they the condition of the `if` statement holds.

We can also optionally include an `else` branch on the `if` statement that will only be executed if the condition doesn't hold:

```python
if condition_is_true:
    execute_this_code
else:
    this_code_is_executed_otherwise
```

There are several important concepts to note here:

 * If we want to compare two values (e.g. the value the user entered and a fixed
   string) we use `==` instead of `=`
 * We can compare numbers and strings using the comparison operators `==`, `!=`,
   `<=`, `>=`, `<`, and `>`
 * If statements can be nested (we'll look at this more next week)
 * We will spend more time looking at what we can place in the condition of if
   statements next week

We can also abbreviate the following:

```python
if condition_is_true:
    execute_this_code
else:
    if this_other_condition_is_true:
        execute_this_other_code
    else:
        do_this_if_no_conditions_hold
```

to

```python
if condition_is_true:
    execute_this_code
elif this_other_condition_is_true:
    execute_this_other_code
else:
    do_this_if_no_conditions_hold
```

You can have as many `elif` branches as you like, but only one `if` branch and
one `else` branch, which must appear at the beginning and end respectively.

## For loops

A for loop is a bit like a while loop, except that we can execute the body many
times.

```python
for n in range(lower_bound, upper_bound):
    print(str(n))
```

This program will print the numbers `lower_bound <= n < upper_bound`.

## Guessing game

In the Lecture Theatre A session we wrote the following code:

```python
import random

for n in range(0, 10):
    answer = random.randint(0, 1000)
    guess = int(input("Guess: "))
    if guess < answer:
        print("Too low!")
    elif guess == answer:
        print("Correct, you got " + str(answer))
        break
    else:
        print("Too high")
```


## Good resources to look at

 * [Khanacademy][] - good for learning about computer science and computational
   thinking

 * [Codecademy][] - excellent introductory courses in different programming
   languages. Note that they currently use Python 2.x, whereas we are using
   Python 3.x

 * [Project Euler][euler] - programming challenges, probably a good place to
   practice after a couple of weeks

 * [Learn Python the Hard Way](https://learnpythonthehardway.org/python3/)

[khanacademy]: http://khanacademy.org
[codecademy]: http://codecademy.com
[euler]: http://projecteuler.net

## Exercise

 * **Computer number guessing game:** rather than have you guess the number,
   have the computer try and determine it instead. How can you ensure that the
   computer makes as few guesses as possible?
