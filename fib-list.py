def fib(n):
    """Return a list of fibonacci numbers up to n."""
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result

print(fib(20))
