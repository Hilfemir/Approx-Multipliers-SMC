import random
import matplotlib.pyplot as plt
import seaborn as sns

numbers = []
binaries = []

bit_flips = {
	7 : 0,
	6 : 0,
	5 : 0,
	4 : 0,
	3 : 0,
	2 : 0,
	1 : 0,
	0 : 0
}

def count_bit_flips(index: int) -> int:
	"""Counts the number of bit flips of input number bits
	at given index.
	"""
	prev = 0
	for number in binaries:
		current = number[index]
		if current != prev:
			bit_flips[index] += 1

		prev = current


def to_binary_str(a: int) -> str:
	ret = str(bin(a))[2:].zfill(8)
	parts = [x for x in ret] 
	parts.reverse() #reverse so that LSB is at index 0
	binaries.append(parts)
	return ret


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
	num = random.uniform(2, 255)

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

	num = int(num)

	if num < 0:
		num = 0

	#print(num)
	to_binary_str(num)

	numbers.append(num)

for i in range(8):
	count_bit_flips(i)

print(bit_flips)

#plt.figure(figsize=(10, 6))
#sns.kdeplot(numbers)  # You can adjust the bandwidth (bw_adjust) for smoothing
#plt.title('ElGamal Signature Scheme - B')
#plt.xlabel('Value')
#plt.ylabel('Density')
#plt.grid(False)
#plt.savefig("./rand_generated/elgamal_b.png")
#plt.show()

indexes = bit_flips.keys()
values = bit_flips.values()
 
# creating the bar plot
plt.bar(indexes, values, color ='cornflowerblue', 
        width = 0.4)
 
plt.xlabel("Bit indexes")
plt.ylabel("Bit flips")
plt.title("Bit flip count")
plt.grid(visible=True, axis='y', linestyle=':')
plt.savefig("./bit_flips/elgamal_a.png")
plt.show()