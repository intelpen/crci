# Convert byte_string to int with base
print(int("10101",2))
#Write from 0b1010
print(0b1010)
#Encoding of integers
def get_bit(n, position):
    return (n & (1<<position)) >> position

def binary(n:int, length: int = 32):
    bits =[]
    while length >= 0:
        bits.append(get_bit(n, length))
        length -=1
    return bits

#positive - normal encoding
#negative - 2 complement variant
print(binary(2))
print(binary(-2))
print(get_bit(2,0))

#get the number of bits
print(int.bit_length(3))
#Write in binary form : bin
for i in range(-10,10,1):
    print(bin(i), binary(i,length =8))

# In python a negative number when shifted stays negative  - we have what is called arithmetic right shift as the sign
# bit is always filed
# There is no logical right shift (right shift with no fill to the left - or fill with 0)

#Common operations


def set_bit(n, position):
    return n | (1<<position)


def clear_bit(n, position):
    return n & (~(1<<position))

def update_bit_with_value(n, position, bit_value):
    if bit_value == 1:
        set_bit(n, position)
    else:
        clear_bit(n, position)