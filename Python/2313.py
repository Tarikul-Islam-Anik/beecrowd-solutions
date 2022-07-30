a, b, c = map(int, input().split())
if a + c > b:
    if (a != b and b == c) or (a == c and a != b) or (a == b and c != b):
        if (
            pow(a, 2) == pow(b, 2) + pow(c, 2)
            or pow(b, 2) == pow(a, 2) + pow(c, 2)
            or pow(c, 2) == pow(a, 2) + pow(b, 2)
        ):
            print("Valido-Isoceles")
            print("Retangulo: S")
        else:
            print("Valido-Isoceles")
            print("Retangulo: N")
    elif a == b and a == c:
        if (
            pow(a, 2) == pow(b, 2) + pow(c, 2)
            or pow(b, 2) == pow(a, 2) + pow(c, 2)
            or pow(c, 2) == pow(a, 2) + pow(b, 2)
        ):
            print("Valido-Equilatero")
            print("Retangulo: S")
        else:
            print("Valido-Equilatero")
            print("Retangulo: N")

    elif a != b and b != c and a != c:
        if (
            pow(a, 2) == pow(b, 2) + pow(c, 2)
            or pow(b, 2) == pow(a, 2) + pow(c, 2)
            or pow(c, 2) == pow(a, 2) + pow(b, 2)
        ):
            print("Valido-Escaleno")
            print("Retangulo: S")
        else:
            print("Valido-Escaleno")
            print("Retangulo: N")
    else:
        print("Invalido")
else:
    print("Invalido")
