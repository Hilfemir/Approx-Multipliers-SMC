import matplotlib.pyplot as plt
import numpy as np

import sys
sys.path.append("..")
from pairs import Pairs

pairs = Pairs()

def factorial(x: int) -> int:
	if x in [0, 1]:
		return 1
	
	ret = x
	for i in range(x-1, 0, -1):
		#pairs.insert(i, ret)
		ret *= i

	return ret


def binom_coeff(n: int, k: int) -> float:
	f_n = factorial(n)
	f_k = factorial(k)
	f_nmk = factorial(n-k)
	pairs.insert(f_nmk, f_k)
	ret = f_n / (f_k * f_nmk)
	return ret

for i in range(17):
	for j in range(17):
		if i >= j:
			res = binom_coeff(i, j)

#pairs.pkl_dump("./binom.pkl")
print(pairs)