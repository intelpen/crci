# 10.9 Sorted Matrix Search: Given an M x N matrix in which each row and each column is sorted in
# ascending order, write a method to find an element.

#Solution - Matrix MxN
# 1.Brute force : binary_Search on each row O(M*log(N))
# 2. eliminate a row or a column at a timebased on the top-right element comparison with the searched element - O(max(N,M)
# 3. 2D binary search - rather complicated but possible

def find_element(matrix, element):
    row = 0
    column = len(matrix[0])-1

    while row<len(matrix) and column>0:
        if matrix[row][column] ==element:
            return True
        elif matrix[row][column] >element:
            column -=1
        else:
            row +=1
    return False

matrix = [[15,20,40,85],[20,35,80,95],[30,55,95,105],[30,55,95,105],[40,80,100,120]]
print(find_element(matrix,0))