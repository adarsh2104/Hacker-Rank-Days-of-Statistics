
#  Github    : https://github.com/adarsh2104
#  HR-Profile: https://www.hackerrank.com/adarsh_2104
#  Challenge : https://www.hackerrank.com/challenges/s10-weighted-mean
#  Max Score : 30
# 

numbers = int(input())
input_array = [int(x) for x in input().split()]
input_weights = [int(x) for x in input().split()]
w_mean = 0  
for number,weight in zip(input_array,input_weights):
    w_mean += (number * weight)
print(round((w_mean/sum(input_weights)),1))
