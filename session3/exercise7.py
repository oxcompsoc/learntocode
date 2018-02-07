def threes_or_fives(n):
	# return a list of all the integers greater than or equal to zero that are
	# divisible by three or five and less than n
	# You might want to look up the modulus (%) operator, which computes the
	# remainder of division

def test(test_case, expected):
	actual = threes_or_fives(test_case)
	if actual == expected:
		print("Passed test for " + str(test_case))
	else:
		print("Didn't pass test for " + str(test_case))
		print("The result was " + str(actual) + " but it should have been " + str(expected))

test(0, [0])
test(3, [0])
test(5, [0, 3])
test(6, [0, 3, 5])
test(10, [0, 3, 5, 6, 9])