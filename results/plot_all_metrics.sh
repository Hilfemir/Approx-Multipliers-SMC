#!/bin/bash

## all valid multipliers
declare -a mults=(
				 "mul8u_17MN" "mul8u_17MJ" 
				 "mul8u_R36" "mul8u_1A0M"
				 "mul8u_Z9D" "mul8u_17R6"
				 "mul8u_2NDH" "mul8u_197B"
			 	 "mul8u_NLX" "mul8u_GTR"
				 "mul8u_BG1" "mul8u_R92"
				 "mul8u_ZB3" "mul8u_12KA"
				)

## all used metrics
declare -a metrics=("error_prob" "mean_abs_error"
					"mean_relative_error" "mean_squared_error"
					"worst_case_error" "worst_case_relative_error")

## loop through each multiplier for each metric
for metric in "${metrics[@]}"
do
   for mult in "${mults[@]}"
   do
	   ## generate plot
	   python3 plot_results.py --type bar --metric $metric --mult $mult --noshow
   done
done

echo 'Done!'