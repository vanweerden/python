# Main insights: Counter and list comprehensions

from collections import Counter

def highest_rank(arr):
    """Find element that occurs most frequently in an array"""
    # Basic error check: only executes if there is an argument
    if arr:
        # Creates Counter collection of frequencies of items
        c = Counter(arr)
        # Creates list of values of Collection and finds max
        m = max(c.values())
        # Comprehension: Checks for a "tie"
        return max(k for k,v in c.items() if v==m)


""" Detailed notes:
COUNTER 
creates an unordered collection in which elements are stored as
dictionary keys and their counts as dict values.

It is a dict subclass.

USEFUL DICTIONARY METHODS
d.values() returns list of dict values
d.keys() returns list of dict keys
d.items() returns list of key-value pairs (as tuples in a list)
list(d) does the same as d.keys()

max() is a built-in function: takes a list as arg

COMPREHENSIONS
max(k for k,v in c.items() if v==m)

Creates list of keys resulting from evaluating k after putting it through for- an
if- clauses
"""
