def make_multiplier(n):
    """ Returns function that multiplies argument by n.

    Lambda creates anonymous function (cf. JS arrow function)
    """
    return lambda x: x * n

times_two = make_multiplier(2)
times_ten = make_multiplier(10)

# print(times_two(12)) # Should be 24
# print(times_ten(5)) # Should be 50

# Can also be used to pass function as argument (again, like JS arrow function)


ages = [("Andrew", 33), ("Josie", 29), ("Frank", 55)]

def sort_by_age(tuples):
    """Sorts tuples of (name, age) by age."""
    return sorted(tuples, key = lambda x: x[1], reverse = False)

students_ages = [{"name": "Victor", "age": 35}, {"name": "Leidy", "age": 31},
{"name": "Miku", "age": 21}, {"name": "Kelly", "age": 22}]

def sort_dictionaries(dicts):
    """Sorts a dictionary of students by age."""
    return sorted(dicts, key = lambda x: x["age"])

number_list = list(range(1, 101))
def filter_integers(ints):
    """Filters integers that are disivible by 3 (better to just use a list comprehension)."""
    return filter(list(lambda a: a % 3 == 0, ints))

# NOTES
# Filter is not a method attached to a list
# Returns a filter object; must be made into a list with list()
print(filter_integers(number_list))
