def poly_prod(xs, ys):
	# return the list representing the product of the polynomials represented by
	# the lists xs and ys
	
def test(test_case_xs, test_case_ys, expected):
	actual = poly_prod(test_case_xs, test_case_ys)
	if actual == expected:
		print("Passed test for " + str(test_case_xs) + ", " + str(test_case_ys))
	else:
		print("Didn't pass test for " + str(test_case_xs) + ", " + str(test_case_ys))
		print("The result was " + str(actual) + " but it should have been " + str(expected))
		
test([], [], [])
test([1], [], [])
test([1], [2], [2])
test([1, 1], [1, 1], [1, 2, 1])
test([1, 2, 3], [0, 2], [0, 2, 4, 6])
test([0, 2], [1, 2, 3], [0, 2, 4, 6])