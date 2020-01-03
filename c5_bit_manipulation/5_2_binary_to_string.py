# 5.2 Binary to String: Given a real number between O and 1 (e.g., 0.72) that is passed in as a double, print
# the binary representation. If the number cannot be represented accurately in binary with at most 32
# characters, print "ERROR:'

# Solution: binary reprezentation of a fractional number is done by repeatedly  multiplying with 2 and keeping the int part
# Example : 0.5 is 1
# 0.25 is 10

def binary_float(float_number, max_len=32):
    mantis_len = 0
    binary_repr = []
    while mantis_len < max_len and float_number != 0.0:
        digit = int(float_number * 2)
        float_number = (float_number *2) - digit
        mantis_len +=1
        binary_repr.append(digit)
    return binary_repr

print(binary_float(1/2 + 1/8 +1/16))



