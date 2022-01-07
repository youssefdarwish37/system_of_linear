import timeit
import Global
import math


def LU(A):
    n = len(A)  # Give us total of lines

    # Find the maximum value in a column in order to change lines

    i = 0
    maxRow = i

    for k in range(i + 1, n):
        if abs(A[k][i]) > abs(A[maxRow][i]):
            maxRow = k

    # Swap the rows pivoting the maxRow
    for k in range(i, n + 1):
        tmp = A[maxRow][k]
        A[maxRow][k] = A[i][k]
        A[i][k] = tmp

    # b vector
    b = [0 for i in range(n)]
    for i in range(0, n):
        b[i] = A[i][n]
    print(b)
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
        #  Subtract lines
        for k in range(i + 1, n):
            c = U[k][i] / float(U[i][i])
            L[k][i] = c  # Store the multiplier
            for j in range(i, n):
                U[k][j] -= c * U[i][j]  # Multiply with the pivot line and subtract

    # # Checking if L*U =A
    # result = [0 for i in range(n)]
    # for i in range(len(L)):
    #     # iterate through columns of Y
    #     for j in range(len(U[0])):
    #         # iterate through rows of Y
    #         for k in range(len(U)):
    #             result[i][j] += L[i][k] * U[k][j]
    #
    # n = len(L)

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

    # print('L*U=A:')
    # for r in result:
    #     print(r)

    for i in range(len(y)):
        print(f'd{i + 1}={y[i]}')

    for i in range(len(x)):
        print(f'x{i + 1}={x[i]}')
    return x


def gauss_elimination(A):
    n = len(A)  # Give us total of lines

    for i in range(0, n):
        # Find the maximum value in a column in order to change lines
        maxRow = i

        for k in range(i + 1, n):
            if abs(A[k][i]) > abs(A[maxRow][i]):
                maxRow = k

        # Swap the rows pivoting the maxRow
        for k in range(i, n + 1):
            tmp = A[maxRow][k]
            A[maxRow][k] = A[i][k]
            A[i][k] = tmp

        #  Subtract lines
        for k in range(i + 1, n):
            c = A[k][i] / float(A[i][i])
            for j in range(i, n + 1):
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


def gauss_jordan(A):
    n = len(A)  # Give us total of lines

    for i in range(0, n):
        #  Find the maximum value in a column in order to change lines
        maxRow = i
        #
        for k in range(i + 1, n):
            if abs(A[k][i]) > abs(A[maxRow][i]):
                maxRow = k

        # Swap the rows pivoting the maxRow
        for k in range(i, n + 1):
            tmp = A[maxRow][k]
            A[maxRow][k] = A[i][k]
            A[i][k] = tmp

        # making main diagonal =1
        m = float(A[i][i])
        for k in range(i, n + 1):
            A[i][k] = A[i][k] / m
        #  Subtract lines
        for k in range(i + 1, n):
            c = A[k][i] / float(A[i][i])
            for j in range(i, n + 1):
                A[k][j] -= c * A[i][j]  # Multiply with the pivot line and subtract

        if i > 0:
            for k in range(0, i):
                d = A[k][i] / float(A[i][i])

                for j in range(k, n + 1):
                    A[k][j] -= d * A[i][j]  # Multiply with the pivot line and subtract

        #  Subtract lines
        for k in range(i + 1, n):
            c = A[k][i] / float(A[i][i])
            for j in range(i, n + 1):
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


def gauss_seidel(a, epsilon):
    x0, y0, z0 = 0, 0, 0
    # iterations += '%d \t [%.6f \t %.6f\t %.6f]\n' % (0, x1, x2, x3)
    x1, x2, x3 = 0, 0, 0
    for i in range(1, 51):
        x1 = (a[0][3] - a[0][1] * x2 - a[0][2] * x3) / a[0][0]
        x2 = (a[1][3] - a[1][0] * x1 - a[1][2] * x3) / a[1][1]
        x3 = (a[2][3] - a[2][0] * x1 - a[2][1] * x2) / a[2][2]
        e1 = abs((x1 - x0) / x1)
        e2 = abs((x2 - y0) / x2)
        e3 = abs((x3 - z0) / x3)
        x0, y0, z0 = x1, x2, x3
        if e1 < epsilon and e2 < epsilon and e3 < epsilon:
            break
    print(x0, y0, z0)
    return x0, y0, z0


if __name__ == '__main__':
    m = [[8, 4, -1, 11], [-2, 3, 1, 4], [2, -1, 6, 7], [2, -1, 6, 7]]
    m2 = [[1, 1, -1, -3], [6, 2, 2, 2], [-3, 4, 1, 1]]
    m3 = [[12, 3, -5, 1], [1, 5, 3, 28], [3, 7, 13, 76]]
    m4 = [[2, 3, 1, -4], [4, 1, 4, 9], [3, 4, 6, 0]]
    m5 = [[1, -2, -2, -3, 5], [3, -9, 0, -9, 6], [-1, 2, 4, 7, 5], [-3, -6, 26, 2, 6]]  # 4*4
    x = LU(m5)
    y = gauss_elimination(m5)
    z = gauss_jordan(m5)
    gauss_seidel(m5, 0.7)
