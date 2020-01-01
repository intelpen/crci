#Radix sort - we sort by each digit, starting with least significant

def sort_digit(data, digit_mask):
    aux_lists = [[]  for x in range (10)]
    for element in data:
        digit = (element//digit_mask) % 10
        aux_lists[digit].append(element)
    return_list = [y for x in aux_lists for y in x]
    data[:] = return_list[:]



def radix_sort(data):
    max_element = max(data)
    digit_mask = 1
    while max_element > digit_mask:
        sort_digit(data, digit_mask)
        digit_mask *= 10

data = [170, 45, 75, 90, 802, 24, 2, 66]
print(data)
radix_sort(data)
print(data)
