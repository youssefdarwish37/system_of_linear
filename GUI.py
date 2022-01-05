def jordan(n)

    print(arr)
    for i in range(n):
        if arr[i][i] == 0.0:
            print("divide by zero error")
            sys.exit()
        for j in range(n):
            if i == j:
                arr[i] = arr[i]/arr[i][i]
            else:
                m = arr[j][i] / arr[i][i]


                for k in range(n + 1):
                    arr[j][k] = arr[j][k] - m * arr[i][k]
    print(arr)
    for i in range(n):
        xs[i] = arr[i][n] / arr[i][i]
    print(xs)
#jordan(n)