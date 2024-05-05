#!/usr/bin/env python

"""Script used to plot the simulation results stored in a pickled dataframe.
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

from random import choice
import pandas as pd
import argparse
from os import PathLike
from pathlib import Path
import matplotlib.pyplot as plt

metrics_cs = {
	"avg_flips_per_res" : "Průměr překl. bitů",
	"coverage_percentage" : "% pokrytí",
	"delay_avg" : "Průměrné zpoždění",
	"error_prob" : "Pravděpodobnost chyby",
	"max_bit_flips" : "Max. překl. bitů",
	"max_hamming_distance" : "Max. Hammingova vzdálenost",
	"mean_abs_error" : "Průměrná absolutní chyba",
	"mean_relative_error" : "Průměrná relativní chyba",
	"mean_squared_error" : "Průměrná kvadratická chyba",
	"worst_case_error" : "Nejhorší absolutní chyba",
	"worst_case_relative_error" : "Nejhorší relativní chyba",
	"worst_delay" : "Nejhorší zpoždění",
	"area" : "Plocha"
}

area = {
	"mul8u_12KA" : 683.3,
	"mul8u_17MJ" : 18.8,
	"mul8u_17MN" : 13.1,
	"mul8u_17R6" : 228.5,
	"mul8u_197B" : 395.6,
	"mul8u_1A0M" : 75.6,
	"mul8u_2NDH" : 347.8,
	"mul8u_BG1" : 561.8,
	"mul8u_GTR" : 550.5,
	"mul8u_NLX" : 511.5,
	"mul8u_R36" : 60.5,
	"mul8u_R92" : 604.5,
	"mul8u_Z9D" : 220.6,
	"mul8u_ZB3" : 682.8,
	"mul8u_ZDF" : 651.9
}

colors = {
	1 : "#7F58AF",
	2 : "#E84D8A",
	3 : "#FEB326",
	4 : "#64C5EB"
}

def determine_inpath(args_file: str) -> PathLike[str]:
	"""Take path to the input file, edit if necessary.
	Returns Path object of the input file.
	"""
	if not args_file.endswith(".pkl"):
		args_file += ".pkl"
	
	if not args_file.startswith("./pickles/"):
		args_file = f"./pickles/{args_file}"

	return Path(args_file)


def determine_outpath(args_outname: str, metric: str | None, multiplier: str | None) -> PathLike[str]:
	"""Take path to the output file, edit if necessary.
	Returns Path object of the output file.
	"""
	#if multiplier is not None:
	#	args_outname = f"{multiplier}.png"

	if not args_outname.endswith(".png"):
		args_outname += ".png"

	#if not args_outname.startswith("./plots/"):
	#	if metric is not None:
	#		args_outname = f"./plots/metric_examples/{metric}/{args_outname}"
	#	else:
	#		args_outname = f"./plots/{args_outname}"

	return Path(args_outname)
		

def transform_scatter(df: pd.DataFrame, metric: str, distribution: str | None, val_limit: float | None = None) -> pd.DataFrame:
	"""Transform the input dataframe to make it ready for a scatter plot and return it.
	"""
	new_df = df.copy()

	if distribution is not None:
		new_df = new_df[new_df['distribution'] == distribution].copy()

	new_df = new_df[(new_df["metric"] == metric) | (new_df["metric"] == "area")]
	new_df = pd.pivot(new_df, columns="metric", values="value", index="multiplier")

	#add the area column
	new_df['area'] = new_df.index.map(area)

	#drop unknown values
	new_df.dropna(inplace=True)

	if val_limit is not None:
		new_df = new_df[new_df[metric] <= val_limit]

	return new_df


def transform_barplot(df: pd.DataFrame, multiplier: str, metric: str, distribution: str | None) -> pd.DataFrame:
	"""Transform the input dataframe to make it ready for a bar plot and return it.
	"""
	if distribution is not None:
		df = df[df['distribution'] == distribution]

	df = df[(df["multiplier"] == multiplier) & (df["metric"] == metric)]
	df = df[['distribution', 'value']]

	df.rename(columns={'value' : metric}, inplace=True)
 
	#move uni_uni row to start
	df.reset_index(inplace=True, drop=True)
	idx = [7] + [i for i in range(len(df)) if i != 7]
	df = df.reindex(idx)

	return df


def main():
	parser = argparse.ArgumentParser(
	                    prog='plot_results.py',
	                    description='Plot data from a dataframe stored in a pickle file.'
	)
	
	parser.add_argument(
		'--file', '-f',
		help="Name or path of the input pickle file. Default is ./pickles/data.pkl",
		default='data.pkl',
		required=False
	)

	parser.add_argument(
		'--type', '-t',
		help="Type of plot.",
		choices=["scatter", "bar", "multiscatter"],
		default='scatter',
		required=False
	)

	parser.add_argument(
		'--distribution', '-d',
		help="Filter out only certain distribution.",
		choices=[None, 'uni_uni', 'same_triang', 'beta_uni', 'triang_beta', 'gamma_2norm', 'triang_weibull', 'same_uni', 'const_norm'],
		default=None,
		required=False
	)

	parser.add_argument(
		'--metric',
		help="Which metric should be on the Y-axis.",
		choices=[
			'mean_abs_error', 'error_prob', 'mean_relative_error', 'mean_squared_error',
			'worst_case_error', 'worst_case_relative_error', 'max_hamming_distance',
			'worst_delay', 'delay_avg', 'max_bit_flips', 'avg_bit_flips_per_res'
		   ],
		default='mean_abs_error',
		required=False
	)

	parser.add_argument(
		'--multiplier', '--mult',
		help="Selected multiplier (barplot only).",
		default='mul8u_4X5',
		required=False
	)

	parser.add_argument(
		'--print', '-p',
		help="Print the dataframe.",
		action="store_true",
		default=False
	)

	parser.add_argument(
		'--noout',
		help="Don't save the plot.",
		action="store_true",
		default=False
	)

	parser.add_argument(
		'--outname',
		help="Name of the output file.",
		default="output.png"
	)

	parser.add_argument(
		'--noshow',
		help="Don't show the plot.",
		action="store_true",
		default=False
	)

	parser.add_argument(
		'--color', '-c',
		help="Color of the plot",
		choices=[1,2,3,4],
		default=1,
		type=int
	)

	args = parser.parse_args()
	input_file = determine_inpath(args.file)
	output_file = determine_outpath(args.outname, args.metric, str(args.color))

	df = pd.read_pickle(input_file)
	fig = plt.figure(figsize=(12,10))
	ax = fig.add_subplot(1,1,1)

	if args.type == "multiscatter":
		plt.rc('legend',fontsize=25)

		ms_colors = [
			"#22dbfb",
			"#f48494",
			"#0c545c",
			"#028096",
			"#00ff5d",
			"#0c1349",
			"#2369c6",
			"#ffff40"
		]

		distributions = [
			'uni_uni',
			'same_triang',
			'beta_uni',
			'triang_beta',
			'gamma_2norm',
			'triang_weibull',
			'same_uni',
			'const_norm'
		]

		for i, d in enumerate(['uni_uni', 'triang_beta', 'triang_weibull']):
			d_df = transform_scatter(df, args.metric, d, val_limit=1.0)
			d_df.plot.scatter(
				x="area",
				y=args.metric,
				ax=ax,
				s=250,
				color=colors[i+1],
				alpha=0.8,
				label=d
				)
		
		ax.set_ylabel(metrics_cs[args.metric], fontsize=28)
		ax.set_xlabel("Plocha [μm²]", fontsize=28)
		ax.tick_params(axis='both', which='major', labelsize=22)
		ax.grid(visible=True, axis="both", linestyle=":")

		handles, labels = ax.get_legend_handles_labels()
		ax.legend(handles=handles[0:], labels=labels[0:])

		plt.legend(bbox_to_anchor=(0, 1.02, 1, 0.2), loc="lower left",
                mode="expand", borderaxespad=0, ncol=3)

	elif args.type == "scatter":
		df = transform_scatter(df, args.metric, args.distribution)
		df.plot.scatter(x="area", y=args.metric, ax=ax, s=10)

	elif args.type == "bar":
		df = transform_barplot(df, args.multiplier, args.metric, args.distribution)
		df.plot.bar(
			x='distribution', 
			y=args.metric, 
			rot=0, 
			ax=ax, 
			legend=False,
			color=[
				'gray', 
				colors[args.color],
				colors[args.color],
				colors[args.color],
				colors[args.color],
				colors[args.color],
				colors[args.color],
				colors[args.color]]
			)

		ax.set_ylabel(metrics_cs[args.metric], fontsize=28)
		ax.set_xlabel("Rozdělení", fontsize=28)
		ax.set_title(args.multiplier, fontsize=28)
		ax.tick_params(axis='both', which='major', labelsize=22)

		ax.grid(visible=True, axis='y', linestyle=":")

		fig.autofmt_xdate()


	if args.print:
		print(df.to_string())

	if not args.noout:
		plt.savefig(output_file)

	if not args.noshow:
		plt.show()


if __name__ == "__main__":
	main()