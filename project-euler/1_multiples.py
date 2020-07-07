def multiples(max):
    sum = 0
    for n in range(max):
        if n % 3 == 0 or n % 5 == 0:
            sum += n
    return sum

print(multiples(1000))
