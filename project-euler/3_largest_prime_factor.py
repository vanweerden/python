def is_prime(n):
    """Determines whether n is a prime number (brute force)"""
    result = True
    for i in range(2, n):
        if n % i == 0:
            result = False
    return result

def find_factors(x):
    """Creates list of factors of a given integer"""
    factors = []
    f = 2
    while x > 1:
        if x % f == 0:
            factors.append(f)
            # Updates dividend by dividing it by factor
            x /= f
        else:
            f += 1
    return factors

def largest_prime(l):
    """Takes list of factors and returns the largest prime factor"""
    for i in reversed(l):
        if is_prime(i):
            return i

# Find largest prime factor of 600851475143
factors = find_factors(600851475143)
result = largest_prime(factors)
print("Factors: ", factors)
print("Largest:", result)
