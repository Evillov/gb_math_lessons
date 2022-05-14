import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 900)

plt.plot(x, np.cos(x), label='y(k,x), k=1')
plt.plot(x, np.cos(x * 4), label='y(k,x), k=4')

plt.show()
