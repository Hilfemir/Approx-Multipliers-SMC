#!/usr/bin/env python

"""Script used to print simulation results stored in pickled dataframes.
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

from os import PathLike
from pathlib import Path
import pandas as pd
import argparse

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


def determine_inpath(args_file: str) -> PathLike[str]:
	"""Take path to the input file, edit if necessary.
	Returns Path object of the input file.
	"""
	if not args_file.endswith(".pkl"):
		args_file += ".pkl"
	
	if not args_file.startswith("./pickles/"):
		args_file = f"./pickles/{args_file}"

	return Path(args_file)


def main():
	parser = argparse.ArgumentParser(
	                    prog='print_results.py',
	                    description='Print simulation results'
						)
	
	parser.add_argument(
		'--file', '-f',
		help="Name or path of the input pickle file. Default is ./pickles/data.pkl",
		default='data.pkl',
		required=False
	)

	parser.add_argument(
		'--distribution', '-d',
		help="Distribution filter",
		default=None,
		required=False
	)

	parser.add_argument(
		'--multiplier', '-m',
		help='Multiplier filter',
		default=None,
		required=False
	)

	parser.add_argument(
		'--outname',
		help="Name of the output file",
		default='out.csv',
		required=False
		)
	
	parser.add_argument(
		'--noout',
		help="Don't save the output csv file.",
		action='store_true',
		default=False,
		required=False
		)

	args = parser.parse_args()
	input_file = determine_inpath(args.file)

	df = pd.read_pickle(input_file)

	if args.distribution is not None:
		df = df[df['distribution'] == args.distribution]

	if args.multiplier is not None:
		df = df[df['multiplier'] == args.multiplier]

	#pivot for one concrete distribution (shows all different mults)
	df = pd.pivot(df, columns="metric", index="multiplier", values="value")
 
	#pivot for one concrete multiplier (shows all different distributions)
	#df = pd.pivot(df, columns="metric", index="distribution", values="value")

	#add the area column
	df['area'] = df.index.map(area)

	#drop unknown values
	df.dropna(inplace=True)

	#drop irrelevant columns
	df.drop(columns=["coverage_percentage"])

	#move 'area' column to the front
	column_to_move = df.pop("area")
	df.insert(0, "area", column_to_move)

	#sort by area
	df.sort_values(by=['area'], inplace=True)

	#out_table = df[['area', 'error_prob', 'mean_abs_error', 'worst_case_error']].copy()
 
	#change column order
	out_table = df[
		[
			'area',
			'coverage_percentage',
			'error_prob', 
			'mean_abs_error',
			'mean_relative_error',
			'mean_squared_error',
			'worst_case_error',
			'worst_case_relative_error',
			'max_hamming_distance',
			'delay_avg',
			'worst_delay',
			'avg_flips_per_res',
			'max_bit_flips'
			]
		].copy()

	#rename to czech labels
	out_table.rename(columns=metrics_cs, inplace=True)

	print(out_table.to_string(float_format="{:.2f}".format))

	#export csv
	out_table.to_csv(f'./out_csv/{args.outname}', index=True)

if __name__ == "__main__":
	main()