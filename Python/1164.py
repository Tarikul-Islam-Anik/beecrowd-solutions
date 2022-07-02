def is_perfect(n):
    return sum(i for i in range(1, n) if n % i == 0) == n


for i in range(int(input())):
    n = int(input())
    if is_perfect(n):
        print(n, "eh perfeito")
    else:
        print(n, "nao eh perfeito")
