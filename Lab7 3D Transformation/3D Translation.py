import matplotlib.pyplot as plt
import matplotlib.backends.backend_agg as agg
import mpl_toolkits.mplot3d as plt3d
import math as math
from math import pi
from numpy import matmul
import numpy as np


x1 = float(input('Enter ending x-axis of a line from origin'))
y1 = float(input('Enter ending y-axis of a line from origin'))
z1 = float(input('Enter ending z-axis of a line from origin'))
Tx = float(input('Enter translation along x-axis'))
Ty = float(input('Enter translation along y-axis'))
Tz = float(input('Enter translation along z-axis'))


#The translation matrix
Tm = [[1, 0, 0, 0],
      [0, 1, 0, 0],
      [0, 0, 1, 0],
      [Tx, Ty, Tz, 1]]

point0 = [0, 0, 0, 1]
point1 = [x1, y1, z1, 1]

#Tranlating origin
x0, y0, z0, no = np.matmul(point0, Tm)

#Translating eding point
x2, y2, z2, no = np.matmul(point1, Tm)

XYZ = np.array([[0, 0, 0],
                [x1, y1, z1],
                [x0, y0, z0],
                [x2, y2, z2]])

fig = plt.figure()
fig.set_size_inches(8, 9)
ax = fig.add_subplot(111, projection='3d', aspect='equal')
ax.view_init(azim=120)


#Initial line
xs1 = XYZ[0][0], XYZ[1][0]
ys1 = XYZ[0][1], XYZ[1][1]
zs1 = XYZ[0][2], XYZ[1][2]

line1 = plt3d.art3d.Line3D(xs1, ys1, zs1)
ax.add_line(line1)

#Translated Line
xs = XYZ[2][0], XYZ[3][0]
ys = XYZ[2][1], XYZ[3][1]
zs = XYZ[2][2], XYZ[3][2]
line2 = plt3d.art3d.Line3D(xs, ys, zs)
ax.add_line(line2)

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
pygame.display.set_caption('3D Translation')

crashed = False
while not crashed:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			crashed = True