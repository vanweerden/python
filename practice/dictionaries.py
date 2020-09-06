import operator
numbers = {1:2, 0:0, 6:5, 2:1, 9:10}

def sort_dict_by_value(d, order):
    """Sorts a dictionary by value, in ascending ('asc') or descending ('desc') order."""
    if order == "desc":
        return dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
    else: 
        return dict(sorted(d.items(), key=operator.itemgetter(1),  reverse=False))

# itemgetter() is like using items() on dict
# Returns list of tuples, so need to make back into dictionary with dict()
print(sort_dict_by_value(numbers, 'asc'))
