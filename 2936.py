portions = [300, 1500, 600, 1000, 150]

grams = 0

for i in portions:
    n = int(input())
    grams += n * i

print(grams + 225)
