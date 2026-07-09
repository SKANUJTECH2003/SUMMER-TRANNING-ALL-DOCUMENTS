import matplotlib.pyplot as plt
import numpy as np

# Coordinate geometry graph
x = np.linspace(-5, 8, 200)
y = 2 * x - 3

plt.figure(figsize=(7, 5))
plt.plot(x, y, color='royalblue', linewidth=2, label='Line: y = 2x - 3')

# Points on the graph
points = {
    'A': (1, -1),
    'B': (3, 3),
    'C': (5, 7),
}

for name, (px, py) in points.items():
    plt.scatter(px, py, color='red', s=80)
    plt.text(px + 0.1, py + 0.1, name, fontsize=11, color='darkred')

# Draw connecting lines to form a triangle
x_coords = [points['A'][0], points['B'][0], points['C'][0], points['A'][0]]
y_coords = [points['A'][1], points['B'][1], points['C'][1], points['A'][1]]
plt.plot(x_coords, y_coords, color='green', linestyle='--', linewidth=1.5)

# Axes and formatting
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.grid(True, alpha=0.3)
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.title('Coordinate Geometry Graph')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.xlim(-5, 8)
plt.ylim(-5, 10)
plt.legend()
plt.tight_layout()
plt.savefig("coordinate_geometry_graph.png", dpi=300)
plt.show()
