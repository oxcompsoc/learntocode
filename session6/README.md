# Session 6: A tour of data science with Python

## Introduction

So far in this course we've covered the fundamentals of Python - the stuff you need to create pretty much anything useful. Тhis session will be more of a case study in applying your skills to do something useful. In particular, we will focus on doing some data science.

## Set-up

If you want to run the examples in this lecture, you will need a bit of additional software. This should be straightforward to acquire if you installed Python using the instructions from session 0. To install the new stuff:

* Open up a Terminal window in MacOS or Command Prompt in Windows
* Type in the following commands, one by one, waiting for each one to finish, before moving on:

```
pip install jupyter
pip install matplotlib
pip install numpy
pip install pandas
pip install scipy
pip install sklearn
```

You should now have everything necessary to run the examples in this session.

## Modules

Up until now, we've only made use of the *core* Python functionality, things like the `print` and `input` functions, as well as `int`s, `str`s, `list`s, and `dict`s. Sometimes, we need some more advanced functionality. Here is an example where we want to output 10 random integers from the range:

```python
import random

for i in range(10):
    print(random.randint(1,100))
```

`random` is called a **module**. It is a collection of useful functions and classes, related to random number generation. When we say `import random` we tell Python that we would like access to these functions within our current program. The module `random` contains a function, called `randint`, which generates a random number between the lower and upper bound provided (in this case 1 and 100). When we wish to use this function, we must explicitly state that we want to use the `randint` function from the `random` module (since a function with the same name might be defined in another module we import). We do this with the `.`: `random.randint`.

### Creating our own modules

The module `random` is part of the **Python Standard Library**, which is a collection of useful modules you get with every Python installation. When we start writing larger programs, we usually want to organize our own functions in different files, based on what they do. Let's use as an example the fruits classes we defined last session. In a file called `fruits.py` we will put the following code:

```python
# fruits.py
class Apple:
    fruit_name = 'apple'

    def __init__(self, color):
        self.color = color

class Orange:
    fruit_name = 'orange'

    def __init__(self, color):
        self.color = color

def print_fruit(fruit):
    print('This is a ' + fruit.color + ' ' + fruit.fruit_name + '.')
```

Now, if we create a file called `main.py` in the same folder, we could do:

```python
# main.py
import fruits

my_fruit = fruits.Apple('red')
fruits.print_fruit(my_fruit) # Prints 'This is a red apple.'
```

Notice that we `import fruits`, and **not** `import fruits.py`. Importing our own modules works in mostly the same way as standard ones. The difference here is that `fruits.py` needs to be in the same folder as `main.py`.

It is common sometimes to use a lot of functionality from a module. It would be annoying to write out `fruits.` before every fruit we use. Python provides a few tools to make our lives easier. One common thing you will see is:

```python
import fruits as fr

my_fruit = fr.Apple('red')
fr.print_fruit(my_fruit) # Prints 'This is a red apple.'
```

We still have to indicate that the functions/classes we are using are from the fruits module, but the `as` keyword tells Python that we will write `fr.` instead of `fruits.`

Another way is:
```python
from fruits import Apple, print_fruit

my_fruit = Apple('red')
print_fruit(my_fruit) # Prints 'This is a red apple.'
```

This tells Python to take the `Apple` class and the `print_fruit` function **from** the `fruits` module, and treat them as if they were part of this file. We can list out everything we want to **import**, separated by commas. Python also supports the syntax ```from fruits import *```, which would import everything from the module, but this practice is discouraged when writing larger programs, and we suggest you avoid using it.


## Jupyter notebook

For the rest of the session we will be using a graphical environment, called **Jupyter Notebook**, which you should have installed if you followed the set-up instructions. To launch Jupyter, simply open up a terminal (command prompt) window, and type in `jupyter notebook`. This should launch a web browser window that looks something like this: ![jupyter1]

Here, I've navigated to my `learn_to_code` folder. To create a new notebook, simply click **New** > **Python3**: ![jupyter2]

You should now get a window that looks something like this: ![jupyter3]

For the rest of the tutorial, open up the `notebook.ipynb` on this page. Don't worry about memorizing or even fully understanding everything on that page, it is meant as more of a tour of the powerful tools that exist for Python. Also, please don't treat this as a tutorial for *actually* doing data science. This is more a tour of the functionality available to you, should you want to try. If you want to learn more about this area in particular, I encourage you to look up more resources, which will explain the theory in detail.

## Closing remarks

We've covered a lot of ground in this course. If you liked it and want to improve your skills, we encourage you to keep practicing. Bellow we've listed some resources we think might be useful to you. There are many tutorials out there, so feel free to seek out the content that best fits your learning style and your goals with programming. In general, try to practice as much as possible, by actually doing exercises and writing code yourself. If you face errors or get stuck, try to google your issues - you probably aren't the first person to encounter them!

### Resources:


1. [The official Python tutorial][python_tutorial] - learn straight from the source. This is usually a good source for more experienced programmers, but you might want to check it out.

2. [HackerRank][hr] - a great place to do some algorithmic challenges (think "computer science"). They also have an exercise-based Python tutorial.

3. [Project Euler][euler] - mathematical challenges that can be solved with programming. Good if you like maths.

4. [An introduction to pyplot][plt] - if you're specifically interested in using python to make plots.

[jupyter1]: jupyter1.jpg
[jupyter2]: jupyter2.jpg
[jupyter3]: jupyter3.jpg
[python_tutorial]: https://ehmatthes.github.io/pcc/
[euler]: http://projecteuler.net
[plt]: https://matplotlib.org/tutorials/introductory/pyplot.html
[hr]: https://www.hackerrank.com/