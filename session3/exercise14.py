def merge(xs, ys):
	# return a sorted list with the merged contents of the sorted lists xs and ys

def merge_sort(xs):
	# sort xs

def test(test_case_xs, expected):
	actual = merge_sort(test_case_xs)
	if actual == expected:
		print("Passed test for " + str(test_case_xs))
	else:
		print("Didn't pass test for " + str(test_case_xs))
		print("The result was " + str(actual) + " but it should have been " + str(expected))
		
test([], [])
test([0], [0])
test([1, 2], [1, 2])
test([2, 1], [1, 2])
test([4, 3, 2, 1], [1, 2, 3, 4])
test([1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8])
test([8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8])
test([8, 7, 6, 5, 4, 3, 2, 1, 10, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])