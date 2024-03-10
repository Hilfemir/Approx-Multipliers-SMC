import matplotlib.pyplot as plt
import random
import numpy as np
import sys
sys.path.append("..")
from pairs import Pairs

pairs = Pairs()

#Scanline fill algorithm used to fill pixels between 2 endpoints
#The code below was generated using ChatGPT

def draw_line(img, x0, y0, x1, y1):
	dx = abs(x1 - x0)
	dy = abs(y1 - y0)
	steep = dy > dx

	if steep:
		x0, y0 = y0, x0
		x1, y1 = y1, x1

	if x0 > x1:
		x0, x1 = x1, x0
		y0, y1 = y1, y0

	dx = abs(x1 - x0)
	dy = abs(y1 - y0)
	error = 0
	y = y0
	ystep = 1 if y0 < y1 else -1

	for x in range(x0, x1 + 1):
		img[y, x] = 1 if steep else 1
		error += dy

		pairs.insert(2, error)
		if 2 * error >= dx:
			y += ystep
			error -= dx

def scanline_fill(img, vertices):
	min_y = int(np.min(vertices[:, 1]))
	max_y = int(np.max(vertices[:, 1]))

	for y in range(min_y, max_y + 1):
		intersections = []
		for i in range(len(vertices)):
			x0, y0 = vertices[i]
			x1, y1 = vertices[(i + 1) % len(vertices)]
			if (y0 <= y < y1) or (y1 <= y < y0):
				
				pairs.insert((y-y0),(x1-x0))
				x_intersection = int(x0 + (y - y0) * (x1 - x0) / (y1 - y0))
				intersections.append(x_intersection)

		intersections.sort()

		for i in range(0, len(intersections), 2):
			x0 = max(0, intersections[i])
			x1 = min(img.shape[1] - 1, intersections[i + 1])
			img[y, x0:x1 + 1] = 1

def random_vertices(size: int = 20):
	len = random.randint(3, 8)
	vertices = []
	for i in range(len):
		x = random.randint(0, size-1)
		y = random.randint(0, size-1)
		vertices.append([x, y])

	return np.array(vertices)

for i in range(1000):
	size = 180
	img = np.zeros((size, size))
	#vertices = np.array([[2, 1], [8, 1], [5, 5], [2, 8], [8, 8]])
	vertices = random_vertices(size)

	for i in range(len(vertices)):
		x0, y0 = vertices[i]
		x1, y1 = vertices[(i + 1) % len(vertices)]
		draw_line(img, x0, y0, x1, y1)

	scanline_fill(img, vertices)

	#plt.imshow(img, cmap='gray', origin='lower')
	#plt.show()

pairs.pkl_dump()
print(pairs)
print(f"max: {pairs.get_max_val()}")