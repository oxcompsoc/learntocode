# Session 2: While loops, functions, recursion

See [here][week1] for last week's content.

[week1]: https://github.com/oxcompsoc/learntocode/tree/master/session1

## Recap

In the previous session we used these concepts:
```python
# Any text after a '#' symbol on a line is a comment. It is not part of the code.

print("Hello, world!") # This is how we print.

message = "Hi!" # This is how we create variables.
print("The value of the variable is: " + message) # This is how we join strings.

name = input("Please enter you name: ") # This is how we ask for string inputs from our user.
number = int(input("Please enter a number: ")) # This is how we ask for int inputs.
# (Remember: ints are whole numbers [..., -2, -1, 0, 1, 2, ...])

print("The number times two is: " + str(number * 2)) # This is how we join strings with numbers.

# An if statement. Note the : and the == which is how we compare values for equality.
if number == 0:
  print("The number is zero.")
elif number >= 0 and number <= 9:
  print("The number is a positive single digit integer.")
elif number < 0:
  print("The number is negative.")
else:
  print("The number is larger than 10.")
```

## Functions

Last time we saw this example:

```python
name = input("Please enter your name: ")
print("Hi, " + name + "!")
```

Now, if we only had to say hi to one person, this would be fine. But if we want to do this multiple times, writing out `"Hi, " + name + "!"` each time might get laborious. The way we solve this is by using functions:

```python
def say_hi(name):
  print("Hi, " + name + "!")

name_of_person = input("Please enter your name: ")
say_hi(name_of_person)
```
If we run this program, we will see that it does exatly the same thing as before. However, instead of writing out the whole print statement each time, we could now do:

```python
say_hi("Mark")
say_hi("Johnny")
# etc.
```

If we wanted to, we could put the entire first program in a function:
```python
def hi_sequence():
  name = input("Please enter your name: ")
  print("Hi, " + name + "!")

hi_sequence()
```
Again, this is exatly the same as the first program. Hoever, now we can ask for a name multiple times by *calling* the `hi_sequence` function again and again.

So a **function** is a kind of like a mini-program, which we can execute as many time as we like within our big program. Each time we execute this mini-program, we say that we **call** the function.


