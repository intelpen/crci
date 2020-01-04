# 5.7 Pairwise Swap: Write a program to swap odd and even bits in an integer with as few instructions as
# possible (e.g., bit O and bit 1 are swapped, bit 2 and bit 3 are swapped, and so on).

# One solution: take even bits, shift left, take even bits ans shift right and do sum

def pairwise_swap(a):
    print(bin(a))
    odd = a & (0b10101010)
    print(bin(odd))

    print(bin(odd >> 1))

    even = a & (0b01010101)
    print(bin(even))
    print(bin(even<<1))
    return (even << 1) | (odd>>1)

print(bin(pairwise_swap(0b1010111)))
#print(bin(pairwise_swap(0b1100010)))

