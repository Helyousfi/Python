from optparse import Values
from re import I


def myGenerator(n):
    for i in range(n):
        yield i**3

values = myGenerator(500)

print(next(values))
print(next(values))
print(next(values))
print(next(values))
