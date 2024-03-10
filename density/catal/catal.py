import sys
sys.path.append("..")
from pairs import Pairs

pairs = Pairs()

# A dynamic programming based function to find nth
# Catalan number
 
def catalan(n):
    if (n == 0 or n == 1):
        return 1
 
    # Table to store results of subproblems
    catalan = [0 for i in range(n + 1)]
 
    # Initialize first two values in table
    catalan[0] = 1
    catalan[1] = 1
 
    # Fill entries in catalan[] using recursive formula
    for i in range(2, n + 1):
        catalan[i] = 0
        for j in range(i):
            c1 = catalan[j]
            c2 = catalan[i-j-1]
            pairs.insert(c1, c2)
            catalan[i] += c1 * c2
 
    # Return last entry
    return catalan[n]
 
# Driver code
for i in range(8):
    print(catalan(i))
 
pairs.pkl_dump('catal.pkl')
print(pairs)
print(f"max: {pairs.get_max_val()}")