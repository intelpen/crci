# 10.11 Peaks and Valleys: In an array of integers, a "peak" is an element which is greater than or equal
# to the adjacent integers and a "valley" is an element which is less than or equal to the adjacent
# integers. For example, in the array {5, 8, 6, 2, 3, 4, 6}, {8, 6} are peaks and {5, 2} are valleys. Given an
# array of integers, sort the array into an alternating sequence of peaks and valleys.
# EXAMPLE
# Input: {5, 3, 1, 2, 3}
# Output: {5, 1, 3, 2, 3}
from typing import List

def peak_and_valleys(data: List[int]) -> None:
    data.sort()
    for i in range(1, len(data)-1, 1):
        if data[i-1] < data[i] and (data[i] < data[i+1]):
            aux = data[i]
            data[i] = data[i+1]
            data[i+1] = aux

my_list: List[int] = [5,3,3,1,2,3]
print(my_list)
peak_and_valleys(my_list)
print(my_list)