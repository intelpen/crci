# 10.1 Sorted Merge: You are given two sorted arrays, A and B, where A has a large enough buffer at the
# end to hold B. Write a method to merge B into A in sorted order.

# Solution: start from the end  and have two running indexes in A and B

def merge_sorted(a, b, l_a, l_b):
    current = l_a + l_b + 1
    while (l_a >=0) and (l_b >= 0):
        if a[l_a] > b[l_b]:
            a[current] = a[l_a]
            l_a -= 1
        else:
            a[current] = b[l_b]
            l_b -= 1
        current -=1
    if l_b > 0:
        a[0:l_b + 1] = b[0:l_b +1]

a = [5, 6 , 7, 8 , 9]
l_a = len(a)-1
b = [3,4]
l_b = len(b) -1
a = a + b
merge_sorted(a, b, l_a, l_b)
print(a)


