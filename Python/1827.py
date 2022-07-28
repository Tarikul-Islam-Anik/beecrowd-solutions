while True:
    try:
        n = int(input())
        sum = int(n / 3)
        elem = n - sum

        list = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            list[i][i] = 2

        j = 0
        for i in range(n - 1, -1, -1):
            list[j][i] = 3
            j += 1

        for i in range(sum, elem):
            for j in range(sum, elem):
                list[i][j] = 1

        list[int(n / 2)][int(n / 2)] = 4

        for i in range(n):
            for j in range(n):
                print(list[j][i], end="")
            print()
        print()

    except EOFError:
        break
