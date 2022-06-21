salary = float(input())

if 0.00 <= salary <= 2000.00:
    print("Isento")
elif 2000.01 <= salary <= 3000.00:
    print("R$ {:.2f}".format((salary - 2000) * 0.08))
elif 3000.01 <= salary <= 4500.00:
    print("R$ {:.2f}".format((salary - 3000) * 0.18 + (1000 * 0.08)))
elif salary > 4500.00:
    print("R$ {:.2f}".format((salary - 4500) * 0.28 + (1500 * 0.18) + (1000 * 0.08)))
