par, impar = [], []

for i in range(15):
    n = int(input())
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    if len(par) == 5:
        for i in range(5):
            print(f"par[{i}] = {par[i]}")
        par = []
    if len(impar) == 5:
        for i in range(5):
            print(f"impar[{i}] = {impar[i]}")
        impar = []

if len(impar) > 0:
    for i in range(len(impar)):
        print(f"impar[{i}] = {impar[i]}")

if len(par) > 0:
    for i in range(len(par)):
        print(f"par[{i}] = {par[i]}")
