from random import randrange
import sys
sys.path.append("..")
from pairs import Pairs

pairs = Pairs()

#Ellipse rasterization midpoint algorithm
"""
IZG C implementation
ElipseMid(int A, int B)
{ 
	int x = 0, y = B, AA = A*A, BB = B*B;
	int P = BB – AA*B + AA/4;
	while (AA*y > BB*x)
	{ 
		draw_pixel_elipse(x, y);
		if (P < 0)
			{ P += BB*(2*x+3); x++; }
		else
			{ P += BB*(2*x+3) + AA*(2-2*y); x++; y--; }
	}
	P = BB*(x+0,5)*(x+0,5)+AA*(y-1)*(y-1)-AA*BB;
	while (y >= 0)
	{ 
		draw_pixel_elipse(x, y);
		if (P < 0)
			{ P += BB*(2*x+2) + AA*(3-2*y); x++; y--; }
		else
			{ P += AA*(3-2*y); y--; }
	}
}
"""

def ellipse(A: int, B: int):
	x = 0
	y = B

	pairs.insert(A, A)
	AA = A*A

	pairs.insert(B, B)
	BB = B*B

	pairs.insert(AA, B)
	P = int(BB - AA * B + AA/4)

	while(AA * y > BB * x):
		pairs.insert(AA, y)
		pairs.insert(BB, x)

		#print(x, y) #draw pixel

		if (P < 0):
			pairs.insert(2, x)
			pairs.insert(BB, 2*x + 3)
			P += BB * (2*x + 3)
			x += 1
		else:
			pairs.insert(2, x)
			pairs.insert(BB, 2*x + 3)
			pairs.insert(2, y)
			pairs.insert(AA, 2 - 2*y)
			P += BB * (2*x + 3) + AA * (2 - 2*y)
			x += 1
			y -= 1

	pairs.insert(AA, y-1)
	pairs.insert(AA * (y-1), y-1)
	pairs.insert(AA, BB)
	P = BB * (x+0.5) * (x+0.5) + AA * (y-1) * (y-1) - AA * BB

	while(y >= 0):
		#print(x, y) #draw pixel

		if (P < 0):
			pairs.insert(BB, 2*x+2)
			pairs.insert(2, x)
			pairs.insert(AA, 3-2*y)
			pairs.insert(2, y)
			P += BB*(2*x+2) + AA*(3-2*y)
			x += 1
			y += 1
		else:
			pairs.insert(AA, 3-2*y)
			pairs.insert(2, y)
			P += AA*(3-2*y)
			y -= 1


for i in range(1000):
	x = randrange(1, 10)
	y = x + randrange(1, 10)
	ellipse(x, y)


pairs.pkl_dump()