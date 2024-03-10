import sys
sys.path.append("..")
from pairs import Pairs

pairs = Pairs()

def factorial(m: int) -> int:
	ret = 1
	for i in range(2, m+1):
		pairs.insert(ret, i)
		ret *= i

	return ret

for i in range(7):
	res = factorial(i)
	print(res)

pairs.pkl_dump()
print(pairs)
print(f"max: {pairs.get_max_val()}")