values = input().split(" ")
a, b, c, d = values
a, b, c, d = int(a), int(b), int(c), int(d)


if c > 0 and d > 0 and a % 2 == 0:
    if b > c and d > a:
        if (c + d) > (a + b):
            print("Valores aceitos")
        else:
            print("Valores nao aceitos")
    else:
        print("Valores nao aceitos")
else:
    print("Valores nao aceitos")
