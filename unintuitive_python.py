# tested on Python 3.11

"""
Function parameters with mutable Defaults

The Default is evaluated only once and bound to the function when defined, not each time the function is called.
You can set the default to None here instead
"""


def foobar(list=[]):
    list.append(2)
    return list


a = foobar()
print(a)  # [2]
b = foobar()
print(b)  # [2,2]


"""
Python Small Integer caching - run from a python shell

Python caches small integers (integers between -5 and 256)
When a and b are both 256 they refer to same memory location
When a and b are both 257 they are no longer in the range of small integers

The 'is' opterator is used to test if two variables refer to the same object.
The '==' operator is used to compare the equality of objects
"""
a = 256
b = 256
a is b  # True
a = 257
b = 257
a is b  # False
a == b  # True


"""
Computer Floating Point Math
Computers use a base-2 system - binary
Humans use a base-10 system - 10 fingers.

*Not exclusive to Python
"""
print(0.1 + 0.2)  # 0.30000000000000004
a = 0.1 + 0.2
b = 0.3
print(a is b) # False
print(a == b) # False

print(0.9 + 0.8)  # 1.7000000000000002

from decimal import *
print(Decimal(0.1) + Decimal(0.2)) #Decimal('0.3000000000000000166533453694')