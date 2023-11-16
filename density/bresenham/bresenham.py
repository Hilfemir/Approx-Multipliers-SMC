from random import randrange
import sys
sys.path.append("..")
from pairs import Pairs

pairs = Pairs()

#Bresenham's line algorithm
"""
IZG C implementation
LineBres(int x1, int y1, int x2, int y2)
{
	int dx = x2-x1, dy = y2-y1;
	int P = 2*dy – dx;
	int P1 = 2*dy, P2 = P1 - 2*dx;
	int y = y1;
	for (int x = x1; x <= x2; x++)
	{
		draw_pixel( x, y);
		if (P >= 0)
			{ P += P2; y++; }
		else
			P += P1;
	}
}
"""

def line_bres(x1: int, y1: int, x2: int, y2: int):
	dx = x2 - x1
	dy = y2 - y1

	pairs.insert(2, dy)
	P = 2 * dy - dx

	pairs.insert(2, dy)
	P1 = 2 * dy

	pairs.insert(2, dx)
	P2 = P1 - 2*dx

	y = y1
	for x in range(x1, x2+1):
		#print(x, y) #draw pixel
		if (P >= 0):
			P += P2
			y += 1
		else:
			P += P1

for i in range(1000):
	x1 = randrange(0, 100)
	x2 = randrange(101, 200)
	y1 = randrange(0, 50)
	y2 = randrange(51, 100)
	line_bres(x1, y1, x2, y2)

pairs.pkl_dump()