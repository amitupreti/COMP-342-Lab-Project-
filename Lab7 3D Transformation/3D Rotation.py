import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg as agg
import numpy as np
import mpl_toolkits.mplot3d as plt3d
import math as math
from math import pi
from numpy import matmul
import numpy as np

x1 = float(input('Enter ending x-axis of a line from origin'))
y1 = float(input('Enter ending y-axis of a line from origin'))
z1 = float(input('Enter ending z-axis of a line from origin'))
Rx = float(input('Enter the angle of rotation along x-axis'))
Ry = float(input('Enter the angle of rotation along y-axis'))
Rz = float(input('Enter the angle of rotation along z-axis'))
radx = (pi/180) * Rx
rady = (pi/180) * Ry
radz = (pi/180) * Rz

#The translation matrix
Tm = [[1, 0, 0, 0],
      [0, 1, 0, 0],
      [0, 0, 1, 0],
      [-x1, -y1, -z1, 1]]

#Rotation matrix along x-axis
Rmx = [[1, 0, 0, 0],
       [0, math.cos(radx), math.sin(radx), 0],
       [0, -(math.sin(radx)), math.cos(radx), 0],
       [0, 0, 0, 1]]

#Rotation matrix along y-axis
Rmy = [[math.cos(rady), 0, -(math.sin(rady)), 0],
       [0, 1, 0, 0],
       [math.sin(rady), 0, math.cos(rady), 0],
       [0, 0, 0, 1]]

#Rotation matrix along z-axis
Rmz = [[math.cos(radz), math.sin(radz), 0, 0],
       [-(math.sin(radz)), math.cos(radz), 0, 0],
       [0, 0, 1, 0],
       [0, 0, 0, 1]]

line = [x1, y1, z1, 1]

#Rotaion along x-axis
x2, y2, z2, no = np.matmul(line, Rmx)

#Rotated along y-axis
x3, y3, z3, no = np.matmul(line, Rmy)

#Rotated along z-axis
x4, y4, z4, no = np.matmul(line, Rmz)


XYZ = np.array([[0.3, 0.3, 0.3],
                [x1, y1, z1],
                [x2, y2, z2],
                [x3, y3, z3],
                [x4, y4, z4]])

fig = plt.figure()
fig.set_size_inches(8, 9)
ax = fig.add_subplot(111, projection='3d', aspect='equal')
ax.view_init(azim=120)

#Initial line
xs = XYZ[0][0], XYZ[1][0]
ys = XYZ[0][1], XYZ[1][1]
zs = XYZ[0][2], XYZ[1][2]
line = plt3d.art3d.Line3D(xs, ys, zs)
ax.add_line(line)

#Rotated along x-axis
xs = XYZ[0][0], XYZ[2][0]
ys = XYZ[0][1], XYZ[2][1]
zs = XYZ[0][2], XYZ[2][2]
line = plt3d.art3d.Line3D(xs, ys, zs)
ax.add_line(line)

#Rotated along y-axis
xs = XYZ[0][0], XYZ[3][0]
ys = XYZ[0][1], XYZ[3][1]
zs = XYZ[0][2], XYZ[3][2]
line = plt3d.art3d.Line3D(xs, ys, zs)
ax.add_line(line)

#Rotated along z-axis
xs = XYZ[0][0], XYZ[4][0]
ys = XYZ[0][1], XYZ[4][1]
zs = XYZ[0][2], XYZ[4][2]
line = plt3d.art3d.Line3D(xs, ys, zs)
ax.add_line(line)

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
pygame.display.set_caption('3D Rotation')

crashed = False
while not crashed:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True