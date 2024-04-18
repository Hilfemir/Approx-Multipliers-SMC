#!/usr/bin/env python

"""Random number generation with different distributions.

Script used to approximate and plot the probability distributions
 of randomly generated pairs of numbers. The goal is to mimic the distributions
 of multiplication pairs in real algorithms.

author: Michal Blazek
organization: BUT FIT
date: 2024

Part of bachelor's thesis called Statistical model checking of approximate computing systems.
"""

import random
import matplotlib.pyplot as plt
from pyparsing import alphanums
import seaborn as sns

numbers = []

for i in range(10000):
	#Sieve of Pritchard - A
	#alpha = 1.0
	#beta = 0.8
	#num = random.gammavariate(alpha, beta)
	#num = int(num * 7)

	#Sieve of Pritchard - B
	#num = random.uniform(0, 256)
	#num = int(num)

	#if 100 < num < 175:
	#	num = int(random.uniform(0,75))

	#if 175 <= num <= 200:
	#	num = int(random.uniform(200,255))

	#AKS Primality test - A
	num = random.triangular(0, 180, 10)
	num = int(num)

	if num < 0:
		num = int(random.uniform(0,50))

	#if num > 255:
	#	num = int(random.uniform(0,150))

	#AKS Primality test - B
	#alpha = 2.0
	#beta = 2.0
	#num = random.betavariate(alpha, beta)
	#num = int(num * 255)

	#Ellipse Midpoint - A
	#alpha = 0.5
	#beta = 5.0
	#num = random.betavariate(alpha, beta)
	#num = int(num * 40)

	#Ellipse Midpoint - B
	#num = random.uniform(-10,255)
	#num = int(num)
	#if num < 0:
	#	num = int(random.uniform(2,15))

	#Circle Point by Point - both A and B
	#num = random.uniform(2, 255)

	#Integer Square Root - both A and B
	#num = random.triangular(-10, 255, 10)
	#num = int(num)

	#ElGamal Signature Scheme - A
	#num = random.triangular(0, 350, 0)
	#num = int(num)

	#if num > 255:
	#	num = int(random.uniform(0,50))

	#ElGamal Signature Scheme - B
	#alpha = 1.7
	#beta = 1.7
	#num = random.weibullvariate(alpha, beta)
	#num = int(num * 60)

	#if num > 255:
	#	num = int(random.uniform(0,25))

	#Bresenham - A
	#num = 2

	#Bresenham - B
	#num = int(random.gauss(140, 100))

	#if num > 255 or num < 0:
	#	num = int(random.uniform(0,255))

	numbers.append(num)


plt.figure(figsize=(10, 6))
sns.kdeplot(numbers, color='C0')
#sns.kdeplot(numbers, color='C1')

plt.xlabel('Hodnota vstupu X', fontsize=20)
plt.ylabel('Pravděpodobnost výskytu', fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=15)
plt.grid(False)

outname = "aks_x"
plt.savefig(f"../out/rand_generated_numbers/{outname}_randgen_num.png")
plt.show()