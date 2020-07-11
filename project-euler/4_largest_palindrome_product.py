import math

def is_palindrome(n):
    """Checks if a string is a palindrome"""
    n = str(n)
    middle = math.floor(len(n) / 2)

    i = 0
    while i < middle:
        if n[i] != n[(i * -1) - 1]:
            return False
        i += 1
    return True

def list_palindromes(n):
    """Creates list of all palindromic products of values n * n and less

    i.e. n * n, n * n -1, n * n-2, etc.
    """
    factors = range(n, 0, -1)
    palindromes = []

    for a in factors:
        for b in factors:
            if is_palindrome(a * b):
                palindromes.append(a * b)

    return palindromes

def find_largest_value(L):
    """Return largest value from a list"""
    largest = 0
    for n in L:
        if n > largest:
            largest = n
    return largest

def find_largest_palindrome():
    """Find the largest palindrome made from the product of two 3-digit numbers.
    """
    palindromes = list_palindromes(999)
    return find_largest_value(palindromes)

solution = find_largest_palindrome()
print(solution)
