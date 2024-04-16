#!/usr/bin/env python

"""Script used to process simulation results in csv files into a pickled dataframe.
author: Michal Blazek
organization: BUT FIT
date: 2024

Part of bachelor's thesis called Statistical model checking of approximate computing systems.
"""

import csv
from os import PathLike
from pathlib import Path
import pandas as pd
import re
import argparse

class Result(object):
	def __init__(self, dist: str, mult_id: str, metric: str, value: float):
		self.dist = dist
		self.mult_id = mult_id
		self.metric = metric
		self.value = value

	def __repr__(self):
		return f"Result({self.dist}, {self.mult_id}, {self.metric}, {self.value})"
	
	def as_tuple(self) -> tuple:
		return (self.dist, self.mult_id, self.metric, self.value)


def process_file(file_path: PathLike[str]) -> list[tuple]:
	"""Open csv file and collect all necessary data.
	Returns list of Result objects represented as tuples.
	"""
	#collect info about the multiplier and distribution
	parts = file_path.parts
	try:
		dist = parts[-3]
		mult_id = parts[-2]
	except IndexError:
		dist = "unknown"
		mult_id = "unknown"

	if not mult_id.startswith('mul'):
		dist = "unknown"
		mult_id = "unknown"

	#collect lines from the csv file
	data = []
	with open(file_path, newline='') as f:
		reader = csv.reader(f)
		for row in reader:
			data.append(row)

	data = data[1:]

	results = {
		'coverage_percentage' : None,
		'delay_avg' : None,
		'error_prob' : None,
		'mean_abs_error' : None,
		'mean_relative_error' : None,
		'mean_squared_error' : None,
		'worst_case_error' : None,
		'worst_case_relative_error' : None,
		'max_hamming_distance' : None,
		'worst_delay' : None,
		'max_bit_flips' : None,
		'avg_flips_per_res' : None
	}

	#iterate through the csv lines and collect data for each error metric
	title_pattern = r'#\s*(.+?)\s*#' #eg. '# mean_squared_error #1'
	current_title = ""
	for i, d in enumerate(data):
		if title_match := re.search(title_pattern, d[0]):
			if i > 0:
				#found title of next metric, the prev item is the final val of the curr metric
				results[current_title] = round(float(data[i-1][1]), 2)

			current_title = title_match.group(1)

		#last item
		if i == len(data)-1:
			results[current_title] = round(float(d[1]), 2)

	#convert the results to Result objects (and their tuple representations)
	ret = [Result(dist, mult_id, key, val).as_tuple() for key, val in results.items() if val is not None]
	return ret
	

def determine_outpath(out: str) -> PathLike[str]:
	"""Take the 'out' argument of the script and process it into Path object.
	Returns a PathLike object representing path of the output file.
	"""
	if not out.endswith(".pkl"):
		out += ".pkl"

	if not out.startswith("./pickles/"):
		out = f"./pickles/{out}"

	return Path(out)


def determine_inpath(args_dir: str, args_file: str) -> tuple[str, PathLike[str]]:
	"""Returns either 'dir' or 'file' indicating whether the Path is to a directory or only a single file.
	  Also returns a Path object of the input file/dir.
	"""
	if args_file is None:
		return "dir", Path(f'./{args_dir}')
	
	else:
		return "file", Path(args_file)


def main():
	parser = argparse.ArgumentParser(
	                    prog='process_results.py',
	                    description='Processes results from csv files, stores them in a pickle file (default ./data.pkl)'
						)
	
	parser.add_argument(
		'--dir', '-d', 
		help='Directory containing csv files or subdirectories which contain csv files.',
		default='sim_results',
		required=False
	)
	
	parser.add_argument(
		'--file', '-f',
		help="Path to csv file, use this if you only wish to process one specific file. Precedes the --dir option.",
		default=None,
		required=False
	)
	
	parser.add_argument(
		'--out', '-o',
		help="Name of the output pkl file.",
		default='data.pkl',
		required=False
	)
	
	parser.add_argument(
		'--overwrite', '-w',
		help="Overwrite current output file, if exists.",
		action='store_true',
		default=False,
		required=False
	)

	parser.add_argument(
		'--print', '-p',
		help="Print the final dataframe.",
		action='store_true',
		default=False,
		required=False
	)

	parser.add_argument(
		'--noout',
		help="Don't export the dataframe into a pickle file.",
		action='store_true',
		default=False,
		required=False
	)
	
	args = parser.parse_args()

	results = []
	outpath = determine_outpath(args.out)
	intype, inpath = determine_inpath(args.dir, args.file)

	if intype == "dir":
		#find all csv files in dir and all its subdirectories
		file_list = [f for f in inpath.glob('**/*') if f.is_file() and f.name.endswith(".csv")]
		for file_path in file_list:
			part_results = process_file(file_path)
			results.extend(part_results)

	elif intype == "file":
		results.extend(process_file(inpath))

	#export results
	df = pd.DataFrame(results, columns=["distribution", "multiplier", "metric", "value"])

	if not args.noout:
		df.to_pickle(outpath)

	if args.print:
		print(df.to_string())
	

if __name__ == "__main__":
	main()