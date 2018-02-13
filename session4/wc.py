text = input("Please enter some text: ")
words = text.lower().split(" ")
counts = {}

for word in words:
    if word in counts:
        counts[word] = counts[word] + 1
    else:
        counts[word] = 1

for word in counts:
    print("{}: {}".format(word, counts[word]))
