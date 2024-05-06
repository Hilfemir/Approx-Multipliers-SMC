#!/usr/bin/env python

"""Script used to plot the measured scalability results.
author: Michal Blazek
organization: BUT FIT
date: 2024

Part of bachelor's thesis called Statistical model checking of approximate computing systems.

Copyright (c) 2024 Michal Blazek

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
	df = pd.read_csv("./scalability.csv")
	plt.rc('legend',fontsize=16)

	fig = plt.figure(figsize=(9,7))
	ax = fig.add_subplot(1,1,1)

	new_df = df[df['Vstupní bity'] == '7x7']
	new_df.plot(ax=ax, x="Počet hradel", y="Čas [s]", label="mult_7x7", color="#7F58AF")

	#filter out mults with same sized inputs
	new_df = df[df['Vstupní bity'] == '8x8']
	new_df.plot(ax=ax, x="Počet hradel", y="Čas [s]", label="mult_8x8", color="#E84D8A")

	#x = np.arange(1, 351)
	#y = 4.3 * x
	#ax.plot(x, y, color="gray", label="y=4.3x", linestyle=":")

	ax.set_ylabel("Čas [s]", fontsize=20)
	ax.set_xlabel("Počet hradel", fontsize=20)
	ax.tick_params(axis='both', which='major', labelsize=16)

	plt.savefig("scalability_time.png")
	plt.show()

if __name__ == "__main__":
	main()