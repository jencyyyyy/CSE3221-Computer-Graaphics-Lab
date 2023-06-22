import matplotlib.pyplot as plt
import numpy as np

# Generate torus coordinates
theta = np.linspace(0, 2 * np.pi, 100)
phi = np.linspace(0, 2 * np.pi, 50)
theta, phi = np.meshgrid(theta, phi)
R, r = 2, 1  # Major and minor radii
x = (R + r * np.cos(theta)) * np.cos(phi)
y = (R + r * np.cos(theta)) * np.sin(phi)
z = r * np.sin(theta)

# Plot the torus in 2D
plt.subplot(121)
plt.title('Torus (2D)')
plt.axis('equal')
plt.plot(x, y, 'g.')

# Plot the torus in 3D
ax = plt.subplot(122, projection='3d')
ax.set_title('Torus (3D)')
ax.plot_surface(x, y, z, cmap='inferno') #cool,hot,viridis,jet,inferno,magma,cividis

# Display the plots
plt.tight_layout()
plt.show()