while True:
    m = []
    n = 1
    a = 0
    q = int(input())
    if q == 0:
     break
    elif q == 1:
        print(q)
    else:
        for i in range(q):
            x = []
            for l in range(q):
                x.append(n)
                n = n * 2
            m.append(x)
            n = m[a][1]
            a += 1
        t = len(str(m[i][l]))
        for x in m:
            for elem in range(q):
                print('{:{}}' .format(x[elem], t), end=' ') if elem < q-1 else print(
                    '{:{}}' .format(x[elem], t))
    print()
