for i in range(int(input())):
    x, y = map(int, input().split())
    s = 0
    if x % 2 == 0:
        x += 1
    for j in range(y):
        s += x
        x += 2
    print(s)
