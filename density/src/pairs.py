"""The Pairs class is where the multiplication pairs of a selected algorithms are stored.

author: Michal Blazek
organization: BUT FIT
date: 2024

Part of bachelor's thesis called Statistical model checking of approximate computing systems.
"""

import pickle
import numpy as np
from numpy.typing import NDArray
import os
import sys
import pandas as pd
from pathlib import Path

class Pairs(object):
	def __init__(self):
		self.pairs = [] #tuples of a, b pairs


	def __str__(self):
		ret = ""
		for pair in self.pairs:
			ret += f"({pair[0]}, {pair[1]})\n"

		return ret[:-1]

	# SETTERS #

	def insert(self, x: int, y: int):
		x = int(abs(x))
		y = int(abs(y))
		if x <= y:
			self.pairs.append((x, y))
		else:
			self.pairs.append((y, x))


	def from_pkl(self, filename: Path):
		with open(filename,'rb') as f:
			data = pickle.load(f)
			
			if isinstance(data, list):
				self.pairs.extend(data)

	# GETTERS #

	def get_pairs(self) -> list:
		return self.pairs
	

	def get_xvals(self) -> list:
		return [el[0] for el in self.pairs]
	

	def get_yvals(self) -> list:
		return [el[1] for el in self.pairs]
	

	def get_pairs_ndarray(self) -> NDArray:
		return np.array(self.pairs)
	

	def get_xvals_ndarray(self) -> NDArray:
		return np.array([el[0] for el in self.pairs])


	def get_yvals_ndarray(self) -> NDArray:
		return np.array([el[1] for el in self.pairs])
	

	def get_min_val(self) -> int:
		min_x = min(self.get_xvals())
		min_y = min(self.get_yvals())
		
		return min(min_x, min_y)
	

	def get_max_val(self) -> int:
		max_x = max(self.get_xvals())
		max_y = max(self.get_yvals())
		
		return max(max_x, max_y)
	

	def singular_dataframe(self, step=None) -> pd.DataFrame:
		if step is not None:
			data = sorted(self.pairs, key=lambda el: el[0]*el[1])
			data = self.pairs[::step]
		else:
			data = self.pairs
		#data = {"x" : [el[0] for el in self.pairs], "y" : [el[1] for el in self.pairs]}
		df = pd.DataFrame(data=data, columns=['x', 'y'])
		
		return df


	# OUTPUT #

	def pkl_dump(self, filename: str | None = None):
		if filename is None:
			filename = os.path.basename(sys.argv[0])[:-3]
			filename += ".pkl"

		if not filename.endswith(".pkl"):
			raise ValueError("Error: filename has to end with .pkl suffix.")

		with open(filename,'wb') as f:
			pickle.dump(self.pairs, f)
	