import numpy as np
import matplotlib.pyplot as plt

rx = 2  # x-axis radius
ry = 1  # y-axis radius
s = 1   # shape parameter

theta = np.linspace(0, 2 * np.pi, 1000)
x = rx * np.sign(np.cos(theta)) * np.abs(np.cos(theta))**(2/s)
y = ry * np.sign(np.sin(theta)) * np.abs(np.sin(theta))**(2/s)

plt.plot(x, y)
plt.gca().set_aspect('equal', adjustable='box')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Superellipsed')
plt.grid(True)
plt.show()
