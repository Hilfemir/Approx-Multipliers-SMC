import matplotlib.pyplot as plt
import numpy as np
from numpy.typing import NDArray
import argparse
import seaborn as sns
import pandas as pd
from pathlib import Path
from scipy.ndimage import gaussian_filter

from pairs import Pairs
from stats import Stats as st
from utils import find_data_file, fig_setup, get_range, bins_setup
	
# parse args #
parser = argparse.ArgumentParser(
                    prog='graph_heatmap.py',
                    description='Plots the heatmap of probabilites of x and y pairs.'
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
	default=None,
	type=float,
	help="Minimal value on the Y axis."
	)

parser.add_argument(
	'--ymax',
	default=None,
	type=float,
	help="Maximal value on the Y axis."
	)

parser.add_argument(
	'--filename', 
	'-f',
	default=None,
	type=str,
	help="Name of the file containing the data (only useful when there's multiple .pkl files in dir.)"
	)

parser.add_argument(
	'--bins',
	'-b',
	default=10,
	type=int,
	help="Number of bins used when creating histogram data."
	)

parser.add_argument(
	'--binsx',
	default=None,
	type=int,
	help="Number of bins used on the x axis when creating histogram data."
	)

parser.add_argument(
	'--binsy',
	default=None,
	type=int,
	help="Number of bins used on the y axis when creating histogram data."
	)

parser.add_argument(
	'--interpolation',
	'-i',
	default='kaiser',
	type=str,
	help="Interpolation used when plotting the histogram."
)

parser.add_argument(
	'--cmap',
	'-c',
	default='CMRmap',
	type=str,
	help="Color map used when plotting the histogram."
)

args = parser.parse_args()
dirname = args.dirname
xmin = args.xmin
xmax = args.xmax
ymin = args.ymin
ymax = args.ymax
fname = args.filename
bins = args.bins
binsx = args.binsx
binsy = args.binsy
interpolation = args.interpolation
cmap = args.cmap

bins = bins_setup(bins, binsx, binsy)

try:
	filename = find_data_file(dirname, fname)
except Exception as e:
	print("Error: directory not found.")
	exit(1)

#load data from the pickle file
data = Pairs()
data.from_pkl(filename)

x = data.get_xvals_ndarray()
y = data.get_yvals_ndarray()

xmin, xmax, ymin, ymax = get_range(x, y, xmin, xmax, ymin, ymax)

heatmap, xedges, yedges = np.histogram2d(x, y, bins=bins, range=[[xmin, xmax], [ymin, ymax]])
heatmap = heatmap.T

heatmap = heatmap / np.linalg.norm(heatmap)

extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]

#plot the results
#set up the graph figure
fig = plt.figure(figsize=(20,20))
ax = fig.add_subplot()

fig_setup(ax, x, y, xmin, xmax, ymin, ymax)

im = ax.imshow(heatmap, extent=extent, origin='lower', interpolation=interpolation, cmap=cmap)
ax.set_aspect('auto')

plt.colorbar(im, ax=ax, label='Probability density')

plt.show()
