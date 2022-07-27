while True:
    m = int(input())
    s = 1
    a = 1
    matrix = []
    if m == 0:
        break
    for i in range(m):
        x = []
        for j in range(m):
            x.append(s)
        matrix.append(x)

    while m-2 > 0:
        for i in range(a, m-1):
            for j in range(a, m-1):
                matrix[i][j] = s+1
        s += 1
        a += 1
        m -= 1
    for i in matrix:
        for pos, j in enumerate(i):
            print('{:3}'.format(j), end="") if pos == 0 else print(
                '{:4}'.format(j), end="")
        print()
    print()
