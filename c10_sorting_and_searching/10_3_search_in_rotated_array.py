# 10.3 Search in Rotated Array: Given a sorted array of n integers that has been rotated an unknown
# number of times, write code to find an element in the array. You may assume that the array was
# originally sorted in increasing order.
# EXAMPLE
# lnput: find 5 in{15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14}
# Output: 8 (the index of 5 in the array)

#Solution ... some variation of binary sort .... (brute would be to rotate the array then do binary sort ...
# .. but this would be o(N)

#Solution 2 ... some half part of the array is ordered correctly - and do a complicated binary search ich ....
