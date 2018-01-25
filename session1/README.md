# Introduction to Python

The first thing that you’ll need to do is install Python installed on your
computer. You can find information on how to do that [here][install].

[install]: https://github.com/oxcompsoc/learntocode/tree/master/session0

Throughout these documents note that text in a `monospaced font` is Python code.

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

[replit]: repl.it/languages/python3

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
variable we just write its name - this is exactly the same as if we'd
written the value in the first place. The following program functions in exactly the same way as the first program we wrote

```python
message = "Hello, world!"
print(message)
```

## Functions

A function is a piece of code that is available to your program that can be
reused in different contexts. Functions are a little like sausage machines; you
can put beef in and get a beef sausage, you can put pork in and get a pork
sausage back, etc.

Some functions require you to provide **arguments** as an input to the function,
and some functions will also **return** a result back to you. We will see later
in the course how to define your own functions, but in this session we only
looked at the print and input functions. If we write `print("Hello, world!")`
then the text `"Hello world!"` will be "printed" on the screen. Alternatively,
if we write `name = input("What is your name?")` then we request show the user
the prompt, they get the chance to input some text, and that text will be
returned and assigned to the variable name.

## Writing scripts

In IDLE we can write script files, which contain a sequence of Python statements
that we can run over and over, without the need to keep typing in what we want
to do. To write a script, click File > New and enter a few statements:

```python
name = input("What is your name?")
print("Hello, " + name)
```

You then need to save the file somewhere sensible with the .py extension before
you can run it (either Run > Run Module, or F5). The program’s output will be
shown in the main Python window.

## If statements

The programs we have seen so far do approximately the same thing, so if
statements allow us to do different things based on whether certain conditions
hold. For example:

```python
name = input("What is your name?")
if name == "thomas":
    print("hey, you’re the best")
else:
    print("Shoo! Go away")
```

There are several important concepts to note here:

 * If we want to compare two values (e.g. the value the user entered and a fixed
   string) we use `==` instead of `=`
 * All the code that is directly below the if statement and has been indented
   right of it will be executed if the condition holds
 * We can add an else branch that is executed if the if statement didn’t hold
 * We can compare numbers and strings using the comparison operators `==`, `!=`,
   `<=`, `>=`, `<`, and `>`
 * If statements can be nested (we'll look at this more next week)
 * We will spend more time looking at what we can place in the condition of if
   statements next week

## Loops

**N.B.** Matt’s group had a slightly longer session this week, whereas Thomas'
group didn't get onto these. Regardless of which group you are in we’ll be doing
these next week.

A horribly inefficient way to write a program that has to do the same thing a
few times would be to copy and paste the code a few times. Instead we use loops
to allow us to run a piece of code many, or infinite times.

```python
for x in range(1, 10):
    print(x)
```

This program outputs:

```
1
2
3
4
5
6
7
8
9
10
```

## Good resources to look at

 * [Khanacademy][] - good for learning about computer science and computational
   thinking

 * [Codecademy][] - excellent introductory courses in different programming
   languages. Note that they currently use Python 2.x, whereas we are using
   Python 3.x

 * [Project Euler][euler] - programming challenges, probably a good place to
   practice after a couple of weeks

[khanacademy]: http://khanacademy.org
[codecademy]: http://codecademy.com
[euler]: http://projecteuler.net

## Challenges

These challenges are entirely optional, and you are more than welcome to do as
few or as many as you like. They are designed around the lecture material, but
will hopefully give you the chance to extend your knowledge a little further.

 * **Mixing strings and numbers:** During the sessions we only concatenated
   (i.e.  added) two strings together, but how do we add a number to a string?
   You may want to look up the str function
 * **A simple quiz game:** multiple questions, possibly multiple choice
   questions, keep track of the number of correct answers and output it at the
   end
 * **Number doubling:** Consider the following program, and correct it so that
   the number that is printed at the end is actually the number that the user
   input. How could you deal with input that is not a number?


```python
# Run this program and see what it outputs
x = input("Enter a number ")
print(x * 2)
```

 * **Number guessing game:** The program has a number, and the user has to guess
   what the number is. The program should respond whether either higher or lower
   as appropriate, or terminate if the user successfully guesses the number. Can
   you generate a random number each time the game is played? You may want to
   look up how to use random.random and while loops (covered next week)
 * **Computer number guessing game:** rather than have you guess the number,
   have the computer try and determine it instead. How can you ensure that the
   computer makes as few guesses as possible?
