# 10.10 Rank from Stream: Imagine you are reading in a stream of integers. Periodically, you wish
# to be able to look up the rank of a number x (the number of values less than or equal to x).
# Implement the data structures and algorithms to support these operations. That is, implement
# the method track(int x), which is called when each number is generated, and the method
# getRankOfNumber(int x), which returns the number of values less than or equal to x (not
# including x itself).
# EXAMPLE
# Stream(in order of appearance):5, 1, 4, 4, 5, 9, 7, 13, 3
# getRankOfNumber(l) 0
# getRankOfNumber(3) 1
# getRankOfNumber(4) 3

# Solution - Brute Force - keep a sorted array of distinct numbers - high insert complexity
# Alternative - keep a Binary Search Tree which also keep the counts of "how many smaller" and updates on insert

#Brute force solution
import random
from c10_sorting_and_searching.binary_search import binary_search

class TrackedStreamBruteForce(object):
    def __init__(self):
        self.data = []

    def track(self, new_element: int) -> None:
        self.data.append(new_element)
        self.data.sort()

    def get_rank(self, element: int) -> int:
        rank: int = binary_search(self.data, element)
        return rank

my_list = [random.randint(0,200) for x in range(100000)]

#my_list = [1,2,3,4,5,6,7,8]*1000000
my_int_stream = (x for x in my_list)

tracked_stream = TrackedStreamBruteForce()
for element in my_int_stream:
    tracked_stream.track(element)
    #print(f"element: {element} - position: {tracked_stream.get_rank(element)}")

print(len(my_list))
print(len(tracked_stream.data))