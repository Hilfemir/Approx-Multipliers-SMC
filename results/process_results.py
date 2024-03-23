import csv
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


def process_file(file_path) -> list[tuple]:
	"""Open csv file and collect all necessary data.
	Returns list of Result objects represented as tuples.
	"""
	#collect info about the multiplier and distribution
	parts = file_path.parts
	dist = parts[0]
	mult_id = parts[1]

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
		'hamming_distance' : None,
		'worst_delay' : None,
		'bit_flips' : None
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
	

def main():
	parser = argparse.ArgumentParser(
	                    prog='process_results.py',
	                    description='Processes results from csv files, stores them in data.pkl'
						)
	
	parser.add_argument(
		'--dir', '-d', 
		help='Directory containing csv files or subdirectories which contain csv files.',
		default='',
		required=False
		)
	
	args = parser.parse_args()

	results = []
	rootdir = Path(f'./{args.dir}')

	#find all csv files in dir and all its subdirectories
	file_list = [f for f in rootdir.glob('**/*') if f.is_file() and f.name.endswith(".csv")]
	for file_path in file_list:
		part_results = process_file(file_path)
		results.extend(part_results)

	df = pd.DataFrame(results, columns=["distribution", "multiplier", "metric", "value"])
	print(df.to_string())
	

if __name__ == "__main__":
	main()