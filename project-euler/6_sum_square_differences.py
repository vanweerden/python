from sys import argv

if len(argv) != 2:
    print('usage: 6_sum_square_difference.py [positive_integer]')
else:
    limit = int(argv[1])

# Elegant way to sum(range(1, limit+1))
sum = int(limit * (limit + 1) / 2)

# Elegant way to sum squares
sum_square = int((2 * limit + 1) * (limit + 1) * limit / 6)

print(sum**2 - sum_square)
