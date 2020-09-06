
def produceDivisors(max):
    lowerBound = int(max / 2) + 1
    upperBound = max + 1
    divisors = []

    for m in range(lowerBound, upperBound):
        divisors.append(m)
    return divisors

def isDivisible(n, divisors):
    result = True
    for d in divisors:
        if n % d != 0:
            result = False
    return result

def findSmallestDivisible(maxDivisor):
    '''Find smallest number that can be divided by each of the numbers
    from 1 to maxDivisor
    '''
    divisors = produceDivisors(maxDivisor)

    candidate = maxDivisor
    while candidate < 1000000000:
        if isDivisible(candidate, divisors):
            return candidate
        else:
            candidate += maxDivisor

result = findSmallestDivisible(20)
print(result)
