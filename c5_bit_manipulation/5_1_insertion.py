# 5.1 Insertion: You are given two 32-bit numbers, N and M, and two bit positions, i and
# j. Write a method to insert M into N such that M starts at bit j and ends at bit i. You
# can assume that the bits j through i have enough space to fit all of M. That is, if
# M = 10011, you can assume that there are at least 5 bits between j and i. You would not, for
# example, have j = 3 and i = 2, because M could not fully fit between bit 3 and bit 2.
# EXAMPLE
# Input: N 10000000000, M
# Output: N = 10001001100
# Hints: #137, #769, #215

#Solution - injection here means that M overrides a part of N, with eventually filling with 0s if needed

from c5_bit_manipulation.general_bit_manipulation_in_python import binary

def insertion(n: int, m:int, i:int, j:int) -> int:
    int_len = 32
    length_insertion = j-i
    length_m = m.bit_length()
    mask_right = (1 << i) -1 # create 00000111 , with i of 1
    mask_left = ((-1) <<j) # create 110000000, with j of zeros
    mask = mask_left & mask_right
    delete_j_to_i = n & mask
    m = m << (j-length_m+1) #moved m in the right position
    return n | m

n = 0b10000000000
m = 0b10011
print(f"n:{binary(n)}")
print(f"m:{binary(m)}")
k = insertion(n,m, 2,6)
print(f'k:{binary(k)}')

