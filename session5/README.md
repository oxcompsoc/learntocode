# Session 5: Dictionaries(cont.) and Object-Oriented Programming

You can find the resources for last week's session [here][s4notes].

In this week's session we are going to continue looking at dictionaries, a common Python data structure introduced at the end of last week's session. Once we've spent a little more time working through an exercise with dictionaries we'll move on to talking about *Object-Oriented Programming* or *OOP* - a way to structure data which is very useful when dealing with various when dealing with Python modules, i.e. the tools that you would use to do more practical things like data analysis and machine learning.

[s4notes]: https://github.com/oxcompsoc/learntocode/tree/master/session4/README.md

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

## Object-Oriented Programming

We talked about types a bit in the first few lectures - think `int` (for *int*egers), `str`(for *str*ings or non-code text), `float`(for *float*ing point numbers or non-whole numbers). It turns out that `list` and `dict` (for *dict*ionary) are also types. You can see that by running:

```python
my_list = ['a', 'b', 'c']
print(type(my_list))            # Prints out <class 'list'>

my_dictionary = {'A': 10, 'B': 42, 'C': 1337}
print (type(my_dictionary))     # Prints out <class 'dict'>
```

It makes sense for those to be their own types because you can do the same things with a variable that contains an `int` as opposed to one that contains a `list` - the former can handle division while the latter has `.append(x)`. While having these types is very convenient and perfectly sufficient to write any program we want (see [Turing-Completeness](https://simple.wikipedia.org/wiki/Turing_complete) if you feel like reading a lot of theory), Python lets us define our own custom types and here's how we do it:

```python
class Person:
    def __init__(self, name, age, birthday):
        self.name = name
        self.age = age
        self.birthday = birthday
        self.friends = []
        self.likes_marmite = False
    
    def addFriend(self, friendName):
        self.friends.append(friendName)

    def printInfo(self):
        print(self.name + ' was born on ' + str(self.birthday) + \
            ' and is ' + str(self.age) + ' years old.')
        if self.likes_marmite:
            print('They like Marmite', end='')
        else:
            print('They don\'t like Marmite', end='')
            
        if len(self.friends) == 0:
            print(' and they don\'t have friends')
        else:
            print(' and their friends are:')
            for friend in self.friends:
                print(friend)
        print()         # A couple of newlines for clarity
        print()

me = Person('Ilia', 21, '15/09')
me.addFriend('Ivan')
me.printInfo()
me.addFriend('Ben')
me.addFriend('Kate')
me.printInfo()

print('My name is ' + me.name)

print(type(me))

ben = Person('Ben', 21, '5/12')
ben.addFriend('Ilia')
ben.addFriend('Kate')
ben.printInfo()


#This prints out the following:
'''
Ilia was born on 15/09 and is 21 years old.
They don't like Marmite and their friends are:
Ivan


Ilia was born on 15/09 and is 21 years old.
They don't like Marmite and their friends are:
Ivan
Ben
Kate


My name is Ilia
<class '__main__.Person'>
Ben was born on 5/12 and is 21 years old.
They don't like Marmite and their friends are:
Ilia
Kate


'''
```

That was a lot of code so here's some explanation:
 - `class Person:` defines a "class" which means a custom type
 - `def __init__(self, ...):` is called a *constructor* - it's a function that defines an *instance* of our class. This is what gets called when you write `Person(...)`.
 - `self` is a reference to the *instance* of the current object. So basically in `__init__` we're trying to say that when we create a person, make their name equal to the parameter `name`, their age equal to the parameter `age` and their birthday equal to the parameter `birthday`. All variables that are accessed through `self` are commonly known as *member variables*.
 - `def addFriend(self, ...):` and `def printInfo(self, ...)` are functions that you can call from an instance of `Person` using `.`. `me.addFriend("Ben")` and `me.printInfo()` are examples of that. Question: Which function that we've seen until now looks like that?
  Notice how `self` is an argument to those functions but we never provide it. That is because `self` is a reserved word in Python and Python will always infer that it's the current instance of the class. In general, don't forget to add `self` as the first argument to any function that you have in Python - there are far more functions that need it than there are that don't.
 - `me = Person('Ilia', 21, '15/09')` is very similar to how we define lists and other variables. Here we define a variable of type `Person` called `me` with the respective `constructor arguments`. In Python you can be explicit about the names of these arguments if you are unsure like so: `me = Person(age = 21, name = 'Ilia', birthday = '15/09')`. If you do this you don't necessarily have to have the arguments in the same order.

It turns out that you can model pretty much anything using simpler values. Let's model a few more things as exercises:

### Exercise: Make a class that represents a room

Make a class that represents a regular room. It needs to have a width, height and depth, a kind among `lecture theatre`, `kitchen`, `living room`, `hallway` and a list of items in them. Also add functions that add and remove items from the rooms, a function that calculates the floor area and one that calculates the volume. Try to make instances of a few rooms that you know like the lecture theatre or your home's living room.

### Exercise: Model a floor

Now that you have a floor, next up make another class in the same file that models a floor of a building - give it no constructor arguments and have it only hold a list of rooms. Add the following functions:
 - `add_room` adds an instance of a room to the list only if the height of the room is the same as that of the other rooms in the list. Question: What should you do when there are no rooms in the list
 - `get_items` returns all the items that are in the rooms on the floor
 - `get_floor_area` returns the overall floor area of every room on the floor
 - `get_floor_volume` returns the overall volume of every room on the floor

### Exercise: Now let's do an entire building

And last but not least we want to make another class in the same file that models an entire building. Similarly to the floors have it accept no constructor arguments and have it only hold a list of floors. We want the building to be stable stable so we want successive floors to have strictly less and less area. THe class should have the following functions: `add_floor`, `get_items`, `get_area` and `get_volume`.


## Polymorphism

Now that we've had a quick intro to classes, next we'll eat some fruit. First let's model an apple:

```python
class Apple:
    fruit_name = 'apple'

    def __init__(self, nutrition, color):
        self.taste = nutrition
        self.color = color
    
    def rot():
        self.nutrition -= 10
```

and let's do an orange:

```python
class Orange:
    fruit_name = 'orange'

    def __init__(self, nutrition, color):
        self.nutrition = nutrition
        self.color = color
    
    def rot():
        self.nutrition -= 5
```

now that we have both we can let take the `Person` class that we defined earlier in the lecture and teach them how to eat like so:

```python
# I'm using ... to represent code that's the same
class Person:

    def __init__(self, ...):
        ...
        self.hunger = 100

    ...

    def eat_fruit(self, fruit):
        print(self.name + ' ate a ' + fruit.color + ' ' + fruit.fruit_name)
        self.hunger -= fruit.nutrition
```

This is an example of polymorphism - what this basically means is that a fruit can be of either type Apple or Orange and we can have a single definition for eat that is capable of handling both of them.

The reason we covered classes today is because they are used everywhere when dealing with modules - the things that most people rely on to do their daily work with Python. Next time we'll cover a few of those with a focus on the ones that are useful for data science.