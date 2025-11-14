# Initial code
words = ['slightly', 'greatly', 'passionately', 'madly', 'not', 'cookies', 'cream']

slice_index = 0
while words[slice_index] != "not":
  slice_index += 1

words = words[0:slice_index]


# Adjustment if the list does not contain "not"
words = ['doe', 'ray', 'me', 'far', 'sew']

slice_index = 0
while slice_index < len(words) and words[slice_index] != "not":
  slice_index += 1

words = words[0:slice_index]
