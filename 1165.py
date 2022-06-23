def is_prime(n):
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))


for i in range(int(input())):
    n = int(input())
    if is_prime(n):
        print(n, "eh primo")
    else:
        print(n, "nao eh primo")
