# Loop statements may have an else clause; it is executed when the loop terminates through exhaustion of the iterable (with for) or when the condition becomes false (with while), but not when the loop is terminated by a break statement. 

# Prints prime numbers between from 2 to 9
for i in range(2, 10):
    # Divides i by all numbers less than it
    for x in range(2, n):
        # If i is not a prime
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            # Totally stops loop, skipping else statment
            break
    # Only runs when break does not occur
    else:
        print(x, 'is a prime number')

