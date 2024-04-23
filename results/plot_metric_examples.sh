#!/bin/bash

python3 plot_results.py --type bar --noshow --metric error_prob --mult mul8u_2NDH -c 1
python3 plot_results.py --type bar --noshow --metric error_prob --mult mul8u_12KA -c 2
python3 plot_results.py --type bar --noshow --metric error_prob --mult mul8u_ZB3 -c 3
python3 plot_results.py --type bar --noshow --metric error_prob --mult mul8u_17MJ -c 4

python3 plot_results.py --type bar --noshow --metric mean_abs_error --mult mul8u_197B -c 1
python3 plot_results.py --type bar --noshow --metric mean_abs_error --mult mul8u_2NDH -c 2
python3 plot_results.py --type bar --noshow --metric mean_abs_error --mult mul8u_ZB3 -c 3
python3 plot_results.py --type bar --noshow --metric mean_abs_error --mult mul8u_17MN -c 4

python3 plot_results.py --type bar --noshow --metric mean_relative_error --mult mul8u_1A0M -c 1
python3 plot_results.py --type bar --noshow --metric mean_relative_error --mult mul8u_197B -c 2
python3 plot_results.py --type bar --noshow --metric mean_relative_error --mult mul8u_12KA -c 3
python3 plot_results.py --type bar --noshow --metric mean_relative_error --mult mul8u_R92 -c 4

python3 plot_results.py --type bar --noshow --metric mean_squared_error --mult mul8u_GTR -c 1
python3 plot_results.py --type bar --noshow --metric mean_squared_error --mult mul8u_ZB3 -c 2
python3 plot_results.py --type bar --noshow --metric mean_squared_error --mult mul8u_12KA -c 3
python3 plot_results.py --type bar --noshow --metric mean_squared_error --mult mul8u_R92 -c 4

python3 plot_results.py --type bar --noshow --metric worst_case_error --mult mul8u_12KA -c 1
python3 plot_results.py --type bar --noshow --metric worst_case_error --mult mul8u_17R6 -c 2
python3 plot_results.py --type bar --noshow --metric worst_case_error --mult mul8u_2NDH -c 3
python3 plot_results.py --type bar --noshow --metric worst_case_error --mult mul8u_GTR -c 4

python3 plot_results.py --type bar --noshow --metric worst_case_relative_error --mult mul8u_197B -c 1
python3 plot_results.py --type bar --noshow --metric worst_case_relative_error --mult mul8u_Z9D -c 2
python3 plot_results.py --type bar --noshow --metric worst_case_relative_error --mult mul8u_R92 -c 3
python3 plot_results.py --type bar --noshow --metric worst_case_relative_error --mult mul8u_17MJ -c 4

echo 'Done!'