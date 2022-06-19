positive = 0
sum = 0
for i in range(6):
    n = float(input())
    if n > 0:
        positive += 1
        sum += n


print(f"{positive} valores positivos")
print(f"{sum/positive:.1f}")
