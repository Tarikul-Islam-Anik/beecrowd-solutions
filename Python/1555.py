def r(x, y):
    return (3 * x) ** 2 + y**2


def b(x, y):
    return 2 * (x**2) + (5 * y) ** 2


def c(x, y):
    return -100 * x + y**3


for i in range(int(input())):
    x, y = map(float, input().split())
    if r(x, y) > b(x, y) and r(x, y) > c(x, y):
        print("Rafael ganhou")
    elif b(x, y) > r(x, y) and b(x, y) > c(x, y):
        print("Beto ganhou")
    elif c(x, y) > r(x, y) and c(x, y) > b(x, y):
        print("Carlos ganhou")
    else:
        print("Empate")
