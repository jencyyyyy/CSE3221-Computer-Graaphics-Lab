import matplotlib.pyplot as plt
import matplotlib.patches as patches


fig, ax = plt.subplots()


triangle = patches.Polygon([[0.1, 0.2], [0.1, 0.7], [0.8, 0.2]], closed=True, facecolor='blue')
ax.add_patch(triangle)


circle = patches.Circle((0.5, 0.5), 0.3, facecolor='red')
ax.add_patch(circle)


rectangle = patches.Rectangle((0.5, 0.2), 0.4, 0.5, facecolor='green')
ax.add_patch(rectangle)


ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')

plt.show()
