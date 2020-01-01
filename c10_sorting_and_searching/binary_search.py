# Binary search - divide et impera (the array have to be sorted)

def binary_search_rec(data, element, left, right):
    if left == right:
        if data[left] == element:
            return element
        else:
            return None
    middle = (left + right) //2
    if element < data[middle]:
        return binary_search_rec(data, element, left, middle)
    elif element > data[middle]:
        return binary_search_rec(data, element, middle + 1, right)
    else:
        return middle

def binary_search(data, element):
    left = 0
    right = len(data)-1
    while (left <= right):
        mid = (left + right) // 2
        if element < data[mid]:
            right = mid-1
        elif element>data[mid]:
            left = mid +1
        else:
            return mid #is equal to the mid


data = [1,4,5,6,7]
index = binary_search_rec(data, element = 6, left = 0, right =len(data) - 1)
index2 = binary_search(data, element = 6)
print(index)
print(index2)