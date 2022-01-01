import timeit
import Global
import math


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
    for i in range(0, n):
        # Find the maximun value in a column in order to change lines
        maxElem = abs(U[i][i])
        maxRow = i
        for k in range(i + 1, n):
            if abs(U[k][i]) > maxElem:
                maxElem = abs(U[k][i])
                maxRow = k

        # Swap the rows pivoting the maxRow
        for k in range(i, n):
            tmp = U[maxRow][k]
            U[maxRow][k] = U[i][k]
            U[i][k] = tmp

        #  Subtract lines
        for k in range(i + 1, n):
            c = U[k][i] / float(U[i][i])
            L[k][i] = c  # Store the multiplier
            for j in range(i, n):
                U[k][j] -= c * U[i][j]  # Multiply with the pivot line and subtract

    n = len(L)

    # substitution Ly=b

    y = [0 for i in range(n)]
    for i in range(0, n, 1):
        y[i] = b[i] / float(L[i][i])
        for k in range(0, i, 1):
            y[i] -= y[k] * L[i][k]
    n = len(U)

    # substitution Ux=y
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


def gauss_elimination(A):
    n = len(A) # Give us total of lines

    for i in range(0, n):
        # Find the maximun value in a column in order to change lines
        maxElem = abs(A[i][i])
        maxRow = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > maxElem:
                maxElem = abs(A[k][i])  # Next line on the diagonal
                maxRow = k

        # Swap the rows pivoting the maxRow
        for k in range(i, n+1):
            tmp = A[maxRow][k]
            A[maxRow][k] = A[i][k]
            A[i][k] = tmp

        #  Subtract lines
        for k in range(i + 1, n):
            c = A[k][i] / float(A[i][i])
            for j in range(i, n+1):
                A[k][j] -= c * A[i][j]  # Multiply with the pivot line and subtract

    # A=[X|b]
    # b vector
    b = [0 for i in range(n)]
    for i in range(0, n):
        b[i] = A[i][n]

    # Fill X matrix
    X = [[0 for i in range(0, n)] for i in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            X[i][j] = A[i][j]
    # backward substitution
    x = [0 for i in range(n)]
    for i in range(len(X) - 1, -1, -1):
        x[i] = b[i]
        for j in range(0, len(X[0])):
            if i != j:
                x[i] -= x[j] * X[i][j]
        x[i] = x[i] / X[i][i]

    print('X:')
    for row in X:
        print(row)

    for i in range(len(x)):
        print(f'd{i + 1}={x[i]}')

    return x


if __name__ == '__main__':
    m = [[8, 4, -1, 11], [-2, 3, 1, 4], [2, -1, 6, 7]]
    m2 = [[1, 1, -1, -3], [6, 2, 2, 2], [-3, 4, 1, 1]]
    x = LU(m)
    y = gauss_elimination(m2)
