# Exercise 1
def sum(xs):
    k = 0
    for x in xs:
        k = k + x
    return k

# Exercise 2
def product(xs):
    p = 1
    for x in xs:
        p = p * x
    return p

# Exercise 3
def mean(xs):
    k = 0
    for x in xs:
        k = k + x
    return k / len(xs)

# Exercise 4
def flatten(xs):
    flattened = []
    for x in xs:
        flattened += x
    return flattened

# Exercise 5
def sum2(xs, ys):
    zs = []
    for i in range(0, len(xs)):
        zs.append(xs[i] + ys[i])
    return zs

# Exercise 6
def sum2(xs, ys):
    zs = []
    l = min(len(xs), len(ys))
    for i in range(0, l):
        zs.append(xs[i] + ys[i])
    if len(xs) > len(ys):
        for i in range(l, len(xs)):
            zs.append(xs[i])
    else:
        for i in range(l, len(ys)):
            zs.append(ys[i])
    return zs
    
# Exercise 7
def threes_or_fives(n):
    # return a list of all the integers greater than or equal to zero that are
    # divisible by three or five and less than n
    # You might want to look up the modulus (%) operator, which computes the
    # remainder of division
    xs = []
    for x in range(0, n):
        if x % 3 == 0 or x % 5 == 0:
            xs.append(x)
    return xs
    
# Exercise 8
def filtered_even(xs):
    ys = []
    for x in xs:
        if x % 2 == 0:
            ys.append(x)
    return ys

# Exercise 9
def filtered_text(xs):
    ys = []
    for x in xs:
        if "a" <= x[0] and "z" >= x[0]:
            ys.append(x)
    return ys
    
# Exercise 10
def rot(xs, n):
    ys = []
    for i in range(0, len(xs)):
        ys.append(xs[(i + n) % len(xs)])
    return ys
    
# Exercise 11
def uniques(xs):
    # return a list of all the unique elements
    ys = sorted(xs)
    zs = []
    for i in range(0, len(ys)):
        if i == 0 or ys[i] != ys[i - 1]:
            zs.append(ys[i])
    return zs
    
# Exercise 12
def bin_search(xs, x):
    # return the least index of an element equal to x in the sorted list xs
    low = 0
    high = len(xs)
    while low + 1 < high:
        guess = (low + high) // 2
        if x < xs[guess]:
            high = guess
        else:
            low = guess
    return low
    
# Exercise 13
def merge(xs, ys):
    # return a sorted list with the merged contents of the sorted lists xs and ys
    i = 0
    j = 0
    zs = []
    while not (i == len(xs) or j == len(ys)):
        if xs[i] < ys[j]:
            zs.append(xs[i])
            i = i + 1
        else:
            zs.append(ys[j])
            j = j + 1
    while i != len(xs):
        zs.append(xs[i])
        i = i + 1
    while j != len(ys):
        zs.append(ys[j])
        j = j + 1
    return zs
    
# Exercise 14
def merge_sort(xs):
    # sort xs
    if len(xs) <= 1:
        return xs
    else:
        first_half = xs[:(len(xs) // 2)]
        first_half_sorted = merge_sort(first_half)
        second_half = xs[(len(xs) // 2):]
        second_half_sorted = merge_sort(second_half)
        return merge(first_half_sorted, second_half_sorted)
        
# Exercise 15
def print_polynomial(coefs):
    strs = []
    for i in range(0, len(coefs)):
        if coefs[i] != 0:
            strs.append(str(coefs[i]) + "x^" + str(i))
    print(" + ".join(strs))
        
# Exercise 16
def poly_sum(xs, ys):
    zs = []
    l = min(len(xs), len(ys))
    for i in range(0, l):
        zs.append(xs[i] + ys[i])
    if len(xs) > len(ys):
        for i in range(l, len(xs)):
            zs.append(xs[i])
    else:
        for i in range(l, len(ys)):
            zs.append(ys[i])
    return zs
    
# Exercise 17
def poly_prod(xs, ys):
    # return the list representing the product of the polynomials represented by
    # the lists xs and ys
    # len(xs) + len(ys) - 1 is the maximum degree of the resulting polynomial
    res = [0] * (len(xs) + len(ys) - 1)
    
    # Draw as a table to figure this out
    for i in range(0, len(xs)):
        for j in range(0, len(ys)):
            res[i + j] = res[i + j] + (xs[i] * ys[j])
    
    return res