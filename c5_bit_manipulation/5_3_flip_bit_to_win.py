# 5.3 Flip Bit to Win: You have an integer and you can flip exactly one bit from a O to a 1. Write code to
# find the length of the longest sequence of 1 s you could create.
# EXAMPLE
# Input: 1775
# Output: 8

# Solution -> transforms in counts of ones and go through the counts and see which ones are meargeable
from typing import List
from c5_bit_manipulation.general_bit_manipulation_in_python import  binary


def encode_as_lengths(n: int) -> List[int]:
    bit_length = n.bit_length()
    bits =  binary(n, bit_length-1)
    print(bits)
    prev_bit = 1
    length_ones = 0
    encoding = []
    for bit in bits:
        if bit == 1:
            length_ones +=1
        else:
            #bit =0
            if prev_bit == 1:
                encoding.append(length_ones)
            length_ones = 0
            encoding.append(0)
        prev_bit = bit
    if prev_bit == 1:
        encoding.append(length_ones)

    return encoding

def flip_to_win(number):
    encoded = encode_as_lengths(number)
    max_length = encoded[0] +1
    for i in range(1,len(encoded)-1,1):
        if encoded[i]==0:
            curr_max_len = encoded[i-1] +1+encoded[i+1]
            if max_length < curr_max_len:
                max_length = curr_max_len
    return max_length



print(encode_as_lengths(0b11011101111))
print(flip_to_win(0b11011101111))



