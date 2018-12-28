import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

x = []
y = []
z = []
L = []

for e in os.listdir('0.0013 MeV'):
    L.append('0.0013 MeV' + '/' + e)
    e = e.split()
    z.append(float(e[0]))

for name in L:
    f = open(name, 'r')
    i = 0
    for e in f:
        e = e.split()
        if e.__len__() == 1 and str(e[0]) == '1e+09':
            i += 1
        elif e.__len__() == 2 and i == 1:
            x.append(e[0])
            y.append(e[1])

        if e.__len__() == 1 and str(e[0]) == '1e+11':
            i -= 1

fig = plt.figure(figsize=(8, 3))
ax1 = fig.add_subplot(121, projection='3d')
ax1 = fig.add_subplot(122, projection='3d')

_x = np.array([xi for xi in x])
_y = np.array([yi for yi in y])
_xx, _yy = np.meshgrid(_x, _y)
X, Y = _xx.ravel(), _yy.ravel()

for e in range(100,10001):
    z.append(z[e-100])

top = z
bottom = np.zeros_like(top)
width = depth = 1

ax1.bar3d(X, Y, bottom, width, depth, top, shade=True)
ax1.set_title('Volumed')

plt.show()
print(x.__len__())
print(z.__len__())
print(y.__len__())