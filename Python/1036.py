a, b, c = map(float, input().split())

if b * b - 4 * a * c < 0 or a == 0:
    print("Impossivel calcular")

else:
    r1 = (-b + (b**2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b**2 - 4 * a * c) ** 0.5) / (2 * a)

    print("R1 = {:.5f}".format(r1))
    print("R2 = {:.5f}".format(r2))
