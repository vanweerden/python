def make_multiplier(n):
    """ Returns function that multiplies argument by n.

    Lambda creates anonymous function (cf. JS arrow function)
    """
    return lambda x: x * n

times_two = make_multiplier(2)
times_ten = make_multiplier(10)

print(times_two(12)) # Should be 24
print(times_ten(5)) # Should be 50

# Can also be used to pass function as argument (again, like JS arrow function)
