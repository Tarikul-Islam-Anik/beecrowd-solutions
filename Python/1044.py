a, b = map(int, input().split())

print("Sao Multiplos") if b % a == 0 or a % b == 0 else print("Nao sao Multiplos")
