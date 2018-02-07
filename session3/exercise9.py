def filtered_text(xs):
	# Return a copy of xs that only contains the strings that start with a
	# lowercase letter

def test(test_case, expected):
	actual = filtered_text(test_case)
	if actual == expected:
		print("Passed test for " + str(test_case))
	else:
		print("Didn't pass test for " + str(test_case))
		print("The result was " + str(actual) + " but it should have been " + str(expected))

test([], [])
test(["Learn", "to", "Code"], ["to"])
test(["Oxford", "University", "Computer", "Society"], [])
test(["learn", "to", "code"], ["learn", "to", "code"])