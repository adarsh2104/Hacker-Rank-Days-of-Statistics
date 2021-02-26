
#  Github    : https://github.com/adarsh2104
#  HR-Profile: https://www.hackerrank.com/adarsh_2104
#  Challenge : https://www.hackerrank.com/challenges/s10-standard-deviation
#  Max Score : 30


from math import sqrt

numbers = int(input())
input_array = sorted([int(x) for x in input().split()])

mean = sum(input_array) /numbers
numerator = 0
for number in input_array:
    numerator += pow((number-mean),2)
    
print(round(sqrt(numerator/numbers),1))    
