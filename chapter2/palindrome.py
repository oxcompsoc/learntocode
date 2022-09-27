def palindrome(n):
    if n == 0:
        print(n)
    else:
        print(n)
        palindrome(n - 1)
        print(n)
        
palindrome(3)