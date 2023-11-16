import matplotlib.pyplot as plt
import numpy as np
from numpy.typing import NDArray
import argparse
import seaborn as sns
import pandas as pd
from pathlib import Path

from pairs import Pairs
from stats import Stats as st
from utils import find_data_file, axis_setup


# parse args #
parser = argparse.ArgumentParser(
                    prog='graph_isolated.py',
                    description='Plots isolated probability densities for x and y values.'
					)

parser.add_argument(
	'dirname',
	help="Name of the directory which contains a .pkl file with the data."
	)

parser.add_argument(
	'--xmin',
	default=None,
	type=int,
	help="Minimal value on the X axis."
	)

parser.add_argument(
	'--xmax',
	default=None,
	type=int,
	help="Maximal value on the X axis."
	)

parser.add_argument(
	'--ymin',
	default=0.0,
	type=float,
	help="Minimal value on the Y axis."
	)

parser.add_argument(
	'--ymax',
	default=1.0,
	type=float,
	help="Maximal value on the Y axis."
	)

args = parser.parse_args()
dirname = args.dirname
xmin = args.xmin
xmax = args.xmax
ymin = args.ymin
ymax = args.ymax

try:
	filename = find_data_file(dirname)
except Exception as e:
	print("Error: directory not found.")
	exit(1)

#load data from the pickle file
data = Pairs()
data.from_pkl(filename)

xmin, xmax = axis_setup(data, xmin, xmax)

df = data.singular_dataframe()

df.plot(kind='density', xlim=(xmin, xmax))

plt.show()
