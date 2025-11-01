# String multiplication can be handy sometimes.

# If I want to yell very loudly, for instance, I can go
print("A" * 500)

# If I want to encrypt something with Vigenere (https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)
# I might start with
plaintext = "This is my message"
key = "compsoc"
# Repeat the key until it covers the entire message
key_repeated = key * math.ceil(len(plaintext) / len(key))
# and then proceed from there.

# We'll talk about the length function, len(), when we talk about lists in session 4.
