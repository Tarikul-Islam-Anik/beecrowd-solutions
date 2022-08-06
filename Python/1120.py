while True:
    d, n = input().split()
    if d == "0" and n == "0":
        print(0)
        break
    while n.count(d):
        n = n.replace(d, "")
    if n == "":
        print(1)
    else:
        print(int(n))
