# More advanced problems

In this week's session we are going to once again focus on using data structures
and algorithms that we've already seen in order to solve new problems.

## Dictionaries: Oxford colleges

Before we get started, we're going to spend some time at the prompt in IDLE. The
prompt is a useful way of quickly checking out some functionality without having
to write a full script.

Begin by pasting the following into the prompt:

```python
oxford_sisters = {
    "All Souls":            "Trinity Hall",
    "Balliol":              "St John's",
    "Brasenose":            "Gonville and Caius",
    "Christ Church":        "Trinity",
    "Corpus Christi":       "Corpus Christi",
    "Exeter":               "Emmanuel",
    "Green Templeton":      "St Edmunds'",
    "Harris Manchester":    "Homerton",
    "Jesus":                "Jesus",
    "Keble":                "Selwyn",
    "Lady Margaret Hall":   "Newnham",
    "Linacre":              "Hughes Hall",
    "Lincoln":              "Downing",
    "Magdalen":             "Magdalene",
    "Mansfield":            "Homerton",
    "Merton":               "Peterhouse",
    "New":                  "King's",
    "Oriel":                "Clare College",
    "Pembroke":             "Queens' College",
    "Queen's":              "Pembroke",
    "Somerville":           "Girton",
    "St Anne's":            "Murray Edwards",
    "St Antony's":          "Wolfson",
    "St Catherine's":       "Robinson",
    "St Cross":             "Clare Hall",
    "St Edmund Hall":       "Fitzwilliam",
    "St Hilda's":           "Peterhouse",
    "St Hugh's":            "Clare College",
    "St John's":            "Sidney Sussex",
    "Trinity College":      "Churchill",
    "University College":   "Trinity Hall",
    "Wadham":               "Christ's College",
    "Wolfson":              "Darwin",
    "Worcester":            "St Catharine's"
}
```

This dictionary allows us to look up the sister college for an Oxford college,
but suppose we wanted to work the other way around, and find the sister college
for a Cambridge college. To do this we need to *invert* the dictionary.

```python
cambridge_sisters = {} # Create a new empty dictionary
for oxford_college in oxford_sisters:
    cambridge_sisters[oxford_sisters[oxford_college]] = oxford_college
```

Now try the following:

```python
print(oxford_sisters["Trinity"]) # Prints Churchill
print(cambridge_sisters["Churchill"]) # Prints Trinity
```

Here we have a problem though: Clare College in Cambridge is a sister college of
both St Hugh's and Oriel; dictionary keys have to be unique but dictionary
values do not have to be. One option is to ignore this problem, the other is to
construct lists.

```python
cambridge_sisters = {} # Create a new empty dictionary
for oxford_college in oxford_sisters:
    if oxford_sisters[oxford_college] in cambridge_sisters:
        cambridge_sisters[oxford_sisters[oxford_college]].append(oxford_college)
    else
        cambridge_sisters[oxford_sisters[oxford_college]] = [oxford_college]
```

Now if we try `cambridge_sisters["Clare College"]` we will get back the list
`["St Hugh's", "Oriel"]` (although not necessarily in that order; we could
guarantee ordering with `sort()`).

If, however, we knew in advance that the values were unique we could instead do
all of this in one line of Python:

```python
cambridge_sisters = {v: k for k, v in oxford_sisters.items()}
```

## Lists: Sorting

We aren't going to discuss sorting again during the session - we've already seen
the `sort()` method and `sorted()` function. Therefore instead I would encourage
you to take a look at the bubble sort, insertion sort, merge sort, and quick
sort algorithms in your time, and try to understand the difference in *time
complexity* between the algorithms, and why use them.

## Classes

In previous lectures we've seen the use of both functions and methods, although
we didn't take the time to define them. Often we want to carry several pieces of
information about an *object* around, e.g. for a person we might want to
remember their age and name. We could do this with dictionaries, but we will
later see that we want to perform operations on them.

```python
class College:
    def __init__(self, name, age):
        self.name = name
        self.age = age
# Usage:
catz = College("St Catherine's", 54)
print("{} is {} years old".format(catz.name, catz.age))
```

Defining a college like this isn't very convenient though as we would have to
update the age variable every year. Lets instead compute the age:

```python
import datetime

class College
    def __init__(self, name, year);
        self.name = name
        self.year = year

    def age():
        return datetime.datetime.now().year - self.year

# Usage:
catz = College("St Catherine's", 1963)
print("{} is {} years old".format(catz.name, catz.age())
```
