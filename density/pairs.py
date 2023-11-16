import pickle
import numpy as np
from numpy.typing import NDArray
import os
import sys
import pandas as pd

from stats import Stats as st

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
		x = abs(x)
		y = abs(y)
		if x <= y:
			self.pairs.append((x, y))
		else:
			self.pairs.append((y, x))


	def from_pkl(self, filename: str):
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
	

	def singular_dataframe(self) -> pd.DataFrame:
		data = {"x" : [el[0] for el in self.pairs], "y" : [el[1] for el in self.pairs]}
		df = pd.DataFrame(data=data)
		
		return df


	def heatmap_dataframe(self) -> pd.DataFrame:
		pairs = self.get_pairs()
		
		dens = st.density(pairs)
		
		max_val = self.get_max_val()
		
		axis_range = np.arange(max_val+1)
		
		percentages = np.zeros((max_val+1, max_val+1))
		for key, value in dens.items():
			x, y = key
			percentages[x, y] = value

		df = pd.DataFrame(data={"x" : axis_range, "y" : axis_range})
		df.pivot_table(index='x', columns='y', values=percentages)
		#print(df)


	# OUTPUT #

	def pkl_dump(self, filename: str | None = None):
		if filename is None:
			filename = os.path.basename(sys.argv[0])[:-3]
			filename += ".pkl"

		if not filename.endswith(".pkl"):
			raise ValueError("Error: filename has to end with .pkl suffix.")

		with open(filename,'wb') as f:
			pickle.dump(self.pairs, f)
	