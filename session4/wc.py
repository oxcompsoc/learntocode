text = input("Enter some text: ")
words = text.split(" ")
counts = {}

for word in words:
    if word in counts:
        counts[word] = counts[word] + 1
    else:
        counts[word] = 1

for word in counts:
    print("{}: {}".format(word, counts[word]))
