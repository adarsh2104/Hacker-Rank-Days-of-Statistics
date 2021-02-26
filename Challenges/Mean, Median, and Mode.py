
#  Github    : https://github.com/adarsh2104
#  HR-Profile: https://www.hackerrank.com/adarsh_2104
#  Challenge : https://www.hackerrank.com/challenges/s10-basic-statistics/problem
#  Max Score : 30


import numpy as np
from scipy import stats

numbers = int(input())
input_array = sorted([int(x) for x in input().split()])
print(np.mean(input_array))
print(np.median(input_array))
print(stats.mode(input_array)[0][0])
