# 10.8 Find Duplicates: You have an array with all the numbers from 1 to N, where N is at most 32,000. The
# array may have duplicate entries and you do not know what N is. With only 4 kilobytes of memory
# available, how would you print all duplicate elements in the array?

# Solution 4kB of mem = 4*1024*8 bits = 2^(10+3+2) = 2^15 bits = 32*1024
# We use the same encoding as before and when we have 1 already we report that duplicate
class BitSet():
    def __init__(self, size_in_bytes):
        self.memory = [0]*size_in_bytes

    def set(self, value):
        position_in_memory = value // 8
        offset_in_byte = value % 8
        self.memory[position_in_memory] = self.memory[position_in_memory] | (1<<offset_in_byte)

    def check(self, value):
        position_in_memory = value // 8
        offset_in_byte = value % 8
        return (self.memory[position_in_memory] & (1 << offset_in_byte)) >> offset_in_byte

bit_set = BitSet(4)
my_list = [1,2,3,4,5,6,7,8,9,10, 8,11,12, 5]
for element in my_list:
    print(f"{element}:{bit_set.check(element)}")
    if bit_set.check(element) == 0:
        bit_set.set(element)
        print(f"{element}:{bit_set.check(element)}")
    else:
        print(f"Duplicate {element}")


