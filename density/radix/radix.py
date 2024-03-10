from random import sample
import sys
sys.path.append("..")
from pairs import Pairs

pairs = Pairs()

def radix_sort(arr):
    # Find the maximum number to determine the number of digits
    max_num = max(arr)
    
    # Initialize the place value to the least significant digit
    exp = 1
    
    # Perform counting sort for every digit place using multiplication
    while max_num // exp > 0:
        counting_sort(arr, exp)
        pairs.insert(exp, 10)
        exp *= 10


def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Count occurrences of digits at the current place value using multiplication
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Update count to store the position of each digit in output
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copy the output array to arr
    for i in range(n):
        arr[i] = output[i]


# Example usage:
for i in range(1001):
    arr = sample(range(1, 256), 200)
    radix_sort(arr)
    #print("Sorted array:", arr)

pairs.pkl_dump()
print(pairs)
print(f"max: {pairs.get_max_val()}")