from ast import mod
from random import randrange
import sys
sys.path.append("..")
from pairs import Pairs

pairs = Pairs()

#Modular exponentiation

"""
function modular_pow(base, exponent, modulus) is
    if modulus = 1 then
        return 0
    c := 1
    for e_prime = 0 to exponent-1 do
        c := (c * base) mod modulus
    return c
"""

def modpow(base: int, exponent: int, modulus: int) -> int:
	if modulus == 1:
		return 0
	
	c = 1

	for e_prime in range(exponent):
		pairs.insert(c, base)
		c = (c * base) % modulus

	return c

for i in range(1000):
	base = randrange(10000000, 100000000)
	exponent = randrange(15, 35)
	modulus = 497
	r = modpow(base, exponent, modulus)

	print(r)

pairs.pkl_dump()