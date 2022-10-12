# python 3.8.13
# transform_matrix_into_RREF.py

# Created on Oct 4 14:52:20 2022
# @author: yinchaoyang
# --- utf-8 ---

# Transform a n*m matrix into the REDUCED ROW ECHELON FORM.

import numpy as np

# Transform a matrix into a row echelon form through the Gauss Elimination.
def Gauss_Elimination(matrix, row, column):
    for n in range(min(row, column)):

        # prevent the pivot from being 0
        if matrix[n][n] == 0:
            column_no_zero = []
            for i in range(n, row + 1):
                column_no_zero_i = matrix[n][i]
                column_no_zero.append(abs(column_no_zero_i))
            index_max = column_no_zero.index(max(column_no_zero))
            matrix[n], matrix[index_max] = matrix[index_max], matrix[n]

        # Gauss elimination.
        if n + 1 < row:
            for k in range(n + 1, row): # n+1 <= k < row
                coefficient = matrix[k][n] / matrix[n][n]
                for i in range(column):
                    matrix[k][i] = matrix[k][i] - coefficient * matrix[n][i]
            
    return matrix



# Transform a row echelon form (from the Gauss Elimination Algorithm) into RREF.
def RREF(matrix, row, column):
    matrix = Gauss_Elimination(matrix, row, column)
    for n in range(min(row, column)):
        if matrix[n][n] != 0:
            # turn the pivots into 1
            temp = matrix[n][n]
            for m in range(column):
                matrix[n][m] = matrix[n][m] / temp

            # turn all the other entries in that column into 0 
            for k in range(n): # 0 <= k <= n-1, row
                # row_k <-- row_k - coefficient * row_n
                coefficient = matrix[k][n] / matrix[n][n]
                for i in range(column):
                   matrix[k][i] = matrix[k][i] - coefficient * matrix[n][i]
    
    return matrix


if __name__ == '__main__':
    # Input the matrix.
    print("Please input a n*m matrix.")
    row = int(input("First input the number of row n: "))
    column = int(input("And the number of the column m: "))
    print("Then please input the matrix by row.")
    matrix = np.zeros(row * column).reshape((row, column)) # initialize the n*m matrix
    for i in range(row):
        everyRow = input("Input row %d (%d numbers), split by ' ': " % (i + 1, column))
        matrix[i] = [int(j) for j in everyRow.split()]

    # Transform the matrix into the RREF.
    matrix_RREF = RREF(matrix, row, column)
    print("The RREF of the matrix is: ")
    print(matrix_RREF)