for i in range(int(input())):
    pa, pb, ga, gb = map(float, input().split())

    s = 0

    while pa <= pb:
        pa += int(((pa * ga) / 100))
        pb += int(((pb * gb) / 100))
        s += 1
        if s > 100:
            break
    print("Mais de 1 seculo.") if s > 100 else print(s, "anos.")
