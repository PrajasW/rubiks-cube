import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(3, 3))
ax = fig.add_subplot(111, projection='3d')

x4 = 0
y4 = 0
z4 = 3
dx4 = 3
dy4 = 3
dz4 = 0.01
ax.bar3d(x4, y4, z4, dx4, dy4, dz4, color='yellow', shade=True)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

x1 = 0
y1 = 0
z1 = 0
dx1 = 0.01
dy1 = 3
dz1 = 3
ax.bar3d(x1, y1, z1, dx1, dy1, dz1, color='red', shade=True)

x2 = 0
y2 = 0
z2 = 0
dx2 = 3
dy2 = 0.01
dz2 = 3
ax.bar3d(x2, y2, z2, dx2, dy2, dz2, color='green', shade=True)

x6 = 3
y6 = 0
z6 = 0
dx6 = 0.01
dy6 = 3
dz6 = 3
ax.bar3d(x6, y6, z6, dx6, dy6, dz6, color='orange', shade=True)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

x5 = 0
y5 = 3
z5 = 0
dx5 = 3
dy5 = 0.01
dz5 = 3
ax.bar3d(x5, y5, z5, dx5, dy5, dz5, color='blue', shade=True)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')


x3 = 0
y3 = 0
z3 = 0
dx3 = 3
dy3 = 3
dz3 = 0.01
ax.bar3d(x3, y3, z3, dx3, dy3, dz3, color='white', shade=True)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Rubiks Cube')

plt.show()