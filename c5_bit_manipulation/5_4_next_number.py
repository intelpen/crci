# 5.4 Next Number: Given a positive integer, print the next smallest and the next largest number that
# have the same number of 1 bits in their binary representation.

# Solution: add 1 and count 1s bits
# Better solution: think it aritmethically

from c5_bit_manipulation.general_bit_manipulation_in_python import binary

def count_ones(number: int):
    binary_representation = binary(number, number.bit_length() - 1)
    return sum(binary_representation)

def get_next(number):
    if number ==0:
        return 0
    initial_sum= count_ones(number)

    while count_ones(number+1) != initial_sum:
        number +=1
    return number+1


def get_prev(number):
    if number == 0:
        return 0
    initial_sum = count_ones(number)
    while count_ones(number-1) != initial_sum:
        number -= 1
    return number-1

print(bin(get_next(0b100)))
print(bin(get_next(0b101)))
print(bin(get_prev(0b100)))
print(bin(get_prev(0b101)))

