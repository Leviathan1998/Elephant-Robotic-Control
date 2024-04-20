import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon

# Subplot image creation
fig, ax = plt.subplots()

# Creating rectangle that represents object before robot
rectangle = Rectangle((0.4, 0.6), 0.2, 0.2, color='red', alpha=0.5)
ax.add_patch(rectangle)

center_x = 0.4 + 0.2 / 2
center_y = 0.6 + 0.2 / 2
ax.text(center_x, center_y, '5', ha='center', va='center', fontsize=12)

# Definition of verticles that represents robot
triangle_vertices = np.array([[0.5, 0.4], [0.6, 0.2], [0.4, 0.2]])

# creating of triangle
triangle = Polygon(triangle_vertices, closed=True, color='yellow', alpha=0.5)
ax.add_patch(triangle)

#Setting range of axes for better visualistion 
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

# Iniciakisation of axes labels
ax.set_xlabel('X')
ax.set_ylabel('Y')

# Visualisation of graph
plt.title('Robot Representation')
plt.grid(True)
plt.show()
