import matplotlib.pyplot as plt
import numpy as np
from numpy.typing import NDArray
import argparse
import seaborn as sns
import pandas as pd
from pathlib import Path

from pairs import Pairs
from stats import Stats as st
from utils import find_data_file, axis_setup, get_save_path


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

parser.add_argument(
	'--savepath',
	default=None,
	type=str,
	help='Where should the plot be saved.'
	)

parser.add_argument(
	'--nosave',
	action='store_true',
	help="Don't save the plot."
	)

parser.add_argument(
	'--noshow',
	action='store_true',
	help="Don't show the plot."
	)

parser.add_argument(
	'--title',
	'-t',
	default=None,
	type=str,
	help="Title of the plot."
	)

parser.add_argument(
	'--step',
	default=None,
	type=int,
	help="Step when loading the data. (In case there is too much data)"
	)

args = parser.parse_args()
dirname = args.dirname
xmin = args.xmin
xmax = args.xmax
ymin = args.ymin
ymax = args.ymax
savepath = args.savepath
nosave = args.nosave
noshow = args.noshow
title = args.title
step = args.step

try:
	filename = find_data_file(dirname)
except Exception as e:
	print("Error: directory not found.")
	exit(1)

#obtain path where the plot shall be saved
try:
	savepath = get_save_path(savepath, filename, 'singular')
except Exception as e:
	print(e)
	print("Error: invalid savefig path.")
	exit(2)

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot()

#load data from the pickle file
data = Pairs()
data.from_pkl(filename)

xmin, xmax = axis_setup(data, xmin, xmax)

df = data.singular_dataframe(step=step)
df.rename(columns={'x' : 'X', 'y' : 'Y'}, inplace=True)

df.plot(
	ax=ax,
	kind='density',
	xlim=(xmin, xmax),
	title=title
	)

ax.set_xlabel("Hodnota vstupu", fontsize=11)
ax.set_ylabel("Pravděpodobnost výskytu", fontsize=11)

if not nosave:
	plt.savefig(savepath)

if not noshow:
	plt.show()
