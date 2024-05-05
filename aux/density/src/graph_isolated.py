#!/usr/bin/env python

"""Script used to plot the distribution of multiplication pairs in selected algorithm.
This variant plots input X and input Y separately.

author: Michal Blazek
organization: BUT FIT
date: 2024

Part of bachelor's thesis called Statistical model checking of approximate computing systems.

Copyright (c) 2024 Michal Blazek

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
"""

import matplotlib.pyplot as plt
import numpy as np
from numpy.typing import NDArray
import argparse
import seaborn as sns
import pandas as pd
from pathlib import Path

from pairs import Pairs
from utils import find_data_file, axis_setup, get_save_path

plt.rc('legend',fontsize=20)

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

fig = plt.figure(figsize=(9,6))
ax = fig.add_subplot()

#load data from the pickle file
data = Pairs()
data.from_pkl(filename)

xmin, xmax = axis_setup(data, xmin, xmax)

df = data.singular_dataframe(step=step)

df.drop(columns=['y'], inplace=True)
df.rename(columns={'x' : 'X a Y'}, inplace=True)

print(df)

df.plot(
	ax=ax,
	kind='density',
	xlim=(xmin, xmax),
	title=title,
	color='C0'
	)

ax.set_xlabel("Hodnota vstupu", fontsize=20)
ax.set_ylabel("Pravděpodobnost výskytu", fontsize=20)

ax.tick_params(axis='both', which='major', labelsize=15)

if not nosave:
	plt.savefig(savepath)

if not noshow:
	plt.show()
