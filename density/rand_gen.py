import random
import matplotlib.pyplot as plt
import seaborn as sns

numbers = []
alpha = 0.2
beta = 3.0

for i in range(10000):
    num = random.gammavariate(alpha, beta)
    num = int(num * 100)
    numbers.append(num)

plt.figure(figsize=(10, 6))
sns.kdeplot(numbers, bw_adjust=1.0)  # You can adjust the bandwidth (bw_adjust) for smoothing
plt.title('Density Plot of Given Integers')
plt.xlabel('Value')
plt.ylabel('Density')
plt.grid(False)
plt.show()