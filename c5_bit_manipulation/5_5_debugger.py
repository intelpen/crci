# 5.5 Debugger: Explain what the following code does: ((n & (n-1 )) == 0).

#Solution

# - flips last bits 0
# x = 10110000
# x-1 = 10101111
# x & (x-1) = 1010000 -> total result = number with last 1 bit set to 0
#
# x = 1111
# x-1 = 1110
# x & (x-1) = 1110
#
# x = 0
# x-1 = 111111
# x & (x-1) = 0
#
# x = 1
# x-1 = 0
# x & (x-1) = 0

# In total verify if the element is a power of 2

def power_of_2(n: int) -> bool:
    return (n & (n-1)) == 0

for x in range(-10,10,1):
    print(f"{x}: {bin(x)}:{bin(x-1)}:{bin(x & (x-1))} : {power_of_2(x)}")
