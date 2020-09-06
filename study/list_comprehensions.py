""" List Comprehension
Basic form
[expr for val in collection]

- expr generates elements in list
- for loop evaluates expression for every item in collection

- optional if clause: expr in list only if if-clause evaluates to true
[expr for vcal in collection if <test1> and <test2>]
"""

# Ex. 1 squares of first 100 positive ints
squares = []
for i in range(1, 101):
    squares.append(i**2)

# With list Comprehension: Much more succinct
squares2 = [i**2 for i in range(1, 101)]

# Ex. 2 list of remainders when divide first 100 squares by 5
remainders5 = [x**2 % 5 for x in range (1, 101)]

# Ex 3 Find movies in list that begin with g
# Evaluates title in list only if title starts with "G"
gmovies = [title for title in movies if title.startswith("G")]

# Ex 4 Find movies in list that were released before 2000 (list of tuples)
# Prints title to list, but uses year to evaluate which to print
pre2k = [title for (title, year) in movies if year < 2000]
