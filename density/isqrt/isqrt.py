from random import randrange
import sys
sys.path.append("..")
from pairs import Pairs

pairs = Pairs()

"""
// Integer square root
// (using linear search, ascending)
unsigned int isqrt(unsigned int y)
{
	// initial underestimate, L <= isqrt(y)
	unsigned int L = 0;

	while ((L + 1) * (L + 1) <= y)
		L = L + 1;

	return L;
}
"""

def isqrt(y: int) -> int:
	L = 0

	while((L+1) * (L+1) <= y):
		pairs.insert(L+1, L+1)
		L += 1

	return L

for i in range(1000):
	y = randrange(1, 20000)
	isqrt(y)

#print(pairs)
pairs.pkl_dump()