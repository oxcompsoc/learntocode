def product(xs):
	# Replace with your code
	return 1

def test(test_case, expected):
	actual = product(test_case)
	if actual == expected:
		print("Passed test for " + str(test_case))
	else:
		print("Didn't pass test for " + str(test_case))
		print("The result was " + str(actual) + " but it should have been " + str(expected))

test([1, 2], 2)
test(range(1, 11), 3628800)
test([1, 2, 3, 0, 4, 5], 0)