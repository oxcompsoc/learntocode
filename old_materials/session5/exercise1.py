def sum(xs):
    # return the sum of all the elements in the list xs
    # remove the following line
    return 0

def test(test_case, expected):
    actual = sum(test_case)
    if actual == expected:
        print("Passed test for " + str(test_case))
    else:
        print("Didn't pass test for " + str(test_case))
        print("The result was " + str(actual) + " but it should have been " + str(expected))

test([], 0)
test([1, 2], 3)
test(range(10), 45)
