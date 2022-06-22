while True:
    n = int(input())
    s = 0
    if n == 0:
        break
    if n % 2:
        n += 1
    for i in range(5):
        s += n
        n += 2
    print(s)
