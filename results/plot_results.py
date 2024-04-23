#!/usr/bin/env python

"""Script used to plot the simulation results stored in a pickled dataframe.
author: Michal Blazek
organization: BUT FIT
date: 2024

Part of bachelor's thesis called Statistical model checking of approximate computing systems.
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

colors = {
	1 : "#7F58AF",
	2 : "#64C5EB",
	3 : "#E84D8A",
	4 : "#FEB326"
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
	if multiplier is not None:
		args_outname = f"{multiplier}.png"

	if not args_outname.endswith(".png"):
		args_outname += ".png"

	if not args_outname.startswith("./plots/"):
		if metric is not None:
			args_outname = f"./plots/metric_examples/{metric}/{args_outname}"
		else:
			args_outname = f"./plots/{args_outname}"

	return Path(args_outname)
		

def transform_scatter(df: pd.DataFrame, metric: str, distribution: str | None) -> pd.DataFrame:
	"""Transform the input dataframe to make it ready for a scatter plot and return it.
	"""
	if distribution is not None:
		df = df[df['distribution'] == distribution]

	df = df[(df["metric"] == metric) | (df["metric"] == "avg_flips_per_res")]
	df = pd.pivot(df, columns="metric", values="value", index="multiplier")
	
	return df


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

	print(df)

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
		choices=["scatter", "bar"],
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
	fig = plt.figure(figsize=(12,8))
	ax = fig.add_subplot(1,1,1)

	if args.type == "scatter":
		df = transform_scatter(df, args.metric, args.distribution)
		df.plot.scatter(x="avg_flips_per_res", y=args.metric, ax=ax)

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

		ax.set_ylabel(metrics_cs[args.metric], fontsize=22)
		ax.set_xlabel("Rozdělení", fontsize=22)
		ax.set_title(args.multiplier, fontsize=22)
		ax.tick_params(axis='both', which='major', labelsize=12)

		ax.grid(visible=True, axis='y', linestyle=":")


	if args.print:
		print(df.to_string())

	if not args.noout:
		plt.savefig(output_file, bbox_inches='tight')

	if not args.noshow:
		plt.show()


if __name__ == "__main__":
	main()