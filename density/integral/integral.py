import numpy as np
from pathlib import Path

import sys
sys.path.append("..")
from pairs import Pairs

pairs = Pairs()

def f(x):
	pairs.insert(x, x)
	return x * x + 2

def integrate(a: float, b: float, steps: int = 1000):
	X = np.linspace(a, b, steps)
	
	sum = 0

	for i, x in enumerate(X):
		if i == 0:
			continue
		
		a1 = int((x - X[i-1]))
		a2 = f(int((x + X[i-1]) / 2))
		pairs.insert(a1, a2)

		sum += a1 * a2

	return sum

res = integrate(0, 100, 101)

pairs.pkl_dump(filename="integral2.pkl")
