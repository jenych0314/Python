import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
# import pandas as pd

def f(x,y):
    z = (2*x - 7)**2 - 28 - 4*(2*x - 3)*(2*y - 2) + 4*(2*y - 3)
    return z

x = np.linspace(1, 10, 21)
y = np.linspace(1, 10, 21)

X, Y = np.meshgrid(x, y)
# temp = np.zeros((len(x), len(y)))
# for i in range(xn):
#     for j in range(xn):
#         temp[j, i] = f(x[i], y[j])

fig = plt.figure()
fig.set_size_inches(15, 15)
plt.scatter(X, Y)

# print(np.round(temp, 1))

# plt.figure(figsize = (50,50))
# plt.gray()
# plt.pcolor(temp)
# plt.colorbar()
# plt.show()
# plt.plot(x, y, z)
# plt.show()

# xx, yy = np.meshgrid(x, y)

Z = f(X, Y)

# plt.figure(figsize = (10, 10))
# ax = plt.subplot(1,1,1,projection = '3d')
# ax.plot_surface(xx,yy,temp)
# plt.show()

# fig = plt.figure()
# fig.set_size_inches(15, 15)
# ax = plt.axes(projection='3d')
# surf = ax.contour3D(X, Y, Z, 50, cmap=cm.coolwarm)
# fig.colorbar(surf, shrink=0.5, aspect=5)
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_zlabel('z')
# ax.set_title('3D contour')
# plt.show()

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
fig.set_size_inches(15, 15)
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)
fig.colorbar(surf, shrink=0.5, aspect=5)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('3D contour')
plt.show()