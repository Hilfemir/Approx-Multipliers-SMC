import random
import matplotlib.pyplot as plt
import argparse

from pairs import Pairs
from utils import find_data_file, get_save_path

binaries = []

bit_flips = {
	15 : 0,
	14 : 0,
	13 : 0,
	12 : 0,
	11 : 0,
	10 : 0,
	9 : 0,
	8 : 0,
	7 : 0,
	6 : 0,
	5 : 0,
	4 : 0,
	3 : 0,
	2 : 0,
	1 : 0,
	0 : 0
}

index_names = {
	15 : 'B[7]',
	14 : 'B[6]',
	13 : 'B[5]',
	12 : 'B[4]',
	11 : 'B[3]',
	10 : 'B[2]',
	9 : 'B[1]',
	8 : 'B[0]',
	7 : 'A[7]',
	6 : 'A[6]',
	5 : 'A[5]',
	4 : 'A[4]',
	3 : 'A[3]',
	2 : 'A[2]',
	1 : 'A[1]',
	0 : 'A[0]'
	}

def count_bit_flips(index: int):
	"""Counts the number of bit flips of input number bits
	at given index.
	"""
	prev = 0
	for number in binaries:
		current = number[index]
		if current != prev:
			bit_flips[index] += 1

		prev = current


def to_binary_str(a: int, b: int) -> str:
	p1 = str(bin(a))[2:].zfill(8)
	p2 = str(bin(b))[2:].zfill(8)
	ret = p1 + p2 #string concat
	parts = [x for x in ret] 
	parts.reverse() #reverse so that LSB is at index 0
	binaries.append(parts)
	return ret


def plot_res(title="Bit flip count", outname=None, savefig=False):
	indexes = bit_flips.keys()
	values = bit_flips.values()

	#replace indexes with input bit names
	indexes = [index_names[i] for i in indexes]
	indexes.reverse()

	#normalize output values
	values = [val / sum(values) for val in values]
	values.reverse()
	
	plt.figure(figsize=(15, 8))

	# creating the bar plot
	plt.bar(indexes, values, color ='cornflowerblue', 
	        width = 0.4)
	
	plt.xlabel("Bit indexes")
	plt.ylabel("Bit flip density")
	plt.title(title)
	plt.grid(visible=True, axis='y', linestyle=':')

	if savefig:
		plt.savefig(f"./bit_flips/{outname}")

	plt.show()


def main():
	# parse args #
	parser = argparse.ArgumentParser(
	                    prog='bit_flips.py',
	                    description='Plots a bar graph of probabilities of each bit flipping during multiplications in given algorithm.'
						)

	parser.add_argument(
		'dirname',
		help="Name of the directory which contains a .pkl file with the data."
		)
	
	parser.add_argument(
		'--nosave',
		action='store_true',
		help="Don't save the plot."
		)

	parser.add_argument(
		'--title',
		'-t',
		default="Bit flips",
		type=str,
		help="Title of the plot."
		)

	args = parser.parse_args()

	dirname = args.dirname
	title = args.title
	nosave = args.nosave

	try:
		filename = find_data_file(dirname)
	except Exception as e:
		print("Error: directory not found.")
		exit(1)

	#obtain path where the plot shall be saved
	try:
		savepath = get_save_path(None, filename, 'bit_flips')
	except Exception as e:
		print(e)
		print("Error: invalid savefig path.")
		exit(2)
	
	#load data from the pickle file
	data = Pairs()
	data.from_pkl(filename)

	#convert numbers to their binary representations
	for pair in data.get_pairs():
		to_binary_str(pair[0], pair[1])

	#calculate bit flips for each bit
	for i in range(16):
		count_bit_flips(i)

	plot_res(
		title=title,
		outname=savepath,
		savefig=not(nosave))

if __name__=="__main__": 
	main()