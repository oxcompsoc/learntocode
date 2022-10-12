def mean(xs):
    # return the mean of the list of elements

def test(test_case, expected):
    actual = mean(test_case)
    if actual == expected:
        print("Passed test for " + str(test_case))
    else:
        print("Didn't pass test for " + str(test_case))
        print("The result was " + str(actual) + " but it should have been " + str(expected))

test([1, 2], 1.5)
test(range(0, 10), 4.5)
test([-1, 0, 1], 0)