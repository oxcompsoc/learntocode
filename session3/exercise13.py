def merge(xs, ys):
	# return a sorted list with the merged contents of the sorted lists xs and ys

def test(test_case_xs, test_case_ys, expected):
	actual = merge(test_case_xs, test_case_ys)
	if actual == expected:
		print("Passed test for " + str(test_case_xs) + ", " + str(test_case_ys))
	else:
		print("Didn't pass test for " + str(test_case_xs) + ", " + str(test_case_ys))
		print("The result was " + str(actual) + " but it should have been " + str(expected))
		
test([], [], [])
test([0], [], [0])
test([], [0], [0])
test([0, 1, 2], [0, 1, 2], [0, 0, 1, 1, 2, 2])
test([0, 1, 2], [3, 4, 5], [0, 1, 2, 3, 4, 5])
test([3, 4, 5], [0, 1, 2], [0, 1, 2, 3, 4, 5])
test([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3], [0, 0, 1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9])
test([0, 1, 2, 3], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 0, 1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 8, 9])