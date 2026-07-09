import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# House outline
x1 = [4, 10]
y1 = [2, 2]

x2 = [10, 10]
y2 = [2, 8]

x3 = [10, 4]
y3 = [8, 8]

x4 = [4, 4]
y4 = [8, 2]

# Roof
x5 = [4, 7]
y5 = [8, 12]

x6 = [7, 10]
y6 = [12, 8]

# Door
x7 = [6.5, 6.5]
y7 = [2, 5]

x8 = [6.5, 7.4]
y8 = [5, 5]

# Window
x9 = [4.8, 4.8, 5.8, 5.8, 4.8]
y9 = [5.4, 6.4, 6.4, 5.4, 5.4]

# Circle decoration
circle = Circle((5.2, 10.4), 0.45, fill=False, edgecolor='black', linewidth=2)

plt.plot(x1, y1)
plt.plot(x2, y2)
plt.plot(x3, y3)
plt.plot(x4, y4)
plt.plot(x5, y5)
plt.plot(x6, y6)
plt.plot(x7, y7)
plt.plot(x8, y8)
plt.plot(x9, y9)
plt.gca().add_patch(circle)

plt.xlim(3.2, 11)
plt.ylim(1.5, 13)
plt.gca().set_aspect('equal', adjustable='box')
plt.axis('off')
plt.show()

