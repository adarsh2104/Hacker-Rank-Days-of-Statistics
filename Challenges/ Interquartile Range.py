
#  Github    : https://github.com/adarsh2104
#  HR-Profile: https://www.hackerrank.com/adarsh_2104
#  Challenge : https://www.hackerrank.com/challenges/s10-interquartile-range
#  Max Score : 30


numbers = int(input())
input_array = [int(x) for x in input().split()]
input_freq = [int(x) for x in input().split()]


def find_medium_sum(array):
    if len(array) % 2 == 1:
        return array[len(array) // 2]
    else:
        return (array[len(array) // 2] + array[len(array) // 2 - 1]) / 2
    
        
final_list = []
for index in range(numbers):
    final_list += ([input_array[index]] * input_freq[index])

final_list.sort()

inter_qrange = float(find_medium_sum(final_list[len(final_list) // 2 + len(final_list) % 2:]) - find_medium_sum(final_list[:len(final_list)//2]))
print(inter_qrange)
