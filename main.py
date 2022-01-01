import timeit
import Global
import math
from math import sin, cos, tan, log


def LU(A):
    n = len(A)  # Give us total of lines

    # b vector
    b = [0 for i in range(n)]
    for i in range(0, n):
        b[i] = A[i][n]

    # Fill L matrix and its diagonal with 1
    L = [[0 for i in range(n)] for i in range(n)]
    for i in range(0, n):
        L[i][i] = 1

    # Fill U matrix
    U = [[0 for i in range(0, n)] for i in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            U[i][j] = A[i][j]

    n = len(U)

    # Find both U and L matrices
    for i in range(0, n):  # for i in [0,1,2,..,n]
        # Find the maximun value in a column in order to change lines
        maxElem = abs(U[i][i])
        maxRow = i
        for k in range(i + 1, n):  # Interacting over the next line
            if abs(U[k][i]) > maxElem:
                maxElem = abs(U[k][i])  # Next line on the diagonal
                maxRow = k

        # Swap the rows pivoting the maxRow, i is the current row
        for k in range(i, n):  # Interacting column by column
            tmp = U[maxRow][k]
            U[maxRow][k] = U[i][k]
            U[i][k] = tmp

        #  Subtract lines
        for k in range(i + 1, n):
            c = -U[k][i] / float(U[i][i])
            L[k][i] = -c  # Store the multiplier
            for j in range(i, n):
                U[k][j] += c * U[i][j]  # Multiply with the pivot line and subtract

        #  Make the rows bellow this one zero in the current column
        for k in range(i + 1, n):
            U[k][i] = 0
    n = len(L)

    # (5) Perform substitutioan Ly=b

    y = [0 for i in range(n)]
    for i in range(0, n, 1):
        y[i] = b[i] / float(L[i][i])
        for k in range(0, i, 1):
            y[i] -= y[k] * L[i][k]
    n = len(U)

    # (6) Perform substitution Ux=y
    # backward substitution
    x = [0 for i in range(n)]
    for i in range(len(U) - 1, -1, -1):
        x[i] = y[i]
        for j in range(0, len(U[0])):
            if i != j:
                x[i] -= x[j] * U[i][j]
        x[i] = x[i] / U[i][i]

    print('U:')
    for row in U:
        print(row)

    print('L:')
    for row in L:
        print(row)

    for i in range(len(y)):
        print(f'd{i + 1}={y[i]}')

    for i in range(len(x)):
        print(f'x{i + 1}={x[i]}')
    return x


if __name__ == '__main__':
    m = [[8, 4, -1, 11], [-2, 3, 1, 4], [2, -1, 6, 7]]
    x = LU(m)
