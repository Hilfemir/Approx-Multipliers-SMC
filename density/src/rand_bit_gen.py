from multiprocessing import process
import random
import matplotlib.pyplot as plt
from numpy import add
import seaborn as sns
import pandas as pd

numbers = [] #list of tuples (pairs of numbers)
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


def add_bit_flips(a: int | None, b: int | None):
	if a is not None:
		bit_flips[a] += 1

	if b is not None:
		bit_flips[b] += 1


def process_num(input: int | float, add_val=0, under_to: str | int = "min", over_to: str | int = "max") -> int:
	input = int(input)
	min = 0
	max = 7

	if input < min:
		if under_to == "max":
			input = max
		elif under_to == "min":
			input = min
		elif isinstance(under_to, int):
			input = under_to
		else:
			raise ValueError("Error: gen_num() 'under_to' argument must be either 'max', 'min' or an int.")

	if input > max:
		if over_to == "max":
			input = max
		elif over_to == "min":
			input = min
		elif isinstance(over_to, int):
			input = over_to
		else:
			raise ValueError("Error: gen_num() 'over_to' argument must be either 'max', 'min' or an int.")
		
	return input + add_val


def plot_ax(ax, indexes: list, values: list, color='cornflowerblue'):
	#replace indexes with input bit names
	indexes = [index_names[i] for i in indexes]

	#normalize output values
	if sum(values) > 0:
		values = [(val / sum(values)) * 100 for val in values]

	# creating the bar plot
	ax.bar(indexes, values, color=color,
	        width = 0.4)

	input_name = indexes[0][0] #either A or B
	ax.set(
		xlabel = f"Bity vstupu {input_name}",
		ylabel = "Četnost přepnutí bitu (%)" if input_name == "A" else ""
		)

	ax.grid(visible=True, axis='y', linestyle=':')


def plot_res(outname=None, savefig=False):
	indexes = list(bit_flips.keys())
	values = list(bit_flips.values())

	indexes.reverse() #first A then B
	values.reverse()

	fig = plt.figure(figsize=(20, 10))
	gs = fig.add_gridspec(1, 2, hspace=0, wspace=0)
	(ax1, ax2) = gs.subplots(sharex='col', sharey='row')

	plot_ax(ax1, indexes[0:8], values[0:8])
	plot_ax(ax2, indexes[8:16], values[8:16], color="orangered")

	if savefig and outname is not None:
		plt.savefig(f"./rand_generated_bits/{outname}")

	plt.show()

def main():
	for i in range(10000):
		#isqrt
		"""
		num_a = random.gammavariate(1.0,2.0)
		num_a = process_num(num_a, over_to="min")

		num_b = random.gammavariate(1.0,2.0)
		num_b = process_num(num_b, add_val=8, over_to="min")
		"""

		#####################################################

		#lucas theorem
		"""
		num_a = random.uniform(0, 8)
		num_a = process_num(num_a)

		num_b = None
		"""

		#####################################################

		#ellipse midpoint
		"""
		num_a = int(random.gauss(3,3))
		num_a = process_num(num_a, under_to=1, over_to=2)

		num_b = int(random.triangular(0, 7, 0))

		if num_b == 6:
			num_b = 4

		elif num_b == 5:
			num_b = 1

		elif num_b == 4:
			num_b = 0

		num_b = process_num(num_b, add_val=8)
		"""

		#####################################################

		#radix sort
		"""
		num_a = int(random.uniform(0,5))
		num_a = process_num(num_a)

		if num_a == 0:
			num_a = 5
		
		elif num_a == 4:
			num_a = 6

		num_b = int(random.uniform(0,3))

		if num_b == 2:
			num_b = 3

		num_b = process_num(num_b, add_val=8)
		"""

		#####################################################

		#greedyknapsack
		"""
		num_a = int(random.uniform(0,8))
		num_a = process_num(num_a)

		num_b = int(random.triangular(0, 5, 0))
		num_b = process_num(num_b, add_val=8)
		"""
		
		#####################################################

		#fuss-catalan number
		num_a = int(random.gauss(2, 2))
		num_a = process_num(num_a)

		num_b = int(random.gammavariate(1,1.5))
		num_b = process_num(num_b, add_val=8)

		numbers.append((num_a, num_b))
		add_bit_flips(num_a, num_b)
		

	print(bit_flips)

	plot_res(outname="fusscatal_randgen.png", savefig=True)


if __name__=="__main__": 
	main()