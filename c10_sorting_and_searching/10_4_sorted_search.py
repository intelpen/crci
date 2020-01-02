# 10.4 Sorted Search, No Size: You are given an array-like data structure Listy which lacks a size
# method. It does, however, have an elementAt ( i) method that returns the element at index i in
# 0( 1) time. If i is beyond the bounds of the data structure, it returns -1. (For this reason, the data
# structure only supports positive integers.) Given a Li sty which contains sorted, positive integers,
# find the index at which an element x occurs. If x occurs multiple times, you may return any index.
# Hints: #320, #337, #348

# Solution - it would be nice to have a reversed kind of binary search
# we check in 2, 4, 8, until we obtain an element larger than x. then we search in the last interval

class Listy(object):
    def __init__(self, data):
        self.data = data
    def __getitem__(self, index):
        if index >= len(self.data):
            return -1
        return self.data[index]
    def __len__(self):
        raise NotImplementedError()

def binary_search(data, element, left, right):

    while left <= right:
        middle = (left + right) // 2
        if data[middle] < element:
            left = middle +1
        elif data[middle] > element:
            right = middle -1
        else:
            return middle
    return None

def sorted_search_no_size(listy, element):
    if listy[0] == element:
        return 0
    left = 0
    right = 1
    while listy[right] > -1 and listy[right] < element:
        right = right *2
    print(right)
    if listy[right] == -1:
        right = find_len(listy, right // 2)
    print(f"left{left}")
    print(f"right{right}")
    return binary_search(listy, element, left, right)

def find_len(listy, left):
    right = left * 2
    while left < right:
        middle = (right + left) // 2
        if listy[middle] > -1 :
            left = middle +1
        elif listy[middle] == -1:
            right = middle -1
    return right

listy = Listy([1,3,5,6,7,8,10])
#print(find_len(listy,5))
print(sorted_search_no_size(listy, 2))