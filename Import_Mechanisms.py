import math

print("Using import module:")
print(math.sqrt(25))

import math as m

print("\nUsing import module as alias:")
print(m.factorial(5))

from math import sqrt

print("\nUsing from module import:")
print(sqrt(36))

from math import factorial as fact

print("\nUsing from module import as alias:")
print(fact(5))