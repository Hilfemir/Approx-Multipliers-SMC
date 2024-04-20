#!/usr/bin/env python

"""Script used to print simulation results stored in pickled dataframes.
author: Michal Blazek
organization: BUT FIT
date: 2024

Part of bachelor's thesis called Statistical model checking of approximate computing systems.
"""

from os import PathLike
from pathlib import Path
import pandas as pd
import argparse

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

	args = parser.parse_args()
	input_file = determine_inpath(args.file)

	df = pd.read_pickle(input_file)

	print(df.to_string(float_format="{:.2f}".format))

if __name__ == "__main__":
	main()