import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8, 5])
ypoints = np.array([2 ,7, 3])

retx = np.array([4,4])
rety = np.array([8,8])

plt.plot(xpoints, ypoints)
plt.show()

plt.plot(retx)
plt.plot(rety)
plt.show()