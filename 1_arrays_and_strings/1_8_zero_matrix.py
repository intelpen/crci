# 1.8 Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and
# column are set to 0.

# solution - with copy simple O(M*N) * O(max(N,M) * no elements)
# with 2 vectors - cycle through all matrix and note lines and columns whic need to be 0

def zero_matrix(matrix):
    m = len(matrix)
    n = len(matrix[0])
    print(m)
    print(n)
    lines_zero = set()
    columns_zero = set()
    for line in range(m):
        for column in range(n):
            print(f"{line} : {column}")
            if matrix[line][column] == 0:
                lines_zero.add(line)
                columns_zero.add(column)

    for line in lines_zero:
        for col in range(n):
            matrix[line][col] = 0

    for column in columns_zero:
        for line in range(m):
            matrix[line][column] = 0

    return matrix


a = [[1, 0, 1],[1,1,1],[1,1,1]]
print(a)
print(zero_matrix(a))
