import day1_input

depth_values = day1_input.values

##############################################
### METHODS
##############################################

def count_increases_in(values):
    """Counts the number of times a value in a list is higher than its previous value.
    """
    increase_count = 0

    for i in range(1, len(values)):
        current = values[i]
        previous = values[i-1]

        if current > previous:
            increase_count += 1

    return increase_count

def sliding_window_sums_of(values, window_size=3):
    """Creates a list of the sums of a sliding window.
    """
    sums = []

    range_cap = len(values) - window_size + 1
    for i in range(0, range_cap):
        sums.append(sum(values[i:i+3]))

    return sums

##############################################
### EXECUTION
##############################################

result1 = count_increases_in(depth_values)

sliding_window_sums = sliding_window_sums_of(depth_values)
result2 = count_increases_in(sliding_window_sums_of(depth_values))

print("Part 1 results:", result1)
print("Part 2 results:", result2)

##############################################
### TESTS
##############################################

def part1_tests():
    all_passed = True

    results = []
    results.append(count_increases_in([1, 2, 3, 4, 5]))
    results.append(count_increases_in([5, 4, 3, 2, 1]))
    results.append(count_increases_in([149, 163, 165, 160, 179]))

    expected = [4, 0, 3]

    range_cap = len(results)+1
    for n, r, e in zip(range(1, range_cap), results, expected):
        if (r != e):
            # Is there a way to access the iteration number?
            print(f"Test {n} failed. Expected {e} but got {r}")
            all_passed = False
    
    if all_passed:
        print("All tests passed! :D")

def part2_tests():
    all_passed = True

    results = []
    results.append(sliding_window_sums_of([1, 2, 3, 4, 5]))
    results.append(sliding_window_sums_of([5, 4, 3, 2, 1, 0]))
    results.append(sliding_window_sums_of([149, 163, 165, 160, 179]))

    expected = [[6, 9, 12], [12, 9, 6, 3], [477, 488, 504]]

    range_cap = len(results)+1
    for n, r, e in zip(range(1, range_cap), results, expected):
        if (r != e):
            # Is there a way to access the iteration number?
            print(f"Test {n} failed. Expected {e} but got {r}")
            all_passed = False
    
    if all_passed:
        print("All tests passed! :D")

##############################################
### NOTES
##############################################
"""
enumerate() takes a keyword argument called "start" which allows you to choose the number of the first index. This does NOT allow you to start at a specific index. Rather, it allows you to opt not to use zero-indexing

zip() lets you iterate over two sequences at once. Is there a way to ALSO access the index? Yes. A bit janky, but you can iterate over as many sequences as you want with zip, so you can just add range() to count iterations.
"""
