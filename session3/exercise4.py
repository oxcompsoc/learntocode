def flatten(xs):
	flattened = []
	for x in xs:
		flattened += x
	return flattened

def test(test_case, expected):
	actual = flatten(test_case)
	if actual == expected:
		print("Passed test for " + str(test_case))
	else:
		print("Didn't pass test for " + str(test_case))
		print("The result was " + str(actual) + " but it should have been " + str(expected))

test([], [])
test([[1, 2], [3, 4]], [1, 2, 3, 4])
test([[], [1, 2], [3, 4], []], [1, 2, 3, 4])