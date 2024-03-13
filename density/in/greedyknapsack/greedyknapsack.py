import random
import sys
sys.path.append("..")
from pairs import Pairs

pairs = Pairs()

def random_numbers(count: int, start: int, stop: int, step: int) -> list:
	ret = []
	for i in range(count):
		n = random.randrange(start, stop, step)
		ret.append(n)

	return ret

def fractional_knapsack(value, weight, capacity):
	# Calculate value-to-weight ratio for each item
	value_per_weight = [(v / w, v, w) for v, w in zip(value, weight)]

	# Sort items based on value-to-weight ratio in descending order
	value_per_weight.sort(reverse=True)

	total_value = 0
	knapsack = [0] * len(value)

	for vpw, v, w in value_per_weight:
		if capacity == 0:
			break

		amount = min(w, capacity)

		pairs.insert(amount, int(vpw))
		total_value += amount * int(vpw)

		capacity -= amount
		knapsack[value.index(v)] = amount

	return total_value, knapsack

# Example usage:
for i in range(1000):
	#values = random.sample(range(10, 310, 10), 10)
	values = random_numbers(10, 10, 600, 10)
	#weights = random.sample(range(10, 60, 10), 10)
	weights = random_numbers(10, 10, 250, 10)
	knapsack_capacity = random.randrange(50, 1000, 10)

	total_value, selected_items = fractional_knapsack(values, weights, knapsack_capacity)

	print(f"Total Value: {total_value}")
	print(f"Selected Items: {selected_items}")

pairs.pkl_dump()
print(pairs)
print(f"max: {pairs.get_max_val()}")
