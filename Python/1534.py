while True:
    try:
        n = int(input())
        lst = []
        for i in range(n):
            lst.append([])
            for j in range(n):
                lst[i].append("3")
        for i in range(n):
            lst[i][i] = "1"
            lst[i][n - i - 1] = "2"
        for i in range(n):
            for j in range(n):
                print(lst[i][j], end="")
            print()

    except EOFError:
        break
