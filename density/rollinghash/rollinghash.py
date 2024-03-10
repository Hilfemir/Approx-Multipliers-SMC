import random, string
from random import randrange
from primelibpy import Prime as pr
import sys
sys.path.append("..")
from pairs import Pairs

pairs = Pairs()

#The rolling hash algorithhm
#The code below was generated using ChatGPT

def rolling_hash_search(text, pattern):
	# Define prime number for the hash function to reduce collisions
	prime = pr.getRandomPrime("GoodPrime", 2)

	# Calculate the hash value for the pattern and the initial window in the text
	pattern_hash = 0
	text_hash = 0
	for i in range(len(pattern)):
		pairs.insert(pattern_hash, prime)
		pattern_hash = (pattern_hash * prime + ord(pattern[i])) % prime
		
		pairs.insert(text_hash, prime)
		text_hash = (text_hash * prime + ord(text[i])) % prime

	# Iterate through the text to find the pattern
	for i in range(len(text) - len(pattern) + 1):
		if pattern_hash == text_hash and text[i:i+len(pattern)] == pattern:
			return i  # Pattern found at index i

		# Update the rolling hash for the next window
		if i < len(text) - len(pattern):
			pairs.insert(ord(text[i]), (prime**(len(pattern) - 1)))
			text_hash = (text_hash - ord(text[i]) * (prime**(len(pattern) - 1))) % prime

			pairs.insert(text_hash, prime)
			text_hash = (text_hash * prime + ord(text[i + len(pattern)])) % prime
			text_hash = (text_hash + prime) % prime  # Ensure the hash is non-negative

	return -1  # Pattern not found in the text

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

# Example usage:
for i in range(1000):
	text = randomword(50)
	pattern = text[random.randrange(0, 10) : random.randrange(11, 20)]
	result = rolling_hash_search(text, pattern)

	if result != -1:
		print(f"Pattern found at index {result}")
	else:
		print("Pattern not found in the text")

pairs.pkl_dump()
print(pairs)
print(f"max: {pairs.get_max_val()}")
