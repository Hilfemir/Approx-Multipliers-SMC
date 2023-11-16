import numpy as np
from numpy.typing import NDArray
import pandas as pd
import matplotlib as plt

class Stats(object):
	def __init__(self):
		pass
	
	# STATISTICAL FUNCTIONS #

	@classmethod
	def bincount(cls, values: list, maxkey: int | None = None) -> dict:
		bins = {}

		for element in values:
			if maxkey is not None and element > maxkey:
				continue

			if element not in bins.keys():
				bins[element] = 1
			else:
				bins[element] += 1

		return bins

	@classmethod
	def density(cls, values: list, maxkey: int | None = None) -> dict:
		total_amount = len(values)
		bins = cls.bincount(values, maxkey)

		dens = {key : val/total_amount for key, val in bins.items()}
		return dens
	
	@classmethod
	def dict_to_arrays(cls, d: dict) -> tuple[NDArray, NDArray]:
		ret1 = np.array(list(d.keys()))
		ret2 = np.array(list(d.values()))

		return ret1, ret2
	
	@classmethod
	def single_coords(
			cls,
			pairs: list,
			range_left: int | None = None,
			range_right: int | None = None
			) -> tuple[NDArray, NDArray, NDArray] | None:
		
		xdens = cls.density([el[0] for el in pairs], range_right)
		ydens = cls.density([el[1] for el in pairs], range_right)
		
		if range_left is None:
			range_left = min(xdens.keys())

		if range_right is None:
			range_right = max(xdens.keys())

		xaxis = np.arange(range_left, range_right+1)

		x = np.zeros_like(xaxis, dtype=float)
		keys, vals = cls.dict_to_arrays(xdens)
		x[keys] = np.array(vals)

		y = np.zeros_like(xaxis, dtype=float)
		keys, vals = cls.dict_to_arrays(ydens)
		y[keys] = np.array(vals)

		return x, y, xaxis
	
	@classmethod
	def singular(
			cls,
			pairs: list,
			range_left: int | None = None,
			range_right: int | None = None
			) -> tuple[list, list]:
		
		if range_left is not None and range_right is not None:
			x = np.array([el[0] for el in pairs if range_left <= el[1] <= range_right])
			y = np.array([el[1] for el in pairs if range_left <= el[1] <= range_right])
		elif range_left is not None:
			x = np.array([el[0] for el in pairs if range_left <= el[1]])
			y = np.array([el[1] for el in pairs if range_left <= el[1]])
		elif range_right is not None:
			x = np.array([el[0] for el in pairs if el[1] <= range_right])
			y = np.array([el[1] for el in pairs if el[1] <= range_right])
		else:
			x = np.array([el[0] for el in pairs])
			y = np.array([el[1] for el in pairs])

		return x, y
