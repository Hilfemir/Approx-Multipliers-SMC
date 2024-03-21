import csv
from pathlib import Path
import pandas as pd

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


def process_file(file_path) -> Result:
	"""Open csv file, read the last row and collect all necessary info
	for the Result object, then return it.
	"""
	data = []
	with open(file_path, newline='') as f:
		reader = csv.reader(f)
		for row in reader:
			data.append(row)

	#collect info about the multiplier, distribution and error metric
	parts = file_path.parts
	dist = parts[0]
	mult_id = parts[1]
	metric = parts[2][:-4]

	#last row is the one we are looking for
	value = round(float(data[-1][1]), 2)

	ret = Result(dist, mult_id, metric, value)
	return ret
	

def main():
	results = []
	rootdir = Path('./uniform_uniform')
	subdir_list = [d for d in rootdir.glob('**/*') if d.is_dir()]

	#iterate through results from all multipliers
	for dir in subdir_list:
		#collect the csv files
		file_list = [f for f in rootdir.glob('**/*') if f.is_file() and f.name.endswith(".csv")]
		for file_path in file_list:
			result = process_file(file_path)
			results.append(result.as_tuple())

	df = pd.DataFrame(results, columns=["distribution", "multiplier", "metric", "value"])
	print(df)
	

if __name__ == "__main__":
	main()