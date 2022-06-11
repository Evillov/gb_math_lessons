import itertools
import math

Ank = 0
for i in itertools.permutations("123456789", 2):
    print(i)
    Ank += 1

print(Ank)
print(Ank - 9 )