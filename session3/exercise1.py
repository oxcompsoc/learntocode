def sum(xs):
    k = 0
    for x in xs:
        k = k + x
    return k
    
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