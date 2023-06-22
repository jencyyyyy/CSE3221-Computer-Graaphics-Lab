import matplotlib.pyplot as plt
import numpy as np


theta = np.linspace(0, 2 * np.pi, 100)
phi = np.linspace(0, np.pi, 50)

x = []
y = []
z = []

for t in theta:
    for p in phi:
        x.append(2 * np.sin(p) * np.cos(t))
        y.append(np.sin(p) * np.sin(t))
        z.append(np.cos(p))

x = np.array(x).reshape((50, 100))
y = np.array(y).reshape((50, 100))
z = np.array(z).reshape((50, 100))


max_radius = max(2, 1, 1)


plt.subplot(121)
plt.title('Ellipsoid (2D)')
plt.xlabel('X')
plt.ylabel('Y')
plt.axis('equal')
plt.grid(True)
plt.plot(x, y, 'b.')


ax = plt.subplot(122, projection='3d')
ax.set_title('Ellipsoid (3D)')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')


ax.set_xlim(-max_radius, max_radius)
ax.set_ylim(-max_radius, max_radius)
ax.set_zlim(-max_radius, max_radius)

ax.plot_surface(x, y, z, cmap='cool')

# Display the plots
plt.tight_layout()
plt.show()
