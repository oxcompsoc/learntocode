# Chapter 2: If statements

See [here][week1] for last week's content. 

[week1]: https://github.com/oxcompsoc/learntocode/tree/master/chapter1

We often want our programs to adapt their behaviour based on the input they receive. For instance, lets say we want to create a program, which tells our user if the number they input is small (e.g. less than 10). This is what the next program does:

```python
number = int(input("Please enter a number: "))
if number < 10:
  print(number + " is a small number.")
```

We could also have our program say something if the number is large as well:

```python
number = int(input("Please enter a number: "))
if number < 10:
  print(number + " is a small number.")
else:
  print(number + " is a large number.")
```


We can read the above as
> if "this condition is true" then "execute this code", otherwise "execute this other code"

We can generalise the first example as:

```python
if condition_is_true:
  execute_this_code
```

And the second one as:

```python
if condition_is_true:
  execute_this_code
else:
  this_code_is_executed_otherwise
```

Notice that we write "then" as `:`. The most important thing to notice is that we execute the indented code *only* when the condition holds.

We can write any number of statements inside the **body** of the `if`
statement, i.e. statements that are indented (press `TAB`) will only be
executed if the condition of the `if` statement holds.

There are several important concepts to note here:

 * If we want to compare two values (e.g. the value the user entered and a fixed string) we use `==` instead of `=` (remember, `=` means *becomes*)
 * We can compare numbers and strings using the comparison operators `==`, `!=` (not equal), `<=` (less than or equal), `>=` (greater than or equal), `<` (less than), and `>` (greater than)
 * `if` statements can be nested

We can also abbreviate the following:

```python
number = int(input("Please enter a number: "))
if number < 10:
  print("This number is small.")
else:
  if number >= 10 and number < 100:
    print("This number is not small, but not large either.")
  else:
    print("This number is large.")
```

to

```python
number = int(input("Please enter a number: "))
if number < 10:
  print("This number is small.")
elif number >= 10 and number < 100:
  print("This number is not small, but not large either.")
else:
  print("This number is large.")
```

You can have as many `elif` branches as you like, but only one `if` branch and
one `else` branch, which must appear at the beginning and end respectively.

Here we used the keyword `and` to mean that we want both `number >= 10` and `number < 100` to be true for that branch to be executed. You could use `or` and `not` in expressions, e.g.

```python
number = int(input("Please enter a number: "))
if not number < 10:
  # Will be executed if number is not less than 10 (i.e. if number >= 10)
  print("The number is not less than 10.")

if number == 3 or number == 4:
  # Will be executed if number is equal to 3 or equal to 4
  # Note that comparison is done with == rather than =
  print("The number is either 3 or 4.")
```
If you are using multiple different connectives, you should include parentheses to make it clear how the expression should be interpreted. E.g.

```python
number = int(input("Please enter a number: "))
if ((1 <= number and number < 10) or number == 42) and (not number == 3):
  print("This was the number: " + str(number))
```

This code will only print `number` if it is one of the numbers [0, 1, 2, 4, 5, 6, 7, 8, 9, 42].

*Note: there is an order of operations on logical connectives as well (which you may wish to google); however, it is recommended that you insert parentheses if you are using multiple different connectives, like in the example above.*

It's important to remember that an `else` statement (or an `elif`) statement is associated with the closest `if` statement above it, which has the same indentation (same number of `TAB`s before it). So consider the program:

```python
name = input("Please enter a name: ")
if name == "Mark":
  print("Oh, hi Mark.")
if name == "Johnny":
  print("Oh, hey Johnny, what's up?")
else:
  print("Who is this?")
```

You might think that if the name input is 'Mark' it will print 'Oh, hi Mark.' if it's Johnny, it will print 'Oh, hey Johnny, what's up?', and otherwise it will print 'Who is this?'. But actually, if the name is Mark, it will print both 'Oh, hi Mark' and 'Who is this?'. This is because the `else` statement is only associated with the `if` just above it. The first `if` is completely independent. You might find it helpful to think about the program split as so:
```python
name = input("Please enter a name: ")
```
```python
if name == "Mark":
  print("Oh, hi Mark.")
```
```python
if name == "Johnny":
  print("Oh, hey Johnny, what's up?")
else:
  print("Who is this?")
```

The correct way to write the above program is using an `elif`:
```python
name = input("Please enter a name: ")
if name == "Mark":
  print("Oh, hi Mark.")
elif name == "Johnny":
  print("Oh, hey Johnny, what's up?")
else:
  print("Who is this?")
```


## Exercise

* **One detector:** create a program, which takes as input an int and outputs "This number is 1" if the input was 1 and "This input was not 1" otherwise.

* **Average of two numbers:** create a program which takes as input two numbers and computes their average. Can think of how you could extend this to compute the average of three numbers? How about the average of ten numbers?






