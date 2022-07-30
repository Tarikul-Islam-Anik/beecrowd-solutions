n = int(input())
if n % 2 == 0:
    whites = blacks = int(n**2 / 2)
    print(f"{whites} casas brancas e {blacks} casas pretas")
else:
    whites = blacks = int((n**2 + 1) / 2)
    print(f"{whites} casas brancas e {blacks-1} casas pretas")
