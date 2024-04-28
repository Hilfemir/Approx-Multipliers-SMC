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
	df = pd.read_csv("./memory.csv")
	plt.rc('legend',fontsize=16)

	fig = plt.figure(figsize=(9,7))
	ax = fig.add_subplot(1,1,1)

	print(df)
	df.plot(ax=ax, x="Vstupní bity", y="Paměť [GB]", color="#7F58AF")

	ax.set_ylabel("Paměť [GB]", fontsize=20)
	ax.set_xlabel("Vstupní bity", fontsize=20)
	ax.tick_params(axis='both', which='major', labelsize=16)
	ax.get_legend().remove()

	plt.show()

if __name__ == "__main__":
	main()