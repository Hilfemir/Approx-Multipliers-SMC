import sys
sys.path.append("..")
from pairs import Pairs

pairs = Pairs()

#Fuss-Catalan Number
# A_m(p,r) = r/m! * Prod from i=1 to m-1: (m*p + r - i)

# m! = Prod from i=1 to m: i

def factorial(m: int) -> int:
	ret = 1
	for i in range(2, m+1):
		pairs.insert(ret, i)
		ret *= i

	return ret


def fusscatal(m: int, p: int, r: int) -> float:
	if m == 0:
		return 1.0
	
	if m == 1:
		return float(r)

	left = r / factorial(m)

	pairs.insert(m, p)
	mp = m * p
	right = mp + r - 1

	for i in range(2, m):
		tmp = mp + r - i
		pairs.insert(right, tmp)
		right *= tmp

	return left * right


for i in range(10):
	res = fusscatal(i, 1, 4)
	print(res)

pairs.pkl_dump()