def list_fibonacci(n):
    """Return list of Fibonacci series whose values do not exceed n"""
    a, b = 1, 2
    sequence = []
    while a <= n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

def add_even(l):
    """Takes list of integers and adds the even numbers"""
    sum = 0
    length = len(l)
    for i in range(length):
        if l[i] % 2 == 0:
            sum += l[i]
    return sum

# Takes Fibonacci sequence whose values are under 4 million and adds even values
upper_limit = 4000000
result = add_even(list_fibonacci(upper_limit))
print(result)
