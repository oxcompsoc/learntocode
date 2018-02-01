# Session 2

See [here][week1] for last week's content. Session 2 was on 1/2/18 (HT18 Thurs
week 3).

[week1]: https://github.com/oxcompsoc/learntocode/tree/master/session1

## Recap

We ended the last session with a simple guessing game where the computer picked
a random number and gave us feedback whether or not we were too low or too high:

```python
# Lines that start with a # are comments, and not Python code
# This line "imports" the random library, so it makes the functions
# from the random library available to us
import random

answer = random.randint(0, 999)

for n in range(0, 10):
    guess = int(input("Guess: "))
    if guess < answer:
        print("Too low!")
    elif guess == answer:
        print("Correct, you got " + str(answer))
        break
    else:
        print("Too high")
```

The [randint function is documented here][randint]. It takes two parameters,
`a` and `b`, and returns a random integer `x` that is `a <= x <= b`. The range
function, meanwhile, takes two parameters `a` and `b` and iterates through `a
<= n < b`. We give the user 10 guesses in total because each time the user
guesses they should be able to halve the range they know that `answer` occurs
in, and we have to halve 1000 10 times in order to reach one number.

[randint]: https://docs.python.org/3/library/random.html#random.randint

For the more mathematically minded, we want to reduce the range that we're
thinking about down to one number, so we could consider the number of times
that we have to double 1 in order to reach 1000. We can find this with
logarithms: `log2(1000) = 9.966...`. If we reach a non-integral number of
guesses **we must round up**.

### Feedback from the first session

* Emphasise creating new files rather than deleting existing code
* Demonstrate commenting out code, and the value of comments in general
* Cover for loop ranges again

## Binary search algorithm

In the next exercise we are going to invert the problem and write a program
that asks the user for feedback on whether they are too high or too low.

In the slides we saw that we could maintain a range of possible values of where
the number might be, and that we did this by recording the "lower bound" (that
the value is greater than or equal to) and an "upper bound" (that the value is
*strictly* less than). In order to halve the size of the range, we guess a
value halfway through, and then update the range based on whether the user
tells us the value is too high or less than or equal to the value.

```python
print("Please think of a number that is >= 0 and < 1000")

numberIsGeqTo = 0
numberIsLtThan = 1000

while numberIsGeqTo + 1 != numberIsLtThan:
    # We need to right // instead of / for integer division
    guess = (numberIsGeqTo + numberIsLtThan) // 2
    response = input("Is your number less than " + str(guess) + "? ")
    if response == "yes":
        numberIsLtThan = guess
    elif response == "no":
        numberIsGeqTo = guess

print("Your number is " + str(numberIsGeqTo))
```

We haven't seen non-integer (i.e. floating point, decimal) arithmetic so far,
but Python is a little awkward here — we have to specify that we want to do
integer division, which will round the result down. Alternatively, we could do
`int((numberIsGeqTo + numberIsLtThan) / 2)`.

A `while` loop is a little bit like an `if` statement and a little bit like a
`for` loop. Their general structure in Python is:

```python
while condition_is_true:
    execute_this_code
```

Firstly, Python will check whether the condition is true. In the above example,
it will therefore check `numberIsGeqTo + 1 != numberIsLtThan`, i.e. `0 + 1 !=
1000`, which evaluates to `True`. Seen as the condition is true, it will
execute the code inside the *body* of the loop (i.e. the intended code). Then,
like a `for` loop but unlike an `if` statement, it will then return to the top
and check the condition again. If the condition is `True` again then the body
of the loop will be executed again, and if not then it will continue with code
that appears after the `while` loop.

In our example, we terminate the loop when `numberIsGeqTo + 1 !=
numberIsLtThan` is `False`, i.e. when `numberIsGeqTo + 1 == numberIsLtThan`.
Seen as we are trying to find the number `x` that has the property
`numberIsGeqTo <= x < numberIsLtThan` this condition is sufficient for
termination.

## Functions

We can use functions to *abstract* pieces of code so that we can reuse them
with different values. As we've seen in the case of `print` and `input`,
functions take a set of parameters (which can be empty) and possibly return a
value.

For example, here is a simple Python function that doubles its input:

```python
def double(x):
    return x * 2
```

We can then call this function with any of the following:

```python
x = double(10)
y = double(x)
print(double(z))
```

**Exercise:** what does this function do when passed a string?

A Python function is declared with the `def` keyword (an abbreviation of
`definition`) and is followed by the name of the function and a list of its
parameters. When we call the function the code nested inside the function is
then executed with the parameters assigned the values that the function was
called with. The `return` keyword then takes a value and returns that result to
the code that called the function.

For example, consider the following code:

```python
def multiply(x, y):
    return x * y

def double(x):
    return multiply(2, x)

print(double(x))
```

The code is then executed as:

![Calls](calls.png)

## Recursion

So far we have seen functions calling other functions, but they can just as
easily call themselves. Consider the following code:

```python
def palindrome(n):
    if n == 0:
        print(n)
    else:
        print(n)
        palindrome(n - 1)
        print(n)
```

Note that just like the `print` function, `palindrome` doesn't return a value -
it just outputs values.

If we then run the program `palindrome(3)` the output will be

```
3
2
1
0
1
2
3
```

Recursive function definitions are really common in mathematics and computer
science, but we have to be careful. The following is a common definition for
the Fibonacci sequence:

![Fibonacci](fib.png)

We could then translate this to the following Python function:

```python
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
```

**Exercise:** Try printing out `fib(0), fib(1), ...` with a `for` loop. What do
you notice about the behaviour of the program as `n` starts to get large?
