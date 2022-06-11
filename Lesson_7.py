# import numpy
import numpy as np

a = np.array([1, 5, 0], float)
b = np.array([2, 8, 7], float)
c = np.array([7, 1.5, 3], float)

cross_ab = np.cross(a, b) # - векторное произведение
print(np.inner(cross_ab, c)) # - скалярное произведение и вывод

