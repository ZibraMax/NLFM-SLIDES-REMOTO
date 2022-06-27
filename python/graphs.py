import numpy as np
import matplotlib.pyplot as plt


def ate(p): return np.exp(-p)


def atei(x): return -np.log(x)


maxr = 6
n = 11
x1 = atei(np.linspace(ate(0), ate(maxr), n)).tolist()
x2 = (-atei(np.linspace(ate(maxr), ate(0), n))).tolist()

_x = np.array(x2+x1[1:])

xx, yy = np.meshgrid(_x, _x)
x = xx.flatten()
y = yy.flatten()
p = (x**2+y**2)**0.5
z = ate(p)
print(len(z))
plt.figure().add_subplot(projection='3d').plot_trisurf(x, y, z, cmap='rainbow')
plt.show()