Here are a few more examples of functions (each function occupies it's own square):

```python
def double(number):
  return number * 2
```
```python
def multiply(number1, number2):
  return number1 * number2
```
```python
def print_whatever():
  print("Whatever.")
```
```python
my_number = 10
print(double(my_number)) # Prints 20
print(multiply(my_number, 3)) # Prints 30
```
A few key points:

  * We use the `def` keyword to tell Python that we are defining a function.
  * After def we write the *name* of the function. The possible names for functions are the same as for variables.
  * After the name, in parentheses, we write what *arguments* the function will **take**. If the function takes no arguments, we must write an empty set of parentheses.
  * We write a `:` to indicate that what follows is the *body* of the function. The code that follows should be *indented* (1 `TAB` character), to indicate that it is part of the *body* of the function. The function ends when the first line with less indention is met. (This is very similar to what we had with `if` statements.)
  * If we wish to pass something back to our program, we use the `return` keyword

Now, let's go back to the `say_hi` function:

```python
def say_hi(name):
  print("Hi, " + name + "!")

say_hi("Mark")
```

When we *call* `say_hi` with argument `"Mark"`, Python essentially creates a new program, that looks something like this:

```python
name = "Mark"
print("Hi, " + name + "!")
```

Here, `name` is called a **local** variable. This is because it only exists within that function call (we say that `name` only exists within the **scope** of the function). In fact, functions are not aware of variables that exist outside of them. Here are a few examples where things can go wrong:

```python
def say_hi(name):
  print("Hi, " + name + "!")

say_hi("Mark")
print(name) # ERROR: name is not a variable in the main program!
```

```python
def say_hi():
  print("Hi, " + name + "!") # ERROR: name is not a variable in this function!

name = "Mark"
say_hi()
```

In the last examples, we see that our main program is unaware of the variables in our functions, and vice-versa. Thus, we could rewrite the original program as:

```python
def say_hi(name):
  print("Hi, " + name + "!")

name = input("Please enter your name: ")
say_hi(name)
```
When we do this, we should always keep in mind that the local variable `name` inside the `say_hi` function is completely different from the variable `name` inside our main program. To emphasise this we can also have this example:

```python
def change_name(name):
  name = "Peter"
  print(name) # Prints 'Peter'

name = "Mark"
change_name(name)
print(name) # Prints 'Mark'
```
This illustrates that the name inside the function is a variable, so in particular, we can change it. Additionally, changing the variable inside the function does not change the variable we used outside - they are different variables!

Functions can also have create their own variables:
```python
def print_whatever():
  message = "Whatever."
  print(message) # Prints 'Whatever.

print_whatever() # This is fine.
print(message) # ERROR: message is not a variable in the main program.
```

Now, lets examine the `double` function:

```python
def multiply(number):
  return number * 2

print(double(10)) # Prints '20'
```

What the `return` keyword means is that the value after it is passed back to the part of the code that called it (in this case, to the print statement).

Functions can also call other functions. For example:

```python
def multiply(x, y):
    return x * y

def double(x):
    return multiply(2, x)

print(double(10))
```

When executed, this is what the code will do:

![Calls](calls.png)

Again, each function call creates its own scope. So the local variable `x` inside `double` is different from the local variable `x` inside `multiply`.

## Excercises:

### Easy:
* 1: Create a function, called `my_function`, which prints "This is my first function!".
* 2: Create a function, called `average`, which takes two arguments, `a` and `b`, and returns `(a + b) / 2`. Then, use this function within a program that prints the average of the two numbers.
* 3: Create a function, called `is_this_me`, which takes 1 argument: a name, and prints "Yes!" if the name is your name, and "No!" otherwise.
  
### Medium:
* 4: Create a function, which takes 4 arguments and multiplies them using the `multiply` function. Do this by creating two additional variables inside your functions. *Harder:* do this without creating additional variables.
* 5: Create a function, which takes three arguments: two numbers, `a` and `b`, and one string, `operation`. If `operation` is one of "add", "subtract", "multiply", "divide", your program should return the result of performing that operation on `a` and `b` (e.g. if it is "subtract", return `a` - `b`). If it is neither, it should print "Unknown operation." and return 0.

### Hard:
These questions explore the concept of *recursion*. You might find it helpful to google what that is before attempting them.

* 6: Write a function that takes as input a number n and returns the product of all numbers up to n; that is 1 * 2 * 3 * ... * n.

* 7: (Math) The Fibonnaci numbers are defined as follows: F(0) = 0, F(1) = 1, F(n+1) = F(n) + F(n-1) for n >= 1. Write a program that calculates the n-th Fibonnaci number.

## Short aside: incrementing

We've seen before that we can do:
```python
number = 1
print(number + 1) # Prints '2'
print(number) # Prints '1'
```

But what if we want to actually increase the values of `number`? We might be tempted to do:
```python
number = 1
number + 1
print(number) # Still prints '1'
```
But that doesn't change `number` at all: it just asks Python to evaluate what `number + 1` is. The way to actually increment `number` is:

```python
number = 1
number = number + 1
print(number) # Prints 2
```
This might seem a bit confusing at first, since `number` appears both on the left and on the right of the `=`. The rule in Python is that stuff on the right side of and `=` are evaluated before stuff on the left side. You can think about the above code like it was shorthand for this:

```python
number = 1
temp = number + 1
number = temp
print(number)
```

Another way to do this exact same thing is:
```python
number = 1
number += 1
print(number)
```

Here, the `+=` operator is used as a shorthand for writing `number = number + 1`. There are analogous operators: `-=`, `*=`, `/=`, etc.
```python
number = 1
number += 2
number -= 3
number *= 4
number /= 5
# ...
```
If unsure, just use the first form: `number = number + 1`. 

In the specific case when we have `number += 1` (i.e. we have `1` on the right-hand side) we say that we **increment** `number`. When we do `number -= 1` we say that we **decrement** `number`.

## While loops

Imagine we wanted to create a simple security function, which asks our user for a password, until they enter the correct one. One way to do this is:

```python
SECRET_PASSWORD = "pass123"

user_input = input("Please enter a password: ")

while user_input != SECRET_PASSWORD:
  print("Access denied: wrong password.")
  print() # Print a newline. This is just here to make things look nicer.
  user_input = input("Please enter the password: ")

print("Access granted.")
```

This program will continue prompting the user for a password until they input the correct password, which is "pass123". One way to think about the above code is like this **(Note: this is NOT actual Python code)**:

```python
SECRET_PASSWORD = "pass123"

user_input = input("Please enter a password: ")

<START OF WHILE LOOP>
if user_input != SECRET_PASSWORD:
  print("Access denied: wrong password.")
  print() # Print a newline. This is just here to make things look nicer.
  user_input = input("Please enter the password: ")
  GOTO: <START OF WHILE LOOP>

print("Access granted.")
```

Here, `<START OF WHILE LOOP>` is just there to label that line. Then the GOTO says that the program should start executing that line again.

So back to the actual code. The idea with the while loop is very simple: the code in the body of the loop will be executed repeatedly, while the condition remains true; otherwise said: until the condition becomes false. In this case, while the user keeps entering the wrong password, the program will keep prompting them for a new one.

Now, if the user enters the correct password on their first try, the body of the loop will not be executed.


Let's see some more examples. Here is how we print the first n natural numbers:
```python
n = int(input("Please enter a number: "))

i = 1
while i <= n:
  print(i)
  i += 1 # Increment i (i becomes bigger by 1).
```

This is a very common paradigm in all of programming. It is called **iterating** over a range. This is because, within the while loop, the variable `i` consecutively takes all values from 1 to n. It is almost ubiquitous to use variable names like `i`, `j`, `k` for iteration.

Here is how we calculate the sum of the first n natural numbers:
```python
n = int(input("Please enter a number: "))

i = 1
sum = 0
while i <= n:
  sum += i
  i += 1

print("The sum of the first " + str(n) + " natural numbers is " + str(sum))
```

A common pitfall is to forget to increment. Here is how we **don't** calculate the sum of the first n natrual numbers:

```python
n = int(input("Please enter a number: "))

i = 1
sum = 0
while i <= n:
  sum += i

print("The sum of the first " + str(n) + " natural numbers is " + str(sum))
```

If that looks like the same code to you, don't worry; even experienced programmers often make this simple mistake. The issue is that we don't increment `i` within the body of the loop. So every time we pass through the loop, `i` remains `1`. If `n` is more than `2`, then this loop will go on forever.

## Excercises:

### Easy:
* 8: Create a program that asks the user to input a number `n`, and then prints the first `n` natural numbers in reverse order. E.g. if `n` is 4, your program should print: '4 3 2 1', each number being on a newline.
* 9: Create a program, which asks the user to input a number `n` and then prints the product of the first `n` natural numbers. E.g. if the input is 4, your program should calculate 1 * 2 * 3 * 4 and print the result.


### Medium:
* 10: Create a program, which continuously prompts the user to input a first name and a last name, until the names they enter match yours.

* 11: Create a program, which takes as input a number `n` and then prints the following:

    1

    1 2

    1 2 3

    .............

    1 2 3 4 ... n
  
  *Hint:* If you want to print something without a newline at the end, the way to to that is:
  ```python
  number = 10
  print(number, end=" ") # This will print a space (" ") after number
  ```

### Very hard:

* 12: (Math) Three numbers $a, b, c$ are called a *Pythagorian triple* if $a^2 + b^2 = c^2$. Write a program, which takes as input an integer $n$, and prints as output $n$ different Pythagorian triples.

## Summary
```python
# A few examples of functions:

def multiply(number1, number2):
  return number1 * number2

def double(number):
  return multiply(number, 2)

def print_whatever():
  print("Whatever.")

my_number = 10
print(double(my_number)) # Prints 20
print(multiply(my_number, 3)) # Prints 30

number = 10
number += 1 # Incrementing a number.
number -= 1 # Decrementing a number.

# Printing the first n natural numbers:
n = int(input("Please enter a number: "))
i = 1
while i <= n:
  print(i)
  i += 1 # Increment i (i becomes bigger by 1).
```

## Recap from Session 1

In the previous session we used these concepts:
```python
# Any text after a '#' symbol on a line is a comment. It is not part of the code.

print("Hello, world!") # This is how we print.

message = "Hi!" # This is how we create variables.
print("The value of the variable is: " + message) # This is how we join strings.

name = input("Please enter you name: ") # This is how we ask for string inputs from our user.
number = int(input("Please enter a number: ")) # This is how we ask for int inputs.
# (Remember: ints are whole numbers [..., -2, -1, 0, 1, 2, ...])

print("The number times two is: " + str(number * 2)) # This is how we join strings with numbers.

# An if statement. Note the : and the == which is how we compare values for equality.
if number == 0:
  print("The number is zero.")
elif number >= 0 and number <= 9:
  print("The number is a positive single digit integer.")
elif number < 0:
  print("The number is negative.")
else:
  print("The number is larger than 10.")
```