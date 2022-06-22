def count_digit(n):
    if n < 10:
        return 1
    else:
        return 1 + count_digit(n // 10)


for i in range(int(input())):
    x, y = map(int, input().split())
    print(count_digit(x**y))
