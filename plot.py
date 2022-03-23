import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 11, 1)
y = x
print('Values of x: ', x)
print('Values of y: ', y)
plt.plot(x, y)
plt.title("Identity Function")
plt.xlabel("Values of x")
plt.ylabel("Values of y")
plt.show()