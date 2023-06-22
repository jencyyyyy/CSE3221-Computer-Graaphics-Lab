import numpy as np
import matplotlib.pyplot as plt

a = 100  # x-axis radius
b = 100  # y-axis radius
n = 0.5  # exponent

theta = np.linspace(0, 2 * np.pi, 100)
x = a * np.cos(theta) ** (2/n) * np.sign(np.cos(theta))
y = b * np.sin(theta) ** (2/n) * np.sign(np.sin(theta))

plt.plot(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Superellipsoid')
plt.axis('equal')
plt.grid(True)
plt.show()



import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

a = 100  # x-axis radius
b = 100  # y-axis radius
n = 0.5  # exponent

theta = np.linspace(0, 2 * np.pi, 100)
phi = np.linspace(-np.pi/2, np.pi/2, 100)
theta, phi = np.meshgrid(theta, phi)

x = a * np.cos(theta) ** (2/n) * np.sign(np.cos(theta)) * np.cos(phi)
y = b * np.sin(theta) ** (2/n) * np.sign(np.sin(theta)) * np.cos(phi)
z = np.sin(phi) ** (2/n)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='inferno')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Superellipse (3D)')

plt.show()
