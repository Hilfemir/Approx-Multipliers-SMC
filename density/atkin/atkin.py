import sys
sys.path.append("..")
from pairs import Pairs

pairs = Pairs()

#Sieve of Atkin (Prime numbers generator)

def sieve_off_atkin(limit):
	# 2 and 3 are known
	# to be prime
	if limit > 2:
		print(2, end=" ")
	if limit > 3:
		print(3, end=" ")
 
	# Initialise the sieve
	# array with False values
	sieve = [False] * (limit + 1)
	for i in range(0, limit + 1):
		sieve[i] = False
 
	'''Mark sieve[n] is True if
	one of the following is True:
	a) n = (4*x*x)+(y*y) has odd
	number of solutions, i.e.,
	there exist odd number of
	distinct pairs (x, y) that
	satisfy the equation and
	n % 12 = 1 or n % 12 = 5.
	b) n = (3*x*x)+(y*y) has
	odd number of solutions
	and n % 12 = 7
	c) n = (3*x*x)-(y*y) has
	odd number of solutions,
	x > y and n % 12 = 11 '''
	x = 1
	while x * x <= limit:
		y = 1
		while y * y <= limit:
 
			# Main part of
			# Sieve of Atkin
			pairs.insert(4, x)
			pairs.insert(4*x, x)
			pairs.insert(y, y)
			n = (4 * x * x) + (y * y)
			if (n <= limit and (n % 12 == 1 or
								n % 12 == 5)):
				sieve[n] ^= True
 
			pairs.insert(3, x)
			pairs.insert(3*x, x)
			pairs.insert(y, y)
			n = (3 * x * x) + (y * y)
			if n <= limit and n % 12 == 7:
				sieve[n] ^= True
 
			pairs.insert(3, x)
			pairs.insert(3*x, x)
			pairs.insert(y, y)
			n = (3 * x * x) - (y * y)
			if (x > y and n <= limit and
					n % 12 == 11):
				sieve[n] ^= True
			y += 1
		x += 1
 
	# Mark all multiples of
	# squares as non-prime
	r = 5
	while r * r <= limit:
		if sieve[r]:
			for i in range(r * r, limit+1, r * r):
				pairs.insert(r, r)
				sieve[i] = False
 
		r += 1
 
		# Print primes
	# using sieve[]
	for a in range(5, limit+1):
		if sieve[a]:
			print(a, end=" ")
			 
# Driver Code
limit = 4000
sieve_off_atkin(limit)

print(pairs)
print(f"max: {pairs.get_max_val()}")
pairs.pkl_dump()