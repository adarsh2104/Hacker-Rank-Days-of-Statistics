
#  Github    : https://github.com/adarsh2104
#  HR-Profile: https://www.hackerrank.com/adarsh_2104
#  Challenge : https://www.hackerrank.com/challenges/s10-quartiles
#  Max Score : 30



def find_median(array):
    if len(array) % 2 == 1:
        return array[len(array) // 2]
    else:
        return (array[len(array) // 2] + array[len(array) // 2 - 1]) // 2


n = input()
input_array = sorted([int(x) for x in input().split()])
print(find_median(input_array[:len(input_array)//2]))
print(find_median(input_array))
print(find_median(input_array[len(input_array) // 2 + len(input_array) % 2:]))
