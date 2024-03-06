import random
import matplotlib.pyplot as plt

from pairs import Pairs
from utils import find_data_file

binaries = []

bit_flips = {
	7 : 0,
	6 : 0,
	5 : 0,
	4 : 0,
	3 : 0,
	2 : 0,
	1 : 0,
	0 : 0
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


def to_binary_str(a: int) -> str:
	ret = str(bin(a))[2:].zfill(8)
	parts = [x for x in ret] 
	parts.reverse() #reverse so that LSB is at index 0
	binaries.append(parts)
	return ret


def plot_res(title="Bit flip count", filename="out.png", savefig=False):
	global bit_flips

	if not filename.lower().endswith(".png"):
		filename += ".png"

	#normalize the bit flip counts
	total_flips = sum(bit_flips.values())
	bit_flips = {key : val / total_flips for key, val in bit_flips.items()}

	indexes = bit_flips.keys()
	values = bit_flips.values()
	
	# creating the bar plot
	plt.bar(indexes, values, color ='cornflowerblue',
	        width = 0.4)

	plt.xlabel("Bit indexes")
	plt.ylabel("Bit flips")
	plt.title(title)
	plt.grid(visible=True, axis='y', linestyle=':')

	if savefig:
		plt.savefig(f"./bit_flips/{filename}")

	plt.show()


def main():
	dirname = "isqrt"

	try:
		filename = find_data_file(dirname)
	except Exception as e:
		print("Error: directory not found.")
		exit(1)
	
	#load data from the pickle file
	data = Pairs()
	data.from_pkl(filename)

	#convert numbers to their binary representations
	for pair in data.get_pairs():
		to_binary_str(pair[0])

	#calculate bit flips for each bit
	for i in range(8):
		count_bit_flips(i)

	plot_res(
		title="Bit Flip Count - Integer Square Root",
		filename="isqrt",
		savefig=True)

if __name__=="__main__": 
	main()