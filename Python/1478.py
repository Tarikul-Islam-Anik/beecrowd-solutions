while True:
    num = int(input())
    if num == 0:
        break
    m = []
    for i in range(1, num+1):
        a = []
        c = i
        for j in range(num):
            a.append(abs(c))
            if c == 1:
                c -= 3
            else:
                c -= 1
        m.append(a)
    for i in range(num):
        s = ''
        for j in range(num):
            s += " %3d" % m[i][j]
        print(s[1:])
    print("")
