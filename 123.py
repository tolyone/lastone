import os
import matplotlib as plt
from mpl_toolkits.mplot3d import Axes3D

x = []
y = []
z = []
list = []

for e in os.listdir('0.0013 MeV'):
    list.append('0.0013 MeV' + '/' + e)
    e = e.split()
    y.append(float(e[0]))

for name in list:
    f = open(name, 'r')
    i = 0
    for e in f:
        e = e.split()
        if e.__len__() == 1 and str(e[0]) == '1e+09':
            i += 1
        elif e.__len__() == 2 and i == 1:
            x.append(e[0])
            z.append(e[1])

        if e.__len__() == 1 and str(e[0]) == '1e+11':
            i -= 1


print(x.__len__())
print(z.__len__())
print(y.__len__())