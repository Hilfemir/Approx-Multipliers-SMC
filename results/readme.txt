Results of all simulations
Structure of this folder (example):
                                              |--- plot1.png
			              |--- multiplier1 ---|--- plot2.png
 randgen_distribution1 ---|--- multiplier2    |--- some_data.csv
			              |--- multiplier3    |--- ........
		                  |--- ..........
			              |--- specification.txt
                          |--- distribution_plots


			              |--- ...
 randgen_distribution2 ---|--- ...
			              |--- ...

Details about each distribution (parameters, shifts, etc.) are in the
specification.txt files in their respective folders. Plots are in the distribution_plots folder.

---------------------------------------------------------------------------------------------------------------

Meanings of plots in the distribution_plots folders:

- *_bit_flips.png - Densities of each input bit flipping with each incoming input number.

- *_heatmap.png - Heatmap of density of multiplication pairs in selected algorithm.

- *_randgen_bit_flips.png - Randomly generated bit flips modelled based on the distribution from *_bit_flips.png.

- *_randgen_numbers.png - Randomly generated numbers modelled based on the distribution from *_singular.png.

- *_singular.png - Densities of input numbers plotted individually.

---------------------------------------------------------------------------------------------------------------

Meanings of all relevant simulations and their results in the all_res.png files (found in multiplier folders):

- 'E[<=25000; 4] (max: input_a)' - Max value of the first input number.

- 'E[<=25000; 4] (max: input_b)' - Max value of the second input number.

- 'E[<=500000; 1] (max:res_count)' - Number of all obtained results.

- 'E[<=500000; 4] (max:dif_count)' - Number of results where acc. and approx. results differed.

- error_prob, ..., hamming_distance - Should be self-explanatory.

- 'E[<=500000; 4] (max:bit_flips)' - Most gate bit flips during the calculation of one single result.

- 'E[<=500000; 4] (max:avg_flips_per_res)' - Average number of bit flips per all results.

- 'E[<=500000; 4] (max:bit_flips_sum)' - Sum of all gate bit flips.

- 'simulate [<=2000;1] {bits[0], 2+bits[1], ...}' - (input_bits.png) Visualisation of the jitter of input bits.

- 'simulate [<=2000;1] { input_a, input_b }' - (input_numbers.png) Visualisation of the jitter of input numbers.

- 'simulate[<=10000;1] {res_acc, res_approx}' - (res_diffs.png) Results of both acc. and approx. mults. plotted.
