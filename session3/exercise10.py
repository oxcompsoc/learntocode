def rot(xs, n):
    # return a list of xs rotated by n

def test(test_case_xs, test_case_n, expected):
    actual = rot(test_case_xs, test_case_n)
    if actual == expected:
        print("Passed test for " + str(test_case_xs) + ", " + str(test_case_n))
    else:
        print("Didn't pass test for " + str(test_case) + ", " + str(test_case_n))
        print("The result was " + str(actual) + " but it should have been " + str(expected))

test([], 0, [])
test([], 10, [])
test([1, 2, 3], 1, [2, 3, 1])
test([1, 2, 3, 4, 5], 2, [3, 4, 5, 1, 2])
test([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5])
test([1, 2, 3, 4, 5], -1, [5, 1, 2, 3, 4])