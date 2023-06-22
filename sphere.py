import math
import matplotlib.pyplot as plt

# Generate sphere coordinates

theta = [2 * math.pi * i / 100 for i in range(501)]
phi = [math.pi * i / 50 for i in range(251)]
x = []
y = []
z = []
radius = 1

for p in phi:
    for t in theta:
        x.append(radius * math.sin(p) * math.cos(t))
        y.append(radius * math.sin(p) * math.sin(t))
        z.append(radius * math.cos(p))

# Plot the sphere in 2D
plt.subplot(121)
plt.title('Sphere (2D)')
plt.xlabel('X')
plt.ylabel('Y')
plt.axis('equal')
plt.grid(True)
plt.plot(x, y, 'b.')

# Plot the sphere in 3D
ax = plt.subplot(122, projection='3d')
ax.set_title('Sphere (3D)')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.plot_trisurf(x, y, z, cmap='viridis')

# Display the plots
plt.tight_layout()
plt.show()
