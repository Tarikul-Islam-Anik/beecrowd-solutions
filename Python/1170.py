for i in range(int(input())):
    n = float(input())
    count = 0
    while n > 1:
        n /= 2
        count += 1
    print(count, "dias")
