# A file where I test new things

for x in range(1, 11):
   print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
   print(repr(x*x*x).rjust(10))
