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
	#num = int(num * 150)

	#Sieve of Pritchard - B
	#num = random.uniform(0, 2000)
	#num = int(num)

	#AKS Primality test - A
	#num = random.triangular(-50, 450, 70)

	#AKS Primality test - B
	#alpha = 2.0
	#beta = 2.0
	#num = random.betavariate(alpha, beta)
	#num = int(num * 400)

	#Ellipse Midpoint - A
	#alpha = 0.5
	#beta = 5.0
	#num = random.betavariate(alpha, beta)
	#num = int(num * 40)

	#Ellipse Midpoint - B
	#mu = 9.0
	#sigma = 15.0
	#num = random.gauss(mu, sigma)

	#Circle Point by Point - both A and B
	#num = random.uniform(2, 100)

	#Integer Square Root - both A and B
	#num = random.triangular(-10, 35, 5)

	#ElGamal Signature Scheme - A
	#num = random.triangular(-20, 600, 20)

	#ElGamal Signature Scheme - B
	alpha = 1.7
	beta = 1.7
	num = random.weibullvariate(alpha, beta)
	num = int(num * 200)

	numbers.append(num)

plt.figure(figsize=(10, 6))
sns.kdeplot(numbers)  # You can adjust the bandwidth (bw_adjust) for smoothing
plt.title('ElGamal Signature Scheme - B')
plt.xlabel('Value')
plt.ylabel('Density')
plt.grid(False)
plt.savefig("./rand_generated/elgamal_b.png")
plt.show()
