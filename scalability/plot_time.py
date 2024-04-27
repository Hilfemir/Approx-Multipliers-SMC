#!/usr/bin/env python

"""Script used to plot the measured scalability results.
author: Michal Blazek
organization: BUT FIT
date: 2024

Part of bachelor's thesis called Statistical model checking of approximate computing systems.
"""

import pandas as pd
import matplotlib.pyplot as plt

def main():
	df = pd.read_csv("./scalability.csv")
	plt.rc('legend',fontsize=16)

	fig = plt.figure(figsize=(9,7))
	ax = fig.add_subplot(1,1,1)

	new_df = df[df['Vstupní bity'] == '7x7']
	new_df.plot(ax=ax, x="Počet hradel", y="Čas [s]", label="7x7", color="#7F58AF")

	#filter out mults with same sized inputs
	new_df = df[df['Vstupní bity'] == '8x8']
	new_df.plot(ax=ax, x="Počet hradel", y="Čas [s]", label="8x8", color="#E84D8A")

	ax.set_ylabel("Čas [s]", fontsize=20)
	ax.set_xlabel("Počet hradel", fontsize=20)
	ax.tick_params(axis='both', which='major', labelsize=16)

	plt.show()

if __name__ == "__main__":
	main()