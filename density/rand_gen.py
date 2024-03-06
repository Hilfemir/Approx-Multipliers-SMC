import random
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

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
	#num = random.uniform(2, 255)

	#Integer Square Root - both A and B
	#num = random.triangular(-10, 150, 10)
	#num = int(num)

	#ElGamal Signature Scheme - A
	#num = random.triangular(-20, 600, 20)
	#num = int(num)

	#ElGamal Signature Scheme - B
	#alpha = 1.7
	#beta = 1.7
	#num = random.weibullvariate(alpha, beta)
	#num = int(num * 200)

	num = random.gammavariate(1.0,2.0)
	num = int(num)

	if num < 0:
		num = 0

	if num > 7:
		num = 0

	numbers.append(num)

# Convert the list to a pandas Series
series = pd.Series(numbers)

# Count the occurrences of each value
value_counts = series.value_counts(normalize=True).sort_index()

plt.figure(figsize=(10, 6))
value_counts.plot(kind='bar', color ='cornflowerblue')
plt.xlabel('Value')
plt.ylabel('Density')
plt.grid(visible=True, axis='y', linestyle=':')
plt.title('Frequency of Each Value in the List')
plt.xticks(rotation=0)
plt.show()
