# 5.6 Conversion: Write a function to determine the number of bits you would need to flip to convert
# integer A to integer B.
# EXAMPLE
# Input:29 (or: 11101), 15 (or: 01111)
# Output: 2


# SOLUTION
from c5_bit_manipulation.general_bit_manipulation_in_python import binary

def transfom(a,b):
    a = a ^ b
    return sum(binary(a, a.bit_length()))

print(transfom(0b11101, 0b01111))