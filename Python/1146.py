while True:
    n = int(input())
    if n == 0:
        break
    str = ""
    for i in range(1, n + 1):
        str += f"{i} "
    print(str[:-1])
