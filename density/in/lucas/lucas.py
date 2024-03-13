from random import randrange
import sys
sys.path.append("..")
from pairs import Pairs

pairs = Pairs()

# A Lucas Theorem based solution  
# to compute nCr % p 
  
# Returns nCr % p. In this Lucas  
# Theorem based program, this  
# function is only called for 
# n < p and r < p. 
def nCrModpDP(n, r, p): 
	  
	# The array C is going to store 
	# last row of pascal triangle 
	# at the end. And last entry  
	# of last row is nCr 
	C = [0] * (n + 1); 
  
	# Top row of Pascal Triangle 
	C[0] = 1;  
  
	# One by constructs remaining  
	# rows of Pascal Triangle from  
	# top to bottom 
	for i in range(1, (n + 1)): 
		  
		# Fill entries of current  
		# row using previous row 
		# values 
		j = min(i, r);  
		while(j > 0): 
			C[j] = (C[j] + C[j - 1]) % p; 
			j -= 1; 
	return C[r]; 
  
# Lucas Theorem based function that   
# returns nCr % p. This function 
# works like decimal to binary  
# conversion recursive function. 
# First we compute last digits of  
# n and r in base p, then recur 
# for remaining digits 
def nCrModpLucas(n, r, p): 
	  
	# Base case 
	if (r == 0): 
		return 1; 
		  
	# Compute last digits of n 
	# and r in base p 
	ni = int(n % p); 
	ri = int(r % p); 
		  
	# Compute result for last digits  
	# computed above, and for remaining  
	# digits. Multiply the two results  
	# and compute the result of  
	# multiplication in modulo p. 
	# Last digits of n and r
	tmp1 = nCrModpLucas(int(n / p), int(r / p), p)
	tmp2 = nCrModpDP(ni, ri, p)
	pairs.insert(tmp1, tmp2)
	return (tmp1 * tmp2) % p # Remaining digits 
  
# Driver Code
for i in range(1000):
	n = randrange(10, 1000)
	k = n - randrange(2, 50)
	if k <= 0 or k < n:
		k = n - 5
	p = 251
	
	try:
		res = nCrModpLucas(n, k, p)
	except:
		continue
	
pairs.pkl_dump()
print(pairs)
print(f"max: {pairs.get_max_val()}")