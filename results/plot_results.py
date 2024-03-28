import pandas as pd
import argparse
from os import PathLike
from pathlib import Path
import matplotlib.pyplot as plt


def determine_inpath(args_file: str) -> PathLike[str]:
	"""Take path to the input file, edit if necessary.
	Returns Path object of the input file.
	"""
	if not args_file.endswith(".pkl"):
		args_file += ".pkl"
	
	if not args_file.startswith("./pickles/"):
		args_file = f"./pickles/{args_file}"

	return Path(args_file)
		

def transform_scatter(df: pd.DataFrame, metric: str = "mean_abs_error") -> pd.DataFrame:
	"""Transform the input dataframe to make it ready for a scatter plot and return it.
	"""
	df = df[(df["metric"] == metric) | (df["metric"] == "avg_flips_per_res")]
	df = pd.pivot(df, columns="metric", values="value", index="multiplier")
	return df


def transform_barplot(df: pd.DataFrame, multiplier: str, metric: str) -> pd.DataFrame:
	"""Transform the input dataframe to make it ready for a bar plot and return it.
	"""
	df = df[(df["multiplier"] == multiplier) & (df["metric"] == metric)]
	df = df[['distribution', 'value']]
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

	args = parser.parse_args()
	input_file = determine_inpath(args.file)

	df = pd.read_pickle(input_file)

	if args.type == "scatter":
		df = transform_scatter(df, args.metric)
		df.plot.scatter(x="avg_flips_per_res", y=args.metric)

	elif args.type == "bar":
		df = transform_barplot(df, args.multiplier, args.metric)
		df.plot.bar(x='distribution', y='value', rot=0)

	print(df.to_string())
	plt.show()

if __name__ == "__main__":
	main()