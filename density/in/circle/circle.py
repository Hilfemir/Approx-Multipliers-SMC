from random import randrange
from math import sqrt
import sys
sys.path.append("..")
from pairs import Pairs

pairs = Pairs()

#Naive point by point circle rasterization
"""
IZG C implementation
CircleByPoints(int cx, int cy, int R)
{
	int x = 0, y = R;
	while (x <= y)
	{
		draw_pixel_circle(x + cx, y + cy);
		x++;
		y = round(sqrt(R*R – x*x));
	}
}
"""

def circle(cx: int, cy: int, r: int):
	x = 0
	y = r

	while(x <= y):
		print(x+cx, y+cy) #draw pixel
		x += 1

		pairs.insert(r, r)
		pairs.insert(x, x)
		y = int(round(sqrt(r*r - x*x)))

for i in range(5, 100):
	x = randrange(0, 50)
	y = randrange(0, 50)
	r = i + randrange(0,150)
	circle(x, y, r)

pairs.pkl_dump()
print(pairs)
print(f"max: {pairs.get_max_val()}")