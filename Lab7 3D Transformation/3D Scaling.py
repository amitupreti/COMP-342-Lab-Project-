import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg as agg
import mpl_toolkits.mplot3d as plt3d
import math as math
from math import pi
from numpy import matmul
import numpy as np


Sx = float(input('Enter scaling along x-axis less than 1'))
Sy = float(input('Enter scaling along y-axis less than 1'))
Sz = float(input('Enter scaling along z-axis lessn than 1'))


#The Scaling matrix
Sm = [[Sx, 0, 0, 0],
      [0, Sy, 0, 0],
      [0, 0, Sz, 0],
      [0, 0, 0, 1]]

#The translation matrix
Tm1 = [[1, 0, 0, 0],
      [0, 1, 0, 0],
      [0, 0, 1, 0],
      [0.8, 0, -1, 1]]

#Translation matrix 2
Tm2 = [[1, 0, 0, 0],
      [0, 1, 0, 0],
      [0, 0, 1, 0],
      [-0.8, 0, 1, 1]]

Rm1 = np.matmul(Tm2, Sm)
Rm2 = np.matmul(Rm1, Tm1)

XYZ = np.array([[0.5, 0.5, 1, 1],
                [0, 0.5, 0.5, 1],
                [1, 0.5, 0.5, 1],
                [0, 0, 0.5, 1],
                [1, 0, 0.5, 1]])
XYZ2 = [];

for mat in XYZ:
    a = np.matmul(mat, Rm2)
    XYZ2.append(a)

fig = plt.figure()
fig.set_size_inches(8, 9)
ax = fig.add_subplot(111, projection='3d', aspect='equal')
ax.view_init(azim=120)

#Before scaling
#Line1
xs1 = XYZ[0][0], XYZ[1][0]
ys1 = XYZ[0][1], XYZ[1][1]
zs1 = XYZ[0][2], XYZ[1][2]

line1 = plt3d.art3d.Line3D(xs1, ys1, zs1)
ax.add_line(line1)

#line2
xs2 = XYZ[1][0], XYZ[2][0]
ys2 = XYZ[1][1], XYZ[2][1]
zs2 = XYZ[1][2], XYZ[2][2]
line2 = plt3d.art3d.Line3D(xs2, ys2, zs2)
ax.add_line(line2)

#line3
xs3 = XYZ[1][0], XYZ[3][0]
ys3 = XYZ[1][1], XYZ[3][1]
zs3 = XYZ[1][2], XYZ[3][2]
line3 = plt3d.art3d.Line3D(xs3, ys3, zs3)
ax.add_line(line3)

#line4
xs4 = XYZ[0][0], XYZ[2][0]
ys4 = XYZ[0][1], XYZ[2][1]
zs4 = XYZ[0][2], XYZ[2][2]
line4 = plt3d.art3d.Line3D(xs4, ys4, zs4)
ax.add_line(line4)

#line5
xs5 = XYZ[0][0], XYZ[3][0]
ys5 = XYZ[0][1], XYZ[3][1]
zs5 = XYZ[0][2], XYZ[3][2]
line5 = plt3d.art3d.Line3D(xs5, ys5, zs5)
ax.add_line(line5)

#line6
xs6 = XYZ[4][0], XYZ[2][0]
ys6 = XYZ[4][1], XYZ[2][1]
zs6 = XYZ[4][2], XYZ[2][2]
line6 = plt3d.art3d.Line3D(xs6, ys6, zs6)
ax.add_line(line6)

#line7
xs7 = XYZ[4][0], XYZ[3][0]
ys7 = XYZ[4][1], XYZ[3][1]
zs7 = XYZ[4][2], XYZ[3][2]
line7 = plt3d.art3d.Line3D(xs7, ys7, zs7)
ax.add_line(line7)

#line8
xs8 = XYZ[0][0], XYZ[4][0]
ys8 = XYZ[0][1], XYZ[4][1]
zs8 = XYZ[0][2], XYZ[4][2]
line8 = plt3d.art3d.Line3D(xs8, ys8, zs8)
ax.add_line(line8)

#After scaling
#line1
xs1 = XYZ2[0][0], XYZ2[1][0]
ys1 = XYZ2[0][1], XYZ2[1][1]
zs1 = XYZ2[0][2], XYZ2[1][2]

line1 = plt3d.art3d.Line3D(xs1, ys1, zs1)
ax.add_line(line1)

#line2
xs2 = XYZ2[1][0], XYZ2[2][0]
ys2 = XYZ2[1][1], XYZ2[2][1]
zs2 = XYZ2[1][2], XYZ2[2][2]
line2 = plt3d.art3d.Line3D(xs2, ys2, zs2)
ax.add_line(line2)

#line3
xs3 = XYZ2[1][0], XYZ2[3][0]
ys3 = XYZ2[1][1], XYZ2[3][1]
zs3 = XYZ2[1][2], XYZ2[3][2]
line3 = plt3d.art3d.Line3D(xs3, ys3, zs3)
ax.add_line(line3)

#line4
xs4 = XYZ2[0][0], XYZ2[2][0]
ys4 = XYZ2[0][1], XYZ2[2][1]
zs4 = XYZ2[0][2], XYZ2[2][2]
line4 = plt3d.art3d.Line3D(xs4, ys4, zs4)
ax.add_line(line4)

#line5
xs5 = XYZ2[0][0], XYZ2[3][0]
ys5 = XYZ2[0][1], XYZ2[3][1]
zs5 = XYZ2[0][2], XYZ2[3][2]
line5 = plt3d.art3d.Line3D(xs5, ys5, zs5)
ax.add_line(line5)

#line6
xs6 = XYZ2[4][0], XYZ2[2][0]
ys6 = XYZ2[4][1], XYZ2[2][1]
zs6 = XYZ2[4][2], XYZ2[2][2]
line6 = plt3d.art3d.Line3D(xs6, ys6, zs6)
ax.add_line(line6)

#line7
xs7 = XYZ2[4][0], XYZ2[3][0]
ys7 = XYZ2[4][1], XYZ2[3][1]
zs7 = XYZ2[4][2], XYZ2[3][2]
line7 = plt3d.art3d.Line3D(xs7, ys7, zs7)
ax.add_line(line7)

#line8
xs8 = XYZ2[0][0], XYZ2[4][0]
ys8 = XYZ2[0][1], XYZ2[4][1]
zs8 = XYZ2[0][2], XYZ2[4][2]
line8 = plt3d.art3d.Line3D(xs8, ys8, zs8)
ax.add_line(line8)


canvas = agg.FigureCanvasAgg(fig)
canvas.draw()
renderer = canvas.get_renderer()
raw_data = renderer.tostring_rgb()

import pygame
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((800, 800), DOUBLEBUF)
screen = pygame.display.get_surface()

size = canvas.get_width_height()

surf = pygame.image.fromstring(raw_data, size, "RGB")
screen.blit(surf, (0,0))
pygame.display.flip()
pygame.display.set_caption('3D Scaling')

crashed = False
while not crashed:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True