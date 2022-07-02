evens = 0

for i in range(5):
    n = float(input())
    if n % 2 == 0:
        evens += 1

print(f"{evens} valores pares")
