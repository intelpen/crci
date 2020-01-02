# 10.7 Missing Int: Given an input file with four billion non-negative integers, provide an algorithm to
# generate an integer that is not contained in the file. Assume you have 1 GB of memory available for
# this task.
# FOLLOW UP
# What if you have only 1 O MB of memory? Assume that all the values are distinct and we now have
# no more than one billion non-negative integers.

# Solution 4Billion integers = 4G * 2(or 4)bytes  = 8-16GB
# 1. 1GB available

import random
max_int = 2**4-1
no_elements = 4 * ( 1<<2)
bits_in_integer = 4 #32
print(f"max_inf{max_int}")
print(f"no_elements{no_elements}")
my_file = list(random.randint(0,max_int) for x in range(no_elements))
my_file = [0,1,3,4,5,6,7,9,10,11,12,13,15,15]
print(my_file)
#my_file = random.sample(range(0,max_int), no_elements)
#print(my_file[4:60])

#construct bit map
bit_map = [0]*(no_elements//bits_in_integer)
for element in my_file:
    position_in_map = element//bits_in_integer
    bit_offset = element % bits_in_integer
    bit_map[position_in_map] = bit_map[position_in_map] | (1<<bit_offset)

for element in my_file:
    print("{0:b}".format(element))
#find the missing numbers
for (position_in_map,bits) in enumerate(bit_map):
    for i in range(bits_in_integer):
        if bit_map[position_in_map] & (1<<i) == 0:
            print(f"Missing: {position_in_map * bits_in_integer + i}")

########################################################################
# Followup : if we have 1MB of memory  - 2^20 bytes = 2^28 bit
# And we have 1Billion = 2^30  integer numbers (2^34 bytes of info)
# Then I will go through the file n times = number_of_numbers/1<<24 = 2^30 /2^20 = 1024 times (or just 4 times if bit codif)
# and select the numbers in the bucket [i:(i+1)] * numbers_in_memory and apply same algo


#Another aproach, first pass - count the elements in each bucket - then on second pass look which element from a bucket is missing